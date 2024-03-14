from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from core.page_filter import pages_filter
from .models import Order
from .serializers import OrderSerializer

# class OrderListView(APIView):
#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class OrderDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Order.objects.get(pk=pk)
#         except Order.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         order = self.get_object(pk)
#         if order:
#             serializer = OrderSerializer(order)
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk):
#         order = self.get_object(pk)
#         if order:
#             serializer = OrderSerializer(order, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk):
#         order = self.get_object(pk)
#         if order:
#             order.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(status=status.HTTP_404_NOT_FOUND)

class OrderAddView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"message": "User created succesfully", "success":True})
    

class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        if request.path.startswith('/order/visitors/pages/') or request.path.startswith('/order/visitors/pages'):
            return pages_filter(self, request, Order, *args, **kwargs)
        return super().list(request, *args, **kwargs)
    

class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Deleted successfully", "success":True})
    

class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()  # Güncellenecek nesnelerin sorgusu için kullanılır
    serializer_class = OrderSerializer  # Nesnelerin seri hale getirilmesi için kullanılır

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Kısmi güncellemeleri işlemek için kullanılır
        order_id = kwargs.get('pk')  # kwargs aracılığıyla sipariş id'sini alırız
        if order_id is None:
            return Response({"detail": "Order ID is missing in the request"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(id=order_id)  # Siparişi çeker
        except Order.DoesNotExist:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Gelen verileri temizle
        cleaned_data = {key: value for key, value in request.data.items() if value is not None}
        
        serializer = self.get_serializer(instance=order, data=cleaned_data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order updated successfully", "success": True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)