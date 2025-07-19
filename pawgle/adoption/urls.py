from django.urls import path
from adoption import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate_pet, name='donate_pet'),
    path('my-donations/', views.my_donations, name='my_donations'),
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('adopt/<int:pk>/', views.adopt_pet, name='adopt_pet'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='adoption/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
   
    
    path('adopt/<int:pk>/', views.adopt_pet, name='adopt_pet'),
    path('adoption-submitted/', views.adoption_submitted, name='adoption_submitted'),
    path('my-adoptions/', views.my_adoptions, name='my_adoptions'),
    path('cancel-adoption/<int:pk>/', views.cancel_adoption, name='cancel_adoption'),


path('admin/adoption-requests/', views.all_adoption_requests, name='all_adoption_requests'),
path('admin/update-adoption-status/<int:pk>/', views.update_adoption_status, name='update_adoption_status'),

path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='adoption/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='adoption/passwordchangedone.html'), name='passwordchangedone'),
    
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='adoption/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='adoption/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='adoption/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='adoption/password_reset_complete.html'), name="password_reset_complete"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
