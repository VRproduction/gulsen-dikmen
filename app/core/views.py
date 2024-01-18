from django.views.generic import TemplateView
from .models import HomePageSlider, AboutPage, HomePage, Service, Process, Funfact, FAQ, CustomerComment, HomePageContactSection, Blog

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
            context = super(HomePageView, self).get_context_data(**kwargs)
            context["slider"] = HomePageSlider.objects.first()
            context["about"] = AboutPage.objects.first()
            context["home"] = HomePage.objects.first()
            context["services"] = Service.objects.all()[:5]
            context["processes"] = Process.objects.all()
            context["funfact"] = Funfact.objects.first()
            context["faqs"] = FAQ.objects.all()
            context["customer_comments"] = CustomerComment.objects.all()
            context["contact"] = HomePageContactSection.objects.first()
            context["blogs"] = Blog.objects.filter(is_home_page = True)[:3]
            return context