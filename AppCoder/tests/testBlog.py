from django.test import TestCase
from AppCoder.models import Blog
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
import os
from django.conf import settings

class BlogModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un blog de prueba
        imagen = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        cls.blog = Blog.objects.create(titulo="Test Blog", subtitulo="Test Subtitle", cuerpo="Test body", autor="Test Author", fecha=timezone.now(), imagen=imagen)

    def tearDown(self):
        # Para eliminar la imagen despues de cada test
        if self.blog.imagen:
            path = os.path.join(settings.MEDIA_ROOT, self.blog.imagen.name)
            if os.path.exists(path):
                os.remove(path)

    def test_string_representation(self):
        expected = f"Blog Test Blog de Test Author con fecha {self.blog.fecha}"
        self.assertEqual(str(self.blog), expected)

    def test_blog_deletion(self):
        self.blog.delete()
        # Make sure the associated image file is also deleted
        path = os.path.join(settings.MEDIA_ROOT, self.blog.imagen.name)
        self.assertFalse(os.path.exists(path))