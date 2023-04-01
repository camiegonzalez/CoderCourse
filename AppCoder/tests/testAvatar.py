from django.test import TestCase
from django.contrib.auth.models import User
from AppCoder.models import Avatar

class AvatarModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Creo un usuario de prueba. Tuve que buscar en internet como hacer esto
        test_user = User.objects.create_user(username='testuser', password='testpass')

        # Creo un avatar de prueba
        test_avatar = Avatar.objects.create(
            user=test_user,
            imagen='avatares/test_avatar.jpg'
        )

    def test_avatar_user(self):
        avatar = Avatar.objects.get(id=1)
        self.assertEqual(avatar.user.username, 'testuser')

    def test_avatar_user_max_length(self):
        avatar = Avatar.objects.get(id=1)
        max_length = avatar._meta.get_field('user').max_length
        self.assertEqual(max_length, 100)

    def test_avatar_imagen_upload_to(self):
        avatar = Avatar.objects.get(id=1)
        upload_to = avatar._meta.get_field('imagen').upload_to
        self.assertEqual(upload_to, 'avatares')

    def test_avatar_str(self):
        avatar = Avatar.objects.get(id=1)
        self.assertEqual(str(avatar), f"{avatar.user} - {avatar.imagen}")