from rest_framework import routers
from m2m.views import *
from django.urls import path


# router = routers.SimpleRouter()
# router.register(r'posts', PostViewset)
# router.register(r'tags', TagViewset)
# urlpatterns = router.urls

urlpatterns = [
    path('home/', AdelView.as_view() , name="home-url"),
]