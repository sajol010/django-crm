from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken

from core.my_response import success, error

from django.contrib.auth.models import User

# Create your views here.

class LoginPIView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        try:
            data = self.request.data
            if data['email'] is None:
                return error('Email is required')
            if data['password'] is None:
                return error('Password is required')

            userObj = User.objects.filter(email=data['email'])
            if not userObj.exists():
                 return error('User not found!')

            user = userObj.first()

            if not user.check_password(raw_password=data['password']):
                return error("Password not match!")

            refresh = RefreshToken.for_user(user)

            responseData = {
                'access_token': str(refresh.access_token),
                'refresh': str(refresh),
            }
            return success(responseData)
        except:
         raise Exception("Something wrong")
