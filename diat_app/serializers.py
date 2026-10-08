from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields='__all__'

    password=serializers.CharField(write_only=True)


    def create(self, validated_data):

        data=User.objects.create_user(**validated_data)

        return data