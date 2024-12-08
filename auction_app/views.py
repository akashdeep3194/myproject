from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):
    # Pass any context data to the dashboard template
    context = {
        'user': request.user,
        'welcome_message': f"Welcome, {request.user.username}!",
    }
    return render(request, 'dashboard.html', context)
