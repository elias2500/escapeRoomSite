from rest_framework import permissions

class OnlyOwnerCanRead(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == permissions.GET:
            return obj.user == request.user

        return obj.user == request.user