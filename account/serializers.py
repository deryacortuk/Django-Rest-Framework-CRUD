from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(style ={'input_type':'password'},write_only =True)    
 
    password2 = serializers.CharField(style ={'input_type':'password'},write_only =True)    

    class Meta:
        model = User
        fields = ['username','email','password','password2']       
        
    def validate(self,attrs):
        email = attrs.get('email',' ')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return super().validate(attrs)


    def save(self):
        account =User(
            email =self.validated_data['email'],
            username =self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 =self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'passwords is not matched.'})
        account.set_password(password)
        account.save()

        return account
    
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style ={'input_type':'password'},write_only =True)
    
    class Meta:
        model = User
        fields = ['username','password']

   


