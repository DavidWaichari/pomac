from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.conf.urls import url
from users import views as core_views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('update-profile/update/<int:pk>/',login_required(views.ProfileUpdateView.as_view()),name= 'updateprofile'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
]