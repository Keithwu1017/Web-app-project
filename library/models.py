from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

def picture_directory_path(instance, filename):
    # Clean the book title to create a valid directory name
    book_title_slug = slugify(instance.book.title)
    # Return the path where the image will be saved
    return f'{book_title_slug}/{filename}'

# Create your models here.

class PictureBook(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    n_pages = models.IntegerField()
    likes = models.IntegerField(default=0)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
class Picture(models.Model):
    book = models.ForeignKey(PictureBook, on_delete=models.CASCADE, related_name='pictures')
    page_number = models.IntegerField()
    image = models.ImageField(upload_to=picture_directory_path, max_length=300)

    class Meta:
        ordering = ['page_number']  # Ensures pictures are ordered by page number

    def __str__(self):
        return f"{self.book.title} - Page {self.page_number}"
    
