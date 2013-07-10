from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'journals', views.JournalViewSet)
router.register(r'subscriber', views.SubscriberViewSet)
router.register(r'publishers', views.PublisherViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls))
);