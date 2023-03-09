def log_user(request):
    if not request.user.is_authenticated:
        return {}

    return {
        'log_user': request.user,
    }


def holder(request):
    return {'holder': 1} if request.user.is_staff is True else {}
