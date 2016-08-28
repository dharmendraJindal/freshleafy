from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response

from authentication.models import UserProfile
from authentication.serializers.UserProfileSerializer import UserProfileSerializer
from authentication.serializers.UserSerializer import UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'email'
    serializer_class = UserSerializer
    user_profile_serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer = self.user_profile_serializer_class(user_profile)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data

        print data

        try:
            email = data.get('email', None)
            password = data.get('password', None)
        except:
            email = None
            password = None

        if data:
            first_name = data.get('first_name', None)
            last_name = data.get('last_name', None)
            user = User.objects.create_user(email=email, username=email, password=password,
                                            first_name=first_name, last_name=last_name)

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

            data['username'] = email

            return Response(data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
