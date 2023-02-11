from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .forms import UserForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
class Index(TemplateView):
    template_name = 'clone/index.html'

class About(TemplateView):
    template_name = 'clone/about.html'

class Blog(TemplateView):
    template_name = 'clone/blog.html'

class Blog_grid(TemplateView):
    template_name= 'clone/blog-grid.html'

class Blog_single(TemplateView):
    TemplateView = 'clone/blog-single.html'

class Service(TemplateView):
    template_name = 'clone/service.html'

class Contact(TemplateView):
    template_name = 'clone/contact.html'

class UserFormView(CreateView):
    template_name = 'clone/signup.html'
    success_url = reverse_lazy('signin')
    form_class = UserForm

class Signin(TemplateView):
    template_name = 'clone/signin.html'    

class Portfolio(TemplateView):
    template_name = 'clone/portfolio.html'

class Team(TemplateView):
    template_name = 'clone/team.html'

class Faq(TemplateView):
    template_name = 'clone/faq.html'

class Error(TemplateView):
    template_name = 'clone/team.html'

class Pricing(TemplateView):
    template_name = 'clone/pricing.html'

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'clone/dashboard.html'