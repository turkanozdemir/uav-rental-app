from rest_framework import permissions


class isBrandUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        user_type = getattr(request.user, 'user_type', None)

        if user_type == 'brand' :
            return True

        return False

class isCustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        user_type = getattr(request.user, 'user_type', None)

        if user_type == 'custom':
            return True

        return False