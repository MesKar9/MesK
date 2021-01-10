from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User


# Create your models here.


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )

    title = models.CharField(
        'Başlık',
        blank=True,
        max_length=40
    )

    keywords = models.CharField(
        'Anahtar Kelimeler',
        blank=True,
        max_length=255
    )

    description = models.CharField(
        'Açıklama',
        blank=True,
        max_length=40
    )

    company = models.CharField(
        'Şirket Adı',
        blank=True,
        max_length=40
    )

    address = models.CharField(
        'Adres',
        blank=True,
        max_length=200
    )

    phone = models.CharField(
        'Telefon',
        blank=True,
        max_length=20
    )

    fax = models.CharField(
        'Faks',
        blank=True,
        max_length=20
    )

    email = models.CharField(
        'E-Mail',
        blank=True,
        max_length=30
    )

    smtpServer = models.CharField(
        'SMTP Server',
        blank=True,
        max_length=20
    )

    smtpEmail = models.CharField(
        'SMTP Email',
        blank=True,
        max_length=30
    )

    smtpPassword = models.CharField(
        'SMTP Pass',
        blank=True,
        max_length=20
    )

    smtpPort = models.CharField(
        blank=True,
        max_length=5
    )

    icon = models.ImageField(
        blank=True,
        upload_to='images/'
    )

    facebook = models.CharField(
        'Facebook',
        blank=True,
        max_length=40
    )

    instagram = models.CharField(
        'İnstagram',
        blank=True,
        max_length=40
    )
    twitter = models.CharField(
        'Twitter',
        blank=True,
        max_length=40
    )

    aboutUs = RichTextUploadingField(
        'Hakkımızda',
        blank=True
    )
    contact = RichTextUploadingField(
        'İletişim',
        blank=True
    )

    references = RichTextUploadingField(
        'Referanslar',
        blank=True
    )

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read')
    )

    contact_firstName = models.CharField(
        'İsim',
        blank=True,
        max_length=30
    )

    contact_lastName = models.CharField(
        'Soyisim',
        blank=True,
        max_length=30
    )

    contact_email = models.EmailField(
        'E-mail',
        max_length=30
    )

    contact_subject = models.CharField(
        'Konu',
        max_length=20
    )

    contact_message = RichTextUploadingField(
        'Mesaj',
        max_length=2000
    )

    contact_status = models.CharField(
        max_length=10,
        choices=STATUS,
        default='new'
    )

    contact_ip = models.CharField(
        blank=True,
        max_length=20
    )

    contact_note = models.CharField(
        blank=True,
        max_length=100
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_firstName


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = (
            'contact_firstName',
            'contact_lastName',
            'contact_email',
            'contact_subject',
            'contact_message',
        )


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        blank=True,
        max_length=20
    )

    address = models.CharField(
        blank=True,
        max_length=200
    )

    city = models.CharField(
        blank=True,
        max_length=20
    )

    

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.username


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = (

            'phone',
            'address',
            'city',


        )
