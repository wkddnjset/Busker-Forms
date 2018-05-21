from django.conf.urls import url
from .views import PerFormView

urlpatterns = [
    url(r'^perform/', PerFormView, name='form'),
]
