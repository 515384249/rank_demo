from django.urls import path, include

urlpatterns = [
    path('rank/', include('apps.rank.urls'))
]
