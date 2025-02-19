from django.urls import path, include
from .views import signup_view, home, equipments, experiments, chemicals, chatbot, login_view
from django.contrib.auth import views as auth_views

app_name = "login"

urlpatterns = [
    path("", home, name='home'),
    path('login/', login_view, name='login_page'),
    path("signup/", signup_view, name="signup_page"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("equipments/", equipments, name="equipments"),
    path("experiments/", experiments, name="experiments"),
    path("chemicals/", chemicals, name="chemicals"),
    path("chatbot/", chatbot, name="chatbot"),
]
