from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings

# from django.conf.urls.static import static

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('home/', views.home, name='home'),
    path('man/', views.man, name='man'),
    path('woman/', views.woman, name='woman'),
    path('accessories/', views.accessories, name='accessories'),
    path('bracelets/', views.bracelets, name='bracelets'),
    # path('upload/', views.upload_file, name='upload-file'),

    path('create/', views.create, name='create'),
    path('create/new', views.new, name='new'),
    path('create/report', views.report, name='report'),


]


