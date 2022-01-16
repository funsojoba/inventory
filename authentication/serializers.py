from rest_framework import serializers

from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('fullname', 'email', 'role')
        
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.PasswordField()
    is_new_user = serializers.BooleanField(default=False, required=False)