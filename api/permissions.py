from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_teacher)


class IsTeacherWrite(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_teacher)


class IsSelfWrite(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user == view.get_object())


class IsChatParticipant(BasePermission):
    def has_permission(self, request, view):
        chat = view.get_object()
        return bool(
            request.user and
            request.user in (chat.student, chat.teacher)
        )


class IsMessageSender(BasePermission):
    def has_permission(self, request, view):

        return bool(
            request.user and
            request.user == view.get_object().sender
        )


class IsRelationshipParticipant(BasePermission):
    def has_permission(self, request, view):
        relationship = view.get_object()
        return bool(
            request.user and
            request.user in (relationship.student, relationship.teacher)
        )
