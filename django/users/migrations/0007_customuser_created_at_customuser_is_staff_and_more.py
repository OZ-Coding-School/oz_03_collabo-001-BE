# Generated by Django 5.1 on 2024-08-09 08:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_customuser_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name="가입일자"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=False, verbose_name="운영진"),
        ),
        migrations.AddField(
            model_name="customuser",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정일자"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="nickname",
            field=models.CharField(default="날다람쥐cvoj2", max_length=255, unique=True, verbose_name="닉네임"),
        ),
    ]
