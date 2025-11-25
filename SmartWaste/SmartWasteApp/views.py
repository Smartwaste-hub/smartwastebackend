from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from SmartWasteApp.serializer import *
from SmartWasteApp.forms import BinForm
from SmartWasteApp.models import *

# Create your views here.
class Admindashboard(View):
    def get(self,request):
        return render(request,'administration/admin_home.html')

class LoginPage(View):
    def get(self, request):
        return render(request, "administration/login.html")
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            obj = LoginTable.objects.get(Username=username, Password=password)
            request.session['user_id'] = obj.id
            if obj.UserType =='Admin':
                return HttpResponse('''<script>alert('Login successful');window.location='/Admindashboard '</script>''')
            elif obj.UserType == 'Contractor':
                return HttpResponse('''<script>alert('Login successful');window.location='/Contractorhome/ '</script>''')
        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert('Invalid username or password');window.location='/'</script>''')
    
    
# ////////////////////////////// ADMIN ///////////////////////////////////////////
    

class AddBin(View):
    def get(self, request):
        return render(request, "administration/addbin.html") 
    def post(self,request):
        form=BinForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert('Bin added Succesfully');window.location='/Admindashboard'</script>''')
    
class ManageContractor(View):
    def get(self, request):
        obj = ContractorTable.objects.all()
        return render(request, "administration/managecontractor.html", {'val': obj})
    
class AcceptContractor(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.UserType="contractor"
        obj.save()
        return HttpResponse('''<script>alert('Accepted Succesfully');window.location='/ManageContractor'</script>''')

class RejectContractor(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.UserType="Rejected"
        obj.save()
        return HttpResponse('''<script>alert('Rejected Succesfully');window.location='/ManageContractor'</script>''')


class MonitorBin(View):
    def get(self, request):
        return render(request, "administration/monitorbin.html")
class OverSeeReward(View):
    def get(self, request):
        return render(request, "administration/managecontractor.html") 
     
class VerifyUser(View):
    def get(self, request):
        obj = StudentTable.objects.all()
        return render(request, "administration/verifyuser.html",{'val':obj})  

class AcceptUser(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.UserType="Student"
        obj.save()
        return HttpResponse('''<script>alert('Accepted Succesfully');window.location='/VerifyUser'</script>''')
  
class RejectUser(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.UserType="Rejected"
        obj.save()
        return HttpResponse('''<script>alert('Rejected Succesfully');window.location='/VerifyUser'</script>''')

    
class Complaints(View):
    def get(self, request):
        obj = ComplaintTable.objects.all()
        return render(request, "administration/viewcomplaint&sendreply.html", {'val': obj}) 
    
class ComplaintReply(View):
    def post(self, request, cid):
        obj = ComplaintTable.objects.get(id=cid)
        obj.Reply = request.POST['reply']
        obj.save()
        return HttpResponse('''<script>alert('Succesfully');window.location='/Complaints'</script>''')
    
class ViewBins(View):
    def get(self,request):
        obj=BinTable.objects.all()
        return render(request, "administration/ViewBins.html", {'val': obj})
    

class EditBin(View):
    def get( self,request,id):
        obj=BinTable.objects.get(id=id)
        return render(request, "administration/EditBin.html",{'val':obj})
    def post(self,request,id):
        bin=BinTable.objects.get(id=id)
        bin.BinPlace=request.POST['BinPlace']
        bin.save()
        return HttpResponse('''<script>alert(" Updated Successfully!");window.location="/ViewBins";</script>''')
class DeleteBin(View):
    def get(self,request,id):
        bin=BinTable.objects.get(id=id)   
        bin.delete()
        return HttpResponse('''<script>alert(" Deleted Successfully!");window.location="/ViewBins";</script>''')

        
    
    #////////////////////////CONTRACTOR////////////////////////////
class Maintenence(View):
    def get(self, request):
        return render(request, "CONTRACTOR/maintenence.html")     
       
class Binstatus(View):
    def get(self, request):
        bin=BinTable.objects.all()
        # obj=BinTable.objects.all()
        return render(request, "CONTRACTOR/viewbinstatus.html",{'val':bin}) 
    


# //////////////////////////////API///////////////////


class loginPage_api(APIView):
    def post(self,request):
        response_dict={}

        #get data from the request
        username = request.data.get("Username")
        password = request.data.get("Password")

        #validate input
        if not username or not password:
            response_dict["message"]="Failed"
            return Response(response_dict,status=status.HTTP_400_BAD_REQUEST)
        
        #fetch the user from LoginTable
        t_user = LoginTable.objects.filter(Username=username, Password=password).first()

        if not t_user:
            response_dict["message"]="Failed"
            return Response(response_dict,status=status.HTTP_401_UNAUTHORIZED)
        else:
            response_dict["message"]="success"
            response_dict["login_id"]=t_user.id
            response_dict["UserType"]=t_user.UserType

            return Response(response_dict,status=status.HTTP_200_OK)
        


class ViewRewardAPI(APIView):   
    def get(self,request):
        c=RewardTable.object.all()
        serializer=RewardSerializer(c, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class SendComplaintAPI(APIView):
    def post(self,request,id):
        guardian = LoginTable.objects.get(LOGIN__id=id)
        serializer=ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(guardian=guardian)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, id):
        guardian = StudentTable.objects.get(guardian__id=id)
        Complaints=ComplaintTable.objects.filter(guardian=guardian)
        serializer=ComplaintSerializer(Complaints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    

class StudentRegAPIView(APIView):
     def post(self,request):
         print('==================',request.data)
         reg_serial=StudentSerializer(data=request.data)
         login_serial=LoginSerializer(data=request.data)

         regvalid=reg_serial.is_valid()
         loginvalid=login_serial.is_valid()

         if regvalid and loginvalid:
             login=login_serial.save(UserType='Student')
             reg_serial.save(LOGIN=login)
             return Response({'message':'Registration successful'},status=status.HTTP_200_OK)
         else:
             return Response({'Registration error': reg_serial.errors if not regvalid else None,
                              'login error': login_serial.errors if not loginvalid else None}, status=status.HTTP_400_BAD_REQUEST)
         
 
         