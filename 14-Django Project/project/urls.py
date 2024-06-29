"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import post_list , post_detail , post_create , post_edit , delete_post
from posts.api import PostAPI,PostDetailAPI #,PostUpdateAPI,PostCreateAPI,PostDeleteAPi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    
    path('blog/' , post_list) , 
    path('blog/create' , post_create),
    path('blog/<int:post_id>' , post_detail) , 
    path('blog/<int:post_id>/edit' , post_edit) , 
    path('blog/<int:post_id>/delete' , delete_post) , 
    
    path('blog/api' , PostAPI.as_view()) , 
    # path('blog/api/create' , PostCreateAPI.as_view()),
    path('blog/api/<int:pk>' , PostDetailAPI.as_view()) , 
    # path('blog/api/<int:pk>/edit' , PostUpdateAPI.as_view()) , 
    # path('blog/api/<int:pk>/delete' , PostDeleteAPi.as_view()) , 
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
