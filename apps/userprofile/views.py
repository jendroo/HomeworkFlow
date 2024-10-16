from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from apps.userprofile.models import Teacher, Parent, Student
from apps.userprofile.serializers import TeacherSerializer, ParentSerializer, StudentSerializer


# Login 
class LoginApiView(APIView):
    # No need for permissions since this is for unauthenticated users
    def post(self, request):
        # Extract credentials from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            # Logs the user in and create a session
            login(request, user)

            # Determine user role and return the right profile
            if hasattr(user, 'teacher'):
                serializer = TeacherSerializer(user.teacher)
            elif hasattr(user, 'parent'):
                serializer = ParentSerializer(user.parent)
            else:
                serializer = StudentSerializer(user.student)

            # Return the serialized user profile
            return Response({'user': serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            # Return error if credentials are invalid
            return Response(
                {'error': 'invalid_credentials', 'detail': 'Invalid login credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )


# Logout View
class LogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Since the user is authenticated, it will log them out
        logout(request)
        return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)


# User Profile 
@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def user_profile(request):
    user = request.user

    # GET request to retrieve user profile
    if request.method == 'GET':
        if hasattr(user, 'teacher'):
            serializer = TeacherSerializer(user.teacher)
        elif hasattr(user, 'parent'):
            serializer = ParentSerializer(user.parent)
        else:
            serializer = StudentSerializer(user.student)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT request to update user profile
    elif request.method == 'PUT':
        if hasattr(user, 'teacher'):
            serializer = TeacherSerializer(user.teacher, data=request.data, partial=True)
        elif hasattr(user, 'parent'):
            serializer = ParentSerializer(user.parent, data=request.data, partial=True)
        else:
            serializer = StudentSerializer(user.student, data=request.data, partial=True)

        # Validate and save the updated profile
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Change Password 
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def change_password(request):
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    # Check if the old password is correct
    if not user.check_password(old_password):
        return Response(
            {'error': 'Invalid_Current_Password', 'detail': 'Old password is incorrect'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Set the new password
    user.set_password(new_password)
    user.save()

    # Keep the user logged in after password change
    update_session_auth_hash(request, user)

    return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
