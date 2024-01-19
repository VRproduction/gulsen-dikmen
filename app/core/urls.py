from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('services/', views.ServicePageView.as_view(), name = 'services'),
    path('services/<slug:slug>/', views.ServiceDetailPageView.as_view(), name='service-detail'),
    path('blogs/', views.BlogPageView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.BlogDetailPageView.as_view(), name='blog-detail'),
    path('gallery/', views.GalleryPageView.as_view(), name='gallery'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]
