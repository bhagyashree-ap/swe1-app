import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


def make_question(text, days):
    return Question.objects.create(
        question_text=text,
        pub_date=timezone.now() + datetime.timedelta(days=days),
    )


class PollViewsTests(TestCase):
    def test_index_empty(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls yet")

    def test_index_hides_future_questions(self):
        future = make_question("Future", 1)
        past = make_question("Past", -1)
        response = self.client.get(reverse("polls:index"))
        self.assertNotContains(response, future.question_text)
        self.assertContains(response, past.question_text)

    def test_detail_hides_future_questions(self):
        question = make_question("Future", 1)
        response = self.client.get(reverse("polls:detail", args=(question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_vote_increments_choice_and_redirects(self):
        question = make_question("Favorite color?", -1)
        choice = Choice.objects.create(question=question, choice_text="Blue")
        response = self.client.post(reverse("polls:vote", args=(question.id,)), {"choice": choice.id})
        choice.refresh_from_db()
        self.assertEqual(choice.votes, 1)
        self.assertRedirects(response, reverse("polls:results", args=(question.id,)))

    def test_vote_without_selection_shows_error(self):
        question = make_question("Favorite color?", -1)
        response = self.client.post(reverse("polls:vote", args=(question.id,)), {})
        self.assertContains(response, "You didn&#x27;t select a choice.")
