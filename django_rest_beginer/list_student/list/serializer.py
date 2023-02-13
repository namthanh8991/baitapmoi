from rest_framework import serializers
from rest_framework.response import Response
from .models import student

class studentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    address = serializers.CharField(max_length=200, required=True)
    roll_number = serializers.IntegerField()
    mobile = serializers.CharField(max_length=10, required=True)

    class Meta :
        model = student
        fields = ['first_name','last_name','address','mobile','roll_number']

    def create(self, validated_data):
        return student(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.mobile = validated_data.get('mobile', instance.mobile)

        instance.save()