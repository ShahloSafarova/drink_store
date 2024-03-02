from .views import (UserCreateView, VerifyAPIView, GetNewVerification, ChangeUserInformationView,
                    ChangeUserPhotoView, LoginView, LoginRefreshView)
from django.urls import path

urlpatterns = [
    path("login", LoginView.as_view()),
    path("login/refresh", LoginRefreshView.as_view()),
    path("user-create", UserCreateView.as_view()),
    path('verify', VerifyAPIView.as_view()),
    path('new-verify', GetNewVerification.as_view()),
    path('change-info', ChangeUserInformationView.as_view()),
    path('add-photo', ChangeUserPhotoView.as_view()),
]