from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import *
from .models import *


# Create your views here.


class RegisterApiView(CreateAPIView):

    serializer_class=RegisterSerializer
    queryset=User.


    