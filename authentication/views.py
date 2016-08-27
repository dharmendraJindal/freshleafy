from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response

from authentication.models import UserProfile
from authentication.serializers import UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        data = request.data
        # serializer = self.serializer_class(data=request.data)

        print data, 'data'
        try:
            email = data.get('email', None)
            password = data.get('password', None)
        except:
            username = None
            email = None
            password = None

        if data:
            user = User.objects.create_user(email=email, username=email, password=password)

            # create user profile

            address_one = data.get('address_one', None)
            address_two = data.get('address_two', None)
            street = data.get('street', None)
            landmark = data.get('landmark', None)
            district = data.get('district', None)
            city = data.get('city', None)
            state = data.get('state', None)
            pincode = data.get('pincode', None)
            phonenumber = data.get('phonenumber', None)
            phonenumber_two = data.get('phonenumber_two', None)
            company = data.get('company', None)

            user_profile = UserProfile(user=user,
                                       address_one=address_one,
                                       address_two=address_two,
                                       street=street,
                                       landmark=landmark,
                                       district=district,
                                       city=city,
                                       state=state,
                                       pincode=pincode,
                                       phonenumber=phonenumber,
                                       phonenumber_two=phonenumber_two,
                                       company=company
                                       )
            user_profile.save()

            return Response(data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        account = authenticate(username=username, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = UserSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        logout(request)

        return Response({"you are logged out"}, status=status.HTTP_204_NO_CONTENT)
