from restaurants.models import Restaurant
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    RestaurantListSerializer,
    RestaurantDetailSerializer,
    RestaurantCreateUpdateSerializer,
    CreateSerializer,
)

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'


# Complete Me
class RestaurantCreateView(CreateAPIView):
     serializer_class = CreateSerializer
     def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RestaurantUpdateView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'


class RestaurantDeleteView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'