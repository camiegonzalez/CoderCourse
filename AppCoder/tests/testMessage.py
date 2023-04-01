from django.test import TestCase
from django.utils import timezone
from AppCoder.models import Message

class MessageModelTestCase(TestCase):
    def setUp(self):
        self.message = Message.objects.create(user='John', message='Hello World')

    def test_message_data(self):
        self.assertIsInstance(self.message, Message)
        self.assertEqual(self.message.user, 'John')
        self.assertEqual(self.message.message, 'Hello World')
    
    
    def test_message_date(self):
        now = timezone.now()
        self.assertLessEqual(self.message.dateTime, now)
