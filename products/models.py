from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class Category(MPTTModel):
    STATUS = (
        ('True', 'Aktif'),
        ('False', 'Aktif Değil')
    )

    title = models.CharField(
        'Başlık',
        max_length=40
    )

    keywords = models.CharField(
        'Anahtar Kelimeler',
        max_length=255
    )

    description = models.CharField(
        'Kategori Açıklaması',
        max_length=255
    )

    image = models.ImageField(
        'Kategori Fotoğrafı',
        blank=True,
        upload_to='images/'
    )

    status = models.CharField(
        'Kategori Durumu',
        max_length=10,
        choices=STATUS
    )

    slug = models.SlugField(
        'Kategori Etiketi',
        null=False,
        unique=True
    )

    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # @property
    # def get_image_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
    #     else:
    #         return "/uploads/images/333.jpg"

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={'slug': self.slug})
    # unique = True benzersiz slug üretmek için


class Product(models.Model):
    STATUS = (
        ('True', 'Stokta Var'),
        ('False', 'Stokta Yok')
    )

    

    category = models.ForeignKey(
        Category,
        on_delete=models.
            CASCADE
    )

    title = models.CharField(
        'Ürün İsmi',
        blank=True,
        max_length=40
    )

    keywords = models.CharField(
        'Anahtar Kelimeler',
        blank=True,
        max_length=255
    )

    description = models.CharField(
        'Ürün Açıklaması',
        blank=True,
        max_length=255
    )

    image = models.ImageField(
        'Ürün Fotoğrafı',
        blank=True,
        upload_to='images/',
        default='images/users/333.jpg'
    )

    image2 = models.ImageField(
        'Ürün Fotoğrafı 2',
        blank=True,
        upload_to='images/'
    )

    image3 = models.ImageField(
        'Ürün Fotoğrafı 3',
        blank=True,
        upload_to='images/'
    )

    price = models.FloatField(
        'Fiyat',
        blank=True
    )

    amount = models.IntegerField(
        'Adet',
        blank=True
    )

    slug = models.SlugField(
        null=False,
        unique=True
    )

    detail = RichTextUploadingField(
        'Ürün Detayı',
        blank=True
    )

    status = models.CharField(
        'Ürün Durumu',
        blank=True,
        max_length=10,
        choices=STATUS
    )

    

    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/uploads/users/333.jpg"

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={'slug': self.slug})
    # unique = True benzersiz slug üretmek için


class Images(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        'Başlık',
        max_length=50,
        blank=True
    )

    image = models.ImageField(
        'Fotoğraf',
        null=True,
        blank=True,
        upload_to='images/',
        default=''
    )

    # @property
    # def get_image_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
    #     else:
    #         return "/uploads/images/333.jpg"

    def __str__(self):
        return self.title


