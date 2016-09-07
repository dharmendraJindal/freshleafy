from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from product.models.UserOrderSummary import UserOrderSummary
from product.serialisers.UserOrderSummarySerialiser import UserOrderSummarySerialiser


class UserOrderSummaryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = UserOrderSummary.objects.all()
    serializer_class = UserOrderSummarySerialiser

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.queryset.filter(user=user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)