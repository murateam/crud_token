from django.shortcuts import render


def redirect_users(request):
    return render(
        request,
        'core/main.html',
    )
