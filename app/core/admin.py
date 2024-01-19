from django.contrib import admin
from .models import *
MAX_OBJECTS = 1

class HomePageSliderImageInline(admin.TabularInline):
    model = HomePageSliderImage

@admin.register(HomePageSlider)
class HomePageSliderAdmin(admin.ModelAdmin):

    inlines = [HomePageSliderImageInline, ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
class OurMissionInline(admin.TabularInline):
    model = OurMission

class OurVisionInline(admin.TabularInline):
    model = OurVision

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):

    inlines = [OurMissionInline, OurVisionInline]

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    

class ServicePunktInline(admin.TabularInline):
    model = ServicePunkt

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    inlines = [ServicePunktInline, ]

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['title', 'sequence']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 3:
            return False
        return super().has_add_permission(request)
    
@admin.register(Funfact)
class FunfactAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
admin.site.register(FAQ)

@admin.register(CustomerComment)
class CustomerCommentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 3:
            return False
        return super().has_add_permission(request)
    
@admin.register(HomePageContactSection)
class HomePageContactSectionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    
admin.site.register(Blog)

class WorkHourInline(admin.TabularInline):
    model = WorkHour

@admin.register(GeneralSettings)
class AdminGeneralSettings(admin.ModelAdmin):
    inlines = [WorkHourInline,]

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Appointment)
