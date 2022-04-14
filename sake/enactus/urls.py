from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# URLConf Module
urlpatterns = [
    path('hello/',views.say_hello),
    path('login/',views.login,name='login')
]

urlpatterns += staticfiles_urlpatterns()