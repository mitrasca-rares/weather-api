
from rest_framework.permissions import BasePermission

class IsAuthenticatedAndOwner(BasePermission):
    message = 'You must be the owner of this object.'
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        print('has_object_permission called')
        return obj.owner == request.user