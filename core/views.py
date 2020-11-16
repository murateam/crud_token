from django.shortcuts import render, redirect

def redirect_users(request):
	return render(
		request,
		'core/main.html',
		)

# redirect from main url
# def redirect_users(request):
# 	return redirect('api/v1/users/', permanent=True)
