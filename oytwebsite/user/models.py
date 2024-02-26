from PIL import Image
from django.db import models


class Member(models.Model):
    DEGREE_CHOICES = (
        ('Hazırlık', 'Hazırlık'),
        ('1. Sınıf', '1. Sınıf'),
        ('2. Sınıf', '2. Sınıf'),
        ('3. Sınıf', '3. Sınıf'),
        ('4. Sınıf', '4. Sınıf'),
        ('5. Sınıf', '5. Sınıf'),
        ('6. Sınıf', '6. Sınıf'),
        ('Yüksek Lisans', 'Yüksek Lisans'),
        ('Doktora', 'Doktora'),
        ('Mezun', 'Mezun')
    )

    GROUP_CHAT_PLATFORM_CHOICES = (
        ('Signal', 'Signal'),
        ('Telegram', 'Telegram'),
        ('WhatsApp', 'WhatsApp')
    )

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    student_id = models.CharField(max_length=15)
    department = models.CharField(max_length=64)
    degree = models.CharField(max_length=15, choices=DEGREE_CHOICES)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    group_chat_platform = models.CharField(max_length=8, choices=GROUP_CHAT_PLATFORM_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.student_id


class BoardMember(models.Model):
    ROLE_CHOICES = (
        ('Başkan', 'Başkan'),
        ('Başkan Yardımcısı', 'Başkan Yardımcısı'),
        ('Genel Sekreter', 'Genel Sekreter'),
        ('Eğitim ve Arge Sorumlusu', 'Eğitim ve Arge Sorumlusu'),
        ('Kurumsal İlişkiler Sorumlusu', 'Kurumsal İlişkiler Sorumlusu'),
        ('Mali İşler Sorumlusu', 'Mali İşler Sorumlusu'),
        ('Halkla İlişkiler Sorumlusu', 'Halkla İlişkiler Sorumlusu'),
        ('Organizasyon Sorumlusu', 'Organizasyon Sorumlusu')
    )

    profile_picture = models.ImageField(upload_to='board_member/')
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    role = models.CharField(max_length=32, choices=ROLE_CHOICES)
    website_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.role}'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
