from rest_framework import routers, serializers, viewsets
from .models import login , registration , Todo

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = [ 'email' , 'password']

class registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields = [ 'username' , 'email' , 'password']
    
    def create(self,validate_data):
        return registration.objects.create(**validate_data)

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title','details','date']
        