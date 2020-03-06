from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from register import views as v
from mysite.core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",v.register,name="register"),
    
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    
    path('',TemplateView.as_view(template_name="login/index.html")),
    path('accounts/',include('allauth.urls')),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
