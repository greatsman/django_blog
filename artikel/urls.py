from django.conf.urls import url
from . views import (
                        IndexView,
                        CreateView,
                        UpdateView,
                        DeleteView,
                    )

urlpatterns = [
    url(r"^update/(?P<pk>\d+)$",UpdateView.as_view(), name="update"),
    url(r"^delete/(?P<pk>\d+)$",DeleteView.as_view(), name="delete"),
    url(r"^add/$",CreateView.as_view(), name="add"),
    url(r'^(?P<page>\d+)$', IndexView.as_view(), name='index'),
]
