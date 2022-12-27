from rest_framework import routers
from m2m.views import *


router = routers.SimpleRouter()
router.register(r'posts', PostViewset)
router.register(r'tags', TagViewset)
urlpatterns = router.urls
