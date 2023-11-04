from rest_framework import routers
from .api import AulaViewSet, MateriaViewSet, ProfesorViewSet

router = routers.DefaultRouter()

router.register("profesores", ProfesorViewSet, "profesores")
router.register("materias", MateriaViewSet, "materias")
router.register("aulas", AulaViewSet, "aulas")

urlpatterns = router.urls