"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from mi_app import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('pages/', views.page_list, name='page_list'),
    path('pages/new/', views.page_new, name='page_new'),
    path('pages/<int:pk>/edit/', views.page_edit, name='page_edit'),  # Nueva ruta para editar
    path('pages/<int:pk>/delete/', views.page_delete, name='page_delete'),  # Nueva ruta para eliminar
    path('pages/<int:pk>/', views.page_detail, name='page_detail'),
    path('login/', views.custom_login, name='login'),
    path('home/', views.home, name='home'),
    path('about-me/', views.about_me, name='about_me'),
    path('logout/', LogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)