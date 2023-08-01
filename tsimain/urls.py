from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from register import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'contractors', views.ContractorViewSet)
router.register(r'contracts', views.ContractViewSet)
router.register(r'carnumbers', views.CarNumberViewSet)
router.register(r'fractions', views.FractionViewSet)
router.register(r'records', views.RecordViewSet)
router.register(r'registries', views.RegistryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', TemplateView.as_view(template_name='index.html'))
]
