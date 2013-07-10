# Create your views here.
from rest_framework import viewsets

class JournalViewSet (viewsets.ModelViewSet):
	queryset = Journal.objects.all();
	serializer_class = JournalSerializer();

class PublisheriewSet (viewsets.ModelViewSet):
	queryset = Publisherobjects.all();
	serializer_class = Publishererializer();

class SubscriberViewSet (viewsets.ModelViewSet):
	queryset = Subscriber.objects.all();
	serializer_class = SubscriberSerializer();