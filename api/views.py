# Create your views here.
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from models import *
from django.shortcuts import get_object_or_404

class SubscriberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscriber

class SubscribtionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscribtion
	subscriber = SubscriberSerializer(many = False)

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City

class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Publisher
	city = CitySerializer(many = False)
	profit = serializers.SerializerMethodField('get_profit')
	def get_profit(self, obj):
		queryset = Journal.objects.filter(publisher = obj)
		def summer(s,j):
			return s + j.price * j.number
		return reduce(summer, queryset, 0)

class JournalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Journal
	publisher = PublisherSerializer(many = False)

class JournalWithSubscribtionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Journal
	publisher = PublisherSerializer(many = False)
	subscribtions = serializers.SerializerMethodField('get_subscriptions')
	def get_subscriptions(self, obj): 
		queryset = Subscribtion.objects.filter(journal = obj)
		return SubscribtionSerializer(queryset, many = True).data

def assamble(pubs):
	res = {}
	for pub in pubs:
		if pub['city']['city'] not in res.keys():
			res[pub['city']['city']] = []
		res[pub['city']['city']].append(pub)
	return res

class JournalViewSet (viewsets.ModelViewSet):
	model = Journal
	def list(self, request):
		order_by = request.GET.get('orderby', 'index')
		like = request.GET.get('like', None)
		queryset = Journal.objects
		if like:
			queryset = queryset.filter(name__regex = like)
		else:
			queryset = queryset.all()
		queryset = queryset.order_by(order_by)
		serializer = JournalSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Journal.objects.all()
		journal = get_object_or_404(queryset, pk=pk)
		serializer = JournalWithSubscribtionsSerializer(journal)
		return Response(serializer.data)

	serializer_class = JournalSerializer

class PublisherViewSet (viewsets.ModelViewSet):
	def list(self, request):
		order_by = request.GET.get('orderby', 'name')
		queryset = Publisher.objects.all()
		queryset = queryset.order_by(order_by)
		serializer = PublisherSerializer(queryset, many=True)
		if request.GET.get('by_city', 'false').lower() == 'true':
			return Response(assamble(serializer.data))
		else:
			return Response(serializer.data)

	def update(self, request, pk):
		plus = request.DATA.get('price_plus', 0.0)
		try:
			plus = float(plus)
		except:
			plus = 0.0
		pub = get_object_or_404(Publisher.objects.all(), pk=pk)
		queryset = Journal.objects.filter(publisher = pub)
		for x in queryset:
			x.price += plus
			x.save()
		return Response("ok")


	queryset = Publisher.objects.all()
	serializer_class = PublisherSerializer

class SubscriberViewSet (viewsets.ModelViewSet):
	queryset = Subscriber.objects.all()
	serializer_class = SubscriberSerializer

class CityViewSet (viewsets.ModelViewSet):
	queryset = City.objects.all()
	serializer_class = CitySerializer