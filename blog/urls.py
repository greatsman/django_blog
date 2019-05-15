"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . views import BlogHomeView, BlogDashboardView, LoginFormView
from artikel.views import (
                            ArtikelDetailView,ArtikelKategoriListView,ArtikelListView,
                            )

from django.urls import reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)

urlpatterns = [
    url(r'^dashboard/artikel/', include("artikel.urls",namespace="dashboard_artikel")),
    url(r'^dashboard/', BlogDashboardView.as_view(), name='dashboard'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kategori/(?P<category>[\w\s]+)$', ArtikelKategoriListView.as_view(), name='category'),
    url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(), name='detail'),
    url(r'^(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
    url(r'^$', BlogHomeView.as_view(), name='home'),
]
