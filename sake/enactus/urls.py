from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# URLConf Module
urlpatterns = [
    path('hello/',views.say_hello),
    path('login/',views.login,name='login'),
    path('admin_01/',views.admin_01,name='admin_main'),
    path('admin_02/',views.admin_02,name='admin2'),
    path('profile_01/',views.profile_01,name='profile_01'),
    path('register/',views.register,name='register'),
    path('product_details',views.product_details,name='product_details')
]

urlpatterns += staticfiles_urlpatterns()