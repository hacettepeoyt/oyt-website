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
