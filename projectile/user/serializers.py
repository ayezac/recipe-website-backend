from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "password", "email", "first_name", "last_name")
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validiated_data):
        user = User(**validiated_data)
        user.set_password(validiated_data['password'])
        user.save()
        return user