from django.contrib.auth import logout
from rest_framework import permissions, status, views
from rest_framework.response import Response


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        logout(request)

        return Response({"you are logged out"}, status=status.HTTP_204_NO_CONTENT)
