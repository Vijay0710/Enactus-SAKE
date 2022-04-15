from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# URLConf Module
urlpatterns = [
    path('hello/',views.say_hello),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('product_details',views.product_details,name='product_details')
]

urlpatterns += staticfiles_urlpatterns()