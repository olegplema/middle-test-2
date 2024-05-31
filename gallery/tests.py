from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from gallery.models import Category, Image


class TestViews(TestCase):
    def setUp(self):
        self.categories = [
            Category.objects.create(name="Category 1"),
            Category.objects.create(name="Category 2"),
        ]
        self.image = Image.objects.create(
            title="Image 1",
            image=SimpleUploadedFile("test.jpg", b"file_content"),
            created_date="2022-01-01",
            age_limit=12,
        )
        self.image.categories.set(self.categories)

    def test_gallery_view_returns_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "gallery.html")

    def test_gallery_view_returns_correct_context(self):
        response = self.client.get("/")
        self.assertEqual(list(response.context["categories"]), self.categories)

    def test_image_detail_view_returns_correct_template(self):
        response = self.client.get(f"/image/{self.image.pk}/")
        self.assertTemplateUsed(response, "image_detail.html")

    def test_image_detail_view_returns_correct_context(self):
        response = self.client.get(f"/image/{self.image.pk}/")
        self.assertEqual(response.context["image"], self.image)
