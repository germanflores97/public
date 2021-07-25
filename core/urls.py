from django.urls import path
from .views import IndexTemplateView, TemplateView

urlpatterns=[
    path('', IndexTemplateView.as_view(), name = 'index')
]