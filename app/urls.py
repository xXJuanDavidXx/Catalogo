
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView, CustomLoginView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('catalogo/<int:user_id>/', views.list_products, name='catalogo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('logout/',views.singout, name='logout'),
    path('', views.list_products, name='lista_lociones'),
    path('copiar/', views.copiar, name='copiar')

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
