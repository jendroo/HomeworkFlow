from django.urls import path
from .views import LoginApiView, LogoutApiView, user_profile, change_password

app_name ='userprofile-urls'
urlpatterns = [
    # Login endpoint
    path('login/', LoginApiView.as_view(), name='login'),

    # Logout endpoint
    path('logout/', LogoutApiView.as_view(), name='logout'),

    # User profile (GET and PUT for viewing/updating profile)
    path('profile/', user_profile, name='user_profile'),

    # Change password
    path('change-password/', change_password, name='change_password'),
]