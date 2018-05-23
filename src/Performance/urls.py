from django.conf.urls import url
from .views import PerFormView, SuccessView, send_email, mail_form

urlpatterns = [
    url(r'^perform/', PerFormView, name='form'),
    url(r'^success/', SuccessView, name='success'),
    url(r'^mail-form/', mail_form, name='success'),
    url(r'^send/', send_email, name='mail'),
]
