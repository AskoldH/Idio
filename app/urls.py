from django.urls import path
from .views import IdiomView

urlpatterns = [
    path('idiom/', IdiomView.as_view(), name='idiom_view')
]