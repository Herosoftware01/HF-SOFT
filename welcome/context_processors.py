from .models import UserPermission

def user_permissions(request):
    if request.user.is_authenticated:
        perm, _ = UserPermission.objects.get_or_create(user=request.user)
        return {'permission': perm}
    return {}