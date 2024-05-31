from django.test import Client, TestCase
from django.urls import reverse

from .models import Category, Image


class GalleryViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category1 = Category.objects.create(name="Category 1")
        self.category2 = Category.objects.create(name="Category 2")

    def test_gallery_view_retrieves_all_categories(self):
        response = self.client.get(reverse("gallery_view"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gallery.html")
        self.assertIn("categories", response.context)
        self.assertEqual(len(response.context["categories"]), 2)

    def test_gallery_view_renders_correct_template(self):
        response = self.client.get(reverse("gallery_view"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gallery.html")


class ImageDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Category 1")
        self.image = Image.objects.create(title="Test Image", category=self.category)

    def test_image_detail_view_retrieves_image(self):
        response = self.client.get(reverse("image_detail", args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "image_detail.html")
        self.assertIn("image", response.context)
        self.assertEqual(response.context["image"].id, self.image.id)

    def test_image_detail_view_renders_correct_template(self):
        response = self.client.get(reverse("image_detail", args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "image_detail.html")

    def test_image_detail_view_returns_404_for_nonexistent_image(self):
        response = self.client.get(reverse("image_detail", args=[999]))
        self.assertEqual(response.status_code, 404)
