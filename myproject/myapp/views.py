from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'description', 'id']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a single item instance.
        """
        instance = self.get_object()
        instance.delete()  # Directly delete the item instance
        return Response(status=status.HTTP_204_NO_CONTENT)




# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     search_fields = ['name', 'description','id']


class BulkInsertView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Request data must be a list"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(data=data, many=True)
        if serializer.is_valid():
            # Collect all instances
            instances = [Item(**item) for item in serializer.validated_data]
            # Bulk create
            Item.objects.bulk_create(instances)
            return Response({"message": "Data inserted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
