from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            image=validated_data['image'],
            phone_no=validated_data['phone_no']
          )

        user.set_password(validated_data['password'])
        user.save()

        return user    

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password',)
        extra_kwargs = {'password': {'write_only': True}}    

    #def save(self, **kwargs):
        
class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_no', 'image')     
        #extra_kwargs = {'password': {'read_only': True}}    



        
