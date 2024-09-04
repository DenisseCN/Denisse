"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView , LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.Usuario.urls')),
    path('', include('apps.poleras.urls')),
    path('', include('apps.contacto.urls')),
    path('', include('apps.carrito.urls')),

    
    # Login and Logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home.html', TemplateView.as_view(template_name='home.html'), name='home_alternate'),

    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_forms.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name = 'password_reset_done'),
    path('reset/password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

