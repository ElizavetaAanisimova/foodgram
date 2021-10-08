from rest_framework import permissions


class AuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.user.is_authenticated:
            return True
        return False
