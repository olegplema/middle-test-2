from django.shortcuts import get_object_or_404, render

from .models import Category, Image


def gallery_view(request):
    categories = Category.objects.all()
    return render(request, "gallery.html", {"categories": categories})


def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, "image_detail.html", {"image": image})
