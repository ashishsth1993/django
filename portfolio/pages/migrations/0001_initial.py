# Generated by Django 2.1.7 on 2019-03-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('subheading', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField()),
                ('next_page_button', models.CharField(max_length=15)),
                ('image_1', models.ImageField(blank=True, upload_to='img/about_images')),
                ('image_1_alt', models.CharField(default='Image1', max_length=20)),
                ('image_2', models.ImageField(blank=True, upload_to='img/about_images')),
                ('image_2_alt', models.CharField(default='Image2', max_length=20)),
                ('image_3', models.ImageField(blank=True, upload_to='img/about_images')),
                ('image_3_alt', models.CharField(default='Image3', max_length=20)),
                ('image_4', models.ImageField(blank=True, upload_to='img/about_images')),
                ('image_4_alt', models.CharField(default='Image4', max_length=20)),
                ('image_5', models.ImageField(blank=True, upload_to='img/about_images')),
                ('image_5_alt', models.CharField(default='Image5', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.TextField(default='Lorem ipsum Dolor Mita')),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=15)),
                ('brand_name_2', models.CharField(max_length=15)),
                ('brand_heading', models.TextField(blank=True, null=True)),
                ('brand_paragraph', models.TextField(blank=True, null=True)),
                ('animation_text_1', models.CharField(blank=True, max_length=50, null=True)),
                ('animation_text_2', models.CharField(blank=True, max_length=50, null=True)),
                ('animation_text_3', models.CharField(blank=True, max_length=20, null=True)),
                ('next_page_button', models.CharField(max_length=12)),
                ('facebook_link', models.CharField(default='https://www.facebook.com', max_length=50)),
                ('twitter_link', models.CharField(default='https://www.twitter.com', max_length=50)),
                ('instagram_link', models.CharField(default='https://www.instagram.com', max_length=50)),
            ],
        ),
    ]
