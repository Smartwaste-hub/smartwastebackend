from rest_framework.serializers import ModelSerializer

from SmartWasteApp.models import BinTable, ComplaintTable, ContractorTable, LoginTable, RewardTable, StudentTable    

class LoginSerializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['Username','Password','UserType']

class ContractorSerializer(ModelSerializer):
    class Meta:
        model=ContractorTable
        fields=['name','address','email','dob','qualification','mobilenumber','gender','LOGIN']

class BinSerializer(ModelSerializer):
    class Meta:
        model=BinTable
        fields=['Binname','BinPlace','BinStatus','CollectionStatus','Date']

class StudentSerializer(ModelSerializer):
    class Meta:
        model=StudentTable
        fields=['name','age','address','department','mobilenumber','gender','LOGIN']

class RewardSerializer(ModelSerializer):
    class Meta:
        model=RewardTable
        fields=['STUDENT','BinId','Rewardpoint','Date']

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model=ComplaintTable
        fields=['STUDENT','Complaint','Date','Reply']

