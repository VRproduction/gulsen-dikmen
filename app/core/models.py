from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class GeneralSettings(models.Model):
    site_title = models.CharField(
        max_length=200, verbose_name="Saytın başlığı", null = True, blank = True)
    adress = models.CharField(max_length=1500, verbose_name="Ünvan", null=True, blank = True)
    phone_number = models.CharField(
        max_length=50, verbose_name="Nömrə", null=True, blank=True)
    email = models.EmailField(blank = True)
    g_adress = models.CharField(
        max_length=1500, verbose_name="Google Map linki", null=True, blank=True)
    g_adress_iframe = models.TextField(
        verbose_name="Google Map Iframe linki", null=True, blank=True)
    
    logo = models.FileField(verbose_name="logo",
                            blank=True, upload_to="general_settings_logo")
    mobile_logo = models.FileField(verbose_name="Mobile logo",
                                   help_text="Mobile logo", blank=True, null=True, upload_to="general_settings_mobile_logo")
    favicon = models.FileField(verbose_name="favicon",
                               blank=True, null=True, upload_to="general_settings_favicon")
    footer_logo = models.FileField(help_text="Footer logo", blank=True, null=True, upload_to="general_settings_footer_logo")
    footer_description = models.TextField(null = True, blank = True)
    copyright_title = models.CharField(max_length = 100, blank = True)
    pages_banner_image = models.ImageField(upload_to = 'banner_image', verbose_name = 'Səhiflərdəki banner photo', null = True, blank = True)
    facebook = models.CharField(
        max_length=200, verbose_name="Facebook", blank=True)
    instagram = models.CharField(
        max_length=200, verbose_name="Instagram", blank=True)
    youtube = models.CharField(
        max_length=200, verbose_name="Youtube", blank=True)
    tiktok = models.CharField(
        max_length=200, verbose_name="TikTok", blank=True)
    
    def __str__(self):
        return ('%s') % (self.site_title)

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "General Settings"

class WorkHour(models.Model):
    week_day = models.CharField(max_length = 100)
    hours = models.CharField(max_length = 100)
    settings = models.ForeignKey(GeneralSettings, on_delete = models.SET_NULL, null = True, blank = True, related_name = "work_hours")
    
    def __str__(self) -> str:
        return f'{self.week_day}: {self.hours}'

class HomePage(models.Model):
    consultancy_section_title = models.CharField(max_length = 200, null = True, blank = True)
    service_section_title = models.CharField(max_length = 200, null = True, blank = True)
    how_it_works_title = models.CharField(max_length = 200, null = True, blank = True)
    faq_big_image = models.ImageField(upload_to = "faq_big", null = True, blank = True)
    faq_small_image = models.ImageField(upload_to = "faq_small", null = True, blank = True)
    customer_comment_title = models.CharField(max_length = 200, null = True, blank = True)
    blog_section_title = models.CharField(max_length = 200, null = True, blank = True)

    def __str__(self):
        return "Ana səhifə"

    class Meta:
        verbose_name = "Ana səhifə"
        verbose_name_plural = "Ana səhifə"


class HomePageSlider(models.Model):
    title = models.CharField(max_length = 1000)
    description = models.TextField()

    def __str__(self):
        return "Ana səhifə slayder"

    class Meta:
        verbose_name = "Ana səhifə | Slayder"
        verbose_name_plural = "Ana səhifə | Slayder"


class HomePageSliderImage(models.Model):
    slider = models.ForeignKey(HomePageSlider, on_delete = models.SET_NULL, null = True, blank = True, related_name = "images")
    image =  models.ImageField(upload_to = 'home_page_slider')

    def __str__(self):
        return f"Şəkil {self.pk}"

    class Meta:
        verbose_name = "Şəkil"
        verbose_name_plural = "Şəkillər"

class AboutPage(models.Model):
    image = models.ImageField(upload_to = 'about')
    title = models.CharField(max_length = 500)
    description = models.TextField()
    experience = models.PositiveIntegerField(default = 10)

    def __str__(self):
        return "Haqqımızda"

    class Meta:
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"


class OurMission(models.Model):
    title = models.CharField(max_length = 300)
    about = models.ForeignKey(AboutPage, on_delete = models.SET_NULL, null = True, blank = True, related_name = "missions")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Missiya"
        verbose_name_plural = "Missiyalar"
    
class OurVision(models.Model):
    title = models.CharField(max_length = 300)
    about = models.ForeignKey(AboutPage, on_delete = models.SET_NULL, null = True, blank = True, related_name = "visions")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vizyon"
        verbose_name_plural = "Vizyonlar"


class Service(models.Model):
    title = models.CharField(max_length = 100)
    icon = models.ImageField(upload_to = 'service_icon', null = True)
    image = models.ImageField(upload_to = 'service')
    description = RichTextUploadingField(null = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"

class ServicePunkt(models.Model):
    title = models.CharField(max_length = 500)
    service = models.ForeignKey(Service, on_delete = models.SET_NULL, null = True, blank = True, related_name = "punkts")
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Punkt"
        verbose_name_plural = "Punktlar"

class Process(models.Model):
    image = models.ImageField(upload_to = 'process')
    title = models.CharField(max_length = 100)
    description = models.TextField()
    sequence = models.PositiveIntegerField(default = 1)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Proses"
        verbose_name_plural = "Biz necə işləyirik | Proseslər"
        ordering = ['sequence']

class Funfact(models.Model):
    experience = models.IntegerField(default = 1)
    different_services = models.IntegerField(default = 1)
    happy_patients = models.BigIntegerField(default = 1)
    article = models.IntegerField(default = 1)

    def __str__(self) -> str:
        return "Statistika"
    
    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistika"

class FAQ(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()

    def __str__(self):
        return ('%s') % (self.title)

    class Meta:
        verbose_name = "Sual"
        verbose_name_plural = "Suallar"

class CustomerComment(models.Model):
    image = models.ImageField(upload_to = 'customer_comments')
    full_name = models.CharField(max_length = 100)
    text = models.TextField()

    def __str__(self):
        return ('%s') % (self.full_name)

    class Meta:
        verbose_name = "Müştəri rəyi"
        verbose_name_plural = "Müştəri rəyləri"

class HomePageContactSection(models.Model):
    section_title = models.CharField(max_length = 200, null = True, blank = True)
    video_bg_image = models.ImageField(upload_to = 'contact', null = True)
    youtube_link = models.TextField(null = True, blank = True)

    def __str__(self):
        return "Əlaqə"

    class Meta:
        verbose_name = "Ana səhifə | Əlaqə hissəsi"
        verbose_name_plural = "Ana səhifə | Əlaqə hissəsi"


class BlogCategory(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar | Blog"

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = RichTextUploadingField()
    category = models.ForeignKey(BlogCategory, on_delete = models.SET_NULL, null = True, blank = True)
    image = models.ImageField(upload_to = 'blogs')
    created = models.DateField(auto_now_add = True)
    is_home_page = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bloq"
        verbose_name_plural = "Bloqlar"