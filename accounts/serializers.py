from django.contrib.auth.models import User
from rest_framework import serializers, validators
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 10,
                },
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "Email Already Exits"
                    )
                ]
            }
        }

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists!")
        return value
