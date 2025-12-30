from rest_framework.serializers import ModelSerializer

from SmartWasteApp.models import *

class LoginSerializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['Username','Password','UserType']


class ContractorSerializer(ModelSerializer):
    class Meta:
        model=ContractorTable
        fields=['namem','address','email','dob','qualification','mobilenumber','gender','LOGIN']

class BinSerializer(ModelSerializer):
    class Meta:
        model=BinTable
        fields=['Binname','BinPlace','BinStatus','CollectionStatus','Date']

class StudentSerializer(ModelSerializer):
    class Meta:
        model=StudentTable
        fields=['name','age','address','department','mobilenumber','gender', 'email']

class RewardSerializer(ModelSerializer):
    class Meta:
        model=RewardTable
        fields=['STUDENT','BinId','Rewardpoint','Date']

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model=ComplaintTable
        fields=['STUDENT','Complaint','Date','Reply']


class ProductSerializer(ModelSerializer):
    class Meta:
        model=ProductTable
        fields=['ProductName','Point','Image','Description']

