from django.views.generic import TemplateView
from artikel.views import ArtikelForHome
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)

class BlogHomeView(TemplateView,ArtikelForHome):
    template_name = "index.html"
    
    def get_context_data(self):
        context  =   {
                        'artikel_all_list':self.get_all_artikel(),
                        'artikel_each_category_list':self.get_latest_artikel_each_category(),
                        
                    }
        return context
    
class BlogDashboardView(LoginRequiredMixin,TemplateView):
    template_name = "index_admin.html"

class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = '/dashboard'
    success_message = "You were successfully logged in"

    
