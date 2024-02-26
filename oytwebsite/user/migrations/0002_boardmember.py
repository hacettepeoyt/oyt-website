# Generated by Django 5.0.2 on 2024-02-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='board_member/')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('role', models.CharField(choices=[('Başkan', 'Başkan'), ('Başkan Yardımcısı', 'Başkan Yardımcısı'), ('Genel Sekreter', 'Genel Sekreter'), ('Eğitim ve Arge Sorumlusu', 'Eğitim ve Arge Sorumlusu'), ('Kurumsal İlişkiler Sorumlusu', 'Kurumsal İlişkiler Sorumlusu'), ('Mali İşler Sorumlusu', 'Mali İşler Sorumlusu'), ('Organizasyon Sorumlusu', 'Organizasyon Sorumlusu')], max_length=32)),
                ('website_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
            ],
        ),
    ]
