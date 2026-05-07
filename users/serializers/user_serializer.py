from rest_framework import serializers
from users.models import User

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','email','password','role']

    def validate_role(self, value):
        if value == 'ADMIN':
            raise serializers.ValidationError(
                "Admin registration is not allowed."
            )    
        return value
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)