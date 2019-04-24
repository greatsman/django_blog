from django.views.generic import TemplateView
from artikel.views import ArtikelForHome

class BlogHomeView(TemplateView,ArtikelForHome):
    template_name = "index.html"
    
    def get_context_data(self):
        context  =   {
                        'artikel_all_list':self.get_all_artikel(),
                        'artikel_each_category_list':self.get_latest_artikel_each_category(),
                        
                    }
        return context
    
class BlogDashboardView(TemplateView):
    template_name = "index_admin.html"

    
