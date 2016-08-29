from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.response import Response


class CheckUserExistView(views.APIView):
    def post(self, request):
        data = request.data
        email = data.get('email', None)

        try:
            User.objects.get(email=email)
            u = User.objects.all()
            user_exist_status = True
        except User.DoesNotExist:
            user_exist_status = False

        return Response({'user_exist_status': user_exist_status})
