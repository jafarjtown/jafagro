from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item, Order
from .serializers import ItemSerializer, OrderSerializer
class ItemListView(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
    

class ListOrders(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        """
        orders = Order.objects.all()
        return Response(data)

@api_view(['GET', 'POST'])
def createOrder(request):
  if request.method == 'POST':
    #print(request.data)
    item_id = int(request.data.get('item_id'))
    name = request.data.get('name')
    quantity = request.data.get('quantity')
    phone = request.data.get('phone')
    address = request.data.get('address')
    print(item_id, name, quantity, phone, address)
    print('up')
    item = Item.objects.get(id=item_id)
    order = Order.objects.create(item=item, quantity=quantity, name=name, address=address, phone=phone)
    
    serializer = OrderSerializer(order)
    
    return Response(serializer.data)
  orders = Order.objects.all()
  serializer = OrderSerializer(orders, many=True)
  return Response(serializer.data)
    