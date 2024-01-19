from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.detail import DetailView
from .models import HomePageSlider, AboutPage, HomePage, Service, Process, Funfact, FAQ, CustomerComment, HomePageContactSection, Blog, Gallery
from django.urls import reverse_lazy
from .forms import ContactForm, AppointmentForm
from django.contrib import messages
from django.http import JsonResponse

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["slider"] = HomePageSlider.objects.first()
        context["about"] = AboutPage.objects.first()
        context["home"] = HomePage.objects.first()
        context["services"] = Service.objects.filter(is_home_page = True)[:5]
        context["processes"] = Process.objects.all()
        context["funfact"] = Funfact.objects.first()
        context["faqs"] = FAQ.objects.all()
        context["customer_comments"] = CustomerComment.objects.all()
        context["contact"] = HomePageContactSection.objects.first()
        context["blogs"] = Blog.objects.filter(is_home_page = True)[:3]
        return context
    
    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Form submitted successfully'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context["about"] = AboutPage.objects.first()
        context["funfact"] = Funfact.objects.first()
        context["processes"] = Process.objects.all()
        return context

class ServicePageView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicePageView, self).get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        
        return context
    
class ServiceDetailPageView(DetailView):
    template_name = 'service-detail.html'
    model = Service
    context_object_name = "service"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context
    
class BlogPageView(ListView):
    model = Blog
    template_name = 'blogs.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.all()
    
class BlogDetailPageView(DetailView):
    template_name = 'blog-detail.html'
    model = Blog
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailPageView, self).get_context_data(**kwargs)
        context["last_blogs"] = Blog.objects.exclude(pk = self.get_object().pk).order_by("-created")[:3]
        return context
    
class GalleryPageView(ListView):
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'galleries'
    paginate_by = 9

    def get_queryset(self):
        return Gallery.objects.all()
    
    
class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return JsonResponse({'status': 'success', 'message': 'Form submitted successfully'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})