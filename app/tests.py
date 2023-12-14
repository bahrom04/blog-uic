from app.models import Tag, Post
from django.test import TestCase

class TagTest(TestCase):
    def setUp(self):
        Tag.objects.create(title='Telegram')
        Tag.objects.create(title='Twitter')

    def test_socials_title(self):
        tag_named_telegram = Tag.objects.get(title='Telegram')
        tag_named_twitter = Tag.objects.get(title='Twitter')

        self.assertEqual(tag_named_telegram.tag_name(), 'Telegram')
        self.assertEqual(tag_named_twitter.tag_name(), 'Twitter')


