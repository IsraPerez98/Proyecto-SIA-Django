from django.urls import path, include

from . import views
from allauth.socialaccount.views import SignupView
from .forms import RegistroForm

urlpatterns = [
    #url(r"^signup/$", SignupView.as_view(form_class=RegistroForm), name="registro"),
    path("",include('allauth.urls'))
]
