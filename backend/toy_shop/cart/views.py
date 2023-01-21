from rest_framework import viewsets, status, authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from shop.models import Product
from .models import CartItem
from .serializers import CartItemSerializer
from users.views import auto_creations_of_users
from django.views.decorators.csrf import csrf_exempt


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return
        

class CartItemsViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all().order_by('id')
    serializer_class = CartItemSerializer
    http_method_names = ['get', 'post', 'delete']
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get_queryset(self):
        return self.request.user.items.all()

    def perform_create(self, serializer):
        user = self.request.user
        id_item = self.request.data['item']
        price = Product.objects.get(id=id_item).price
        name = Product.objects.get(id=id_item).name
        serializer.save(user=user, price=price, name=name)

    def list(self, request):
        if request.user.is_anonymous or not request.user.items.all():
            return Response(status=status.HTTP_200_OK, data='empty')   
        return super().list(self, request)     

    def create(self, request, *args, **kwargs):  
        ''' add item to cart '''
        auto_creations_of_users(request)

        added_item_id = int(request.data['item'])  
        check = self.check_added_product(request, added_item_id)
        if check:
            return Response(status=status.HTTP_200_OK, data='already added')

        return super().create(request, *args, **kwargs)     

    def check_added_product(self, request, added_item_id):
        all_items_user = request.user.items.all()
        return any(cart_items.item.id == added_item_id for 
                   cart_items in all_items_user)
