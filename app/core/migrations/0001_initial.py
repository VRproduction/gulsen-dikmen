# Generated by Django 5.0.1 on 2024-01-18 11:10

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('experience', models.PositiveIntegerField(default=10)),
            ],
            options={
                'verbose_name': 'Haqqımızda',
                'verbose_name_plural': 'Haqqımızda',
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Kateqoriya',
                'verbose_name_plural': 'Kateqoriyalar | Blog',
            },
        ),
        migrations.CreateModel(
            name='CustomerComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='customer_comments')),
                ('full_name', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Müştəri rəyi',
                'verbose_name_plural': 'Müştəri rəyləri',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Sual',
                'verbose_name_plural': 'Suallar',
            },
        ),
        migrations.CreateModel(
            name='Funfact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField(default=1)),
                ('different_services', models.IntegerField(default=1)),
                ('happy_patients', models.BigIntegerField(default=1)),
                ('article', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Statistika',
                'verbose_name_plural': 'Statistika',
            },
        ),
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Saytın başlığı')),
                ('adress', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ünvan')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nömrə')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('g_adress', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Google Map linki')),
                ('g_adress_iframe', models.TextField(blank=True, null=True, verbose_name='Google Map Iframe linki')),
                ('logo', models.FileField(blank=True, upload_to='general_settings_logo', verbose_name='logo')),
                ('mobile_logo', models.FileField(blank=True, help_text='Mobile logo', null=True, upload_to='general_settings_mobile_logo', verbose_name='Mobile logo')),
                ('favicon', models.FileField(blank=True, null=True, upload_to='general_settings_favicon', verbose_name='favicon')),
                ('footer_logo', models.FileField(blank=True, help_text='Footer logo', null=True, upload_to='general_settings_footer_logo')),
                ('footer_description', models.TextField(blank=True, null=True)),
                ('copyright_title', models.CharField(blank=True, max_length=100)),
                ('pages_banner_image', models.ImageField(blank=True, null=True, upload_to='banner_image', verbose_name='Səhiflərdəki banner photo')),
                ('facebook', models.CharField(blank=True, max_length=200, verbose_name='Facebook')),
                ('instagram', models.CharField(blank=True, max_length=200, verbose_name='Instagram')),
                ('youtube', models.CharField(blank=True, max_length=200, verbose_name='Youtube')),
                ('tiktok', models.CharField(blank=True, max_length=200, verbose_name='TikTok')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'General Settings',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultancy_section_title', models.CharField(blank=True, max_length=200, null=True)),
                ('service_section_title', models.CharField(blank=True, max_length=200, null=True)),
                ('how_it_works_title', models.CharField(blank=True, max_length=200, null=True)),
                ('faq_big_image', models.ImageField(blank=True, null=True, upload_to='faq_big')),
                ('faq_small_image', models.ImageField(blank=True, null=True, upload_to='faq_small')),
                ('customer_comment_title', models.CharField(blank=True, max_length=200, null=True)),
                ('blog_section_title', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Ana səhifə',
                'verbose_name_plural': 'Ana səhifə',
            },
        ),
        migrations.CreateModel(
            name='HomePageContactSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(blank=True, max_length=200, null=True)),
                ('video_bg_image', models.ImageField(null=True, upload_to='contact')),
                ('youtube_link', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Ana səhifə | Əlaqə hissəsi',
                'verbose_name_plural': 'Ana səhifə | Əlaqə hissəsi',
            },
        ),
        migrations.CreateModel(
            name='HomePageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Ana səhifə | Slayder',
                'verbose_name_plural': 'Ana səhifə | Slayder',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='process')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('sequence', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Proses',
                'verbose_name_plural': 'Biz necə işləyirik | Proseslər',
                'ordering': ['sequence'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.ImageField(null=True, upload_to='service_icon')),
                ('image', models.ImageField(upload_to='service')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
            ],
            options={
                'verbose_name': 'Xidmət',
                'verbose_name_plural': 'Xidmətlər',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='blogs')),
                ('created', models.DateField(auto_now_add=True)),
                ('is_home_page', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.blogcategory')),
            ],
            options={
                'verbose_name': 'Bloq',
                'verbose_name_plural': 'Bloqlar',
            },
        ),
        migrations.CreateModel(
            name='HomePageSliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_page_slider')),
                ('slider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='core.homepageslider')),
            ],
            options={
                'verbose_name': 'Şəkil',
                'verbose_name_plural': 'Şəkillər',
            },
        ),
        migrations.CreateModel(
            name='OurMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('about', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='missions', to='core.aboutpage')),
            ],
            options={
                'verbose_name': 'Missiya',
                'verbose_name_plural': 'Missiyalar',
            },
        ),
        migrations.CreateModel(
            name='OurVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('about', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visions', to='core.aboutpage')),
            ],
            options={
                'verbose_name': 'Vizyon',
                'verbose_name_plural': 'Vizyonlar',
            },
        ),
        migrations.CreateModel(
            name='ServicePunkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='punkts', to='core.service')),
            ],
            options={
                'verbose_name': 'Punkt',
                'verbose_name_plural': 'Punktlar',
            },
        ),
        migrations.CreateModel(
            name='WorkHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(max_length=100)),
                ('hours', models.CharField(max_length=100)),
                ('settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='work_hours', to='core.generalsettings')),
            ],
        ),
    ]
