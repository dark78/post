from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
import views

router = DefaultRouter()
router.register(r'journals', views.JournalViewSet)
router.register(r'subscribers', views.SubscriberViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'cities', views.CityViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls))
);