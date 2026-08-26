import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):
    try:
        response = requests.get(settings.API_URL, timeout=10)
        response.raise_for_status()
        posts = response.json()
    except requests.RequestException:
        posts = []

    total_responses = len(posts)

    data = {
        'title': "Landing Page' Dashboard",
        'posts': posts[:5],
        'total_responses': total_responses,
    }

    return render(request, 'dashboard/index.html', data)
