from django.urls import path
from .views import LoginApiView, LogoutApiView, user_profile, change_password

urlpatterns = [
    # Login endpoint
    path('api/v1/user/login/', LoginApiView.as_view(), name='login'),

    # Logout endpoint
    path('api/v1/user/logout/', LogoutApiView.as_view(), name='logout'),

    # User profile (GET and PUT for viewing/updating profile)
    path('api/v1/user/profile/', user_profile, name='user_profile'),

    # Change password
    path('api/v1/user/change-password/', change_password, name='change_password'),
]


# Login (/api/v1/user/login/):

#View: LoginApiView
#Method: POST
#Purpose: Handles user login by authenticating the username and password.


#Logout (/api/v1/user/logout/):

#View: LogoutApiView
#Method: POST
##Purpose: Logs out the currently authenticated user.


#User Profile (/api/v1/user/profile/):

#View: user_profile
#Methods:
#GET: Retrieves the current user's profile based on their role (Teacher, Parent, or Student).
#PUT: Allows updating the user's profile with partial updates (only the fields provided will be updated).
#Purpose: Manages user profile retrieval and updates.


#Change Password (/api/v1/user/change-password/):

#View: change_password
#Method: POST
#Purpose: Allows users to change their password after verifying the current password.

