from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from core.views import redirect_users

urlpatterns = [
	path('', redirect_users),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # get auth token
    path('api/v1/users/', include('accounts.urls'), name='users'),
]
