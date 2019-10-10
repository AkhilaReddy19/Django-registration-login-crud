from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [

    #url('^$', views.registration, name='index'),

    path('registration/',views.registration,name="registration"),
    path('Login/',views.Login,name="Login"),
    path('success/',views.success,name="success"),
    path('edit/<int:id>', views.edit,name="edit"),
    path('update/<int:id>', views.update,name="update"),
    path('view_profile/<int:id>', views.view_profile,name="view_profile"),
    path('home/<int:id>',views.home,name="home")

#   url(r'update/(?P<pk>[0-9]+)/$',views.update.as_view())
]
