from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from . models import Artikel
from . forms import ArtikelForm

class IndexView(ListView):
    model = Artikel
    template_name = "artikel/index.html"
    ordering = ['-published']
    paginate_by = 5

class CreateView(CreateView):
    form_class = ArtikelForm
    template_name = "artikel/create.html"

class UpdateView(UpdateView):
    form_class = ArtikelForm
    model = Artikel
    template_name = "artikel/update.html"

class DeleteView(DeleteView):
    model = Artikel
    template_name = "artikel/delete.html"
    success_url = reverse_lazy("dashboard_artikel:index",kwargs={"page":1})


  
# for home
class ArtikelForHome():
    model = Artikel
    def get_all_artikel(self):
        artikel_list = self.model.objects.all().order_by('-published')
        return artikel_list
    
    def get_latest_artikel_each_category(self):
        kategori_list = self.model.objects.values_list('kategori',flat=True).distinct()
        artikel_list = []
        
        for kategori in kategori_list:
            artikel = self.model.objects.filter(kategori=kategori).latest('published')
            artikel_list.append(artikel)
            
        return artikel_list
 
class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name = "kategori_list.html"
    context_object_name = "artikel_list"
    ordering = ['-published']
    paginate_by = 5
    
    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['category'])
        return super().get_queryset()
    
    def get_context_data(self,*args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori',flat=True).distinct().exclude(kategori=self.kwargs['category'])
        self.kwargs.update({'kategori_list':kategori_list,
                            'heading_kategori':self.kwargs['category'],
                            })
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
    
class ArtikelListView(ListView):
    model = Artikel
    template_name = "list.html"
    context_object_name = "artikel_list"
    ordering = ['-published']
    paginate_by = 5
    
    def get_context_data(self,*args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori',flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
    
class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "detail.html"
    context_object_name = "artikel"

    def artikel_sebelum_sesudah(self):
        artikel_semua=  list(self.model.objects.values_list('slug',flat=True).order_by('-published'))
        artikel_saat_ini =  artikel_semua.index(self.kwargs['slug'])
        if artikel_saat_ini<len(artikel_semua):
            if artikel_saat_ini==0:
                artikel_sebelumnya = artikel_semua[artikel_saat_ini+1]
                artikel_berikutnya = None
            elif artikel_saat_ini==len(artikel_semua)-1:
                artikel_sebelumnya = None
                artikel_berikutnya = artikel_semua[artikel_saat_ini-1]
            else:
                artikel_sebelumnya = artikel_semua[artikel_saat_ini+1]
                artikel_berikutnya = artikel_semua[artikel_saat_ini-1]
              
        hasil = {"next":artikel_berikutnya,"previous":artikel_sebelumnya}
        return hasil
    
    def get_context_data(self,*args, **kwargs):
        artikel_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(slug=self.kwargs['slug'])
        kategori_list = self.model.objects.values_list('kategori',flat=True).distinct().exclude(kategori=self.object.kategori)
        self.kwargs.update({'artikel_serupa':artikel_serupa,
                            'kategori_list':kategori_list,
                            'next':self.artikel_sebelum_sesudah()['next'],
                            'previous':self.artikel_sebelum_sesudah()['previous'],
                            })
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
        

