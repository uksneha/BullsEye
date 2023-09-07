from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search_result/', views.search_result, name='search_result'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    # path("__debug__/", include("debug_toolbar.urls")),
]