from io import BytesIO
from itertools import product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from SmartWasteApp.serializer import *
from SmartWasteApp.forms import BinForm, ProductForm
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
            elif obj.UserType == 'contractor':
                return HttpResponse('''<script>alert('Login successful');window.location='/contractorhome'</script>''')
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

class addproduct(View):
    def get(self, request):
        return render(request, "administration/addproduct.html")
    def post(self,request):
         form=ProductForm(request.POST, request.FILES)
         print(form)
         if form.is_valid():
            form.save()
         return HttpResponse('''<script>alert('Product added Succesfully');window.location='/Admindashboard'</script>''')

class ViewProduct(View):
    def get(self,request):
        obj=ProductTable.objects.all()
        return render(request, "administration/ViewProduct.html", {'val': obj})

class EditProduct(View):

    def get(self, request, id):
        obj = get_object_or_404(ProductTable, id=id)
        return render(request, "administration/EditProduct.html", {'val': obj})

    def post(self, request, id):
        product = get_object_or_404(ProductTable, id=id)

        product.ProductName = request.POST.get('ProductName')
        product.Point = request.POST.get('Point')
        product.Description = request.POST.get('Description')

        if 'Image' in request.FILES:
            product.Image = request.FILES['Image']

        product.save()

        return HttpResponse('''<script>alert("Updated Successfully!");  window.location="/ViewProduct";  </script>'''
        )
class DeleteProduct(View):
    def get(self,request,id):
        product=ProductTable.objects.get(id=id)   
        product.delete()
        return HttpResponse('''<script>alert(" Deleted Successfully!");window.location="/ViewProduct";</script>''')

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

class contractorhome(View):
    def get(self, request):
        return render(request, "CONTRACTOR/Contractor_home.html")     
    
class Maintenence(View):
    def get(self, request):
        bin=BinTable.objects.all()
        # obj=BinTable.objects.all()
        return render(request, "CONTRACTOR/maintenence.html",{'val':bin})      
       
class Binstatus(View):
    def get(self, request):
        bin=BinTable.objects.all()
        # obj=BinTable.objects.all()
        return render(request, "CONTRACTOR/viewbinstatus.html",{'val':bin}) 
    


# //////////////////////////////API///////////////////


class loginPage_api(APIView):
    def post(self,request):
        print('-----------------------------------', request.data)
        response_dict={}

        #get data from the request
        username = request.data.get("Username")
        print(username)
        password = request.data.get("Password")
        print(password)
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
    def get(self, request):
        rewards = RewardTable.objects.all()

        total_points = rewards.aggregate(
            total=Sum('RewardPoint')
        )['total'] or 0

        serializer = RewardSerializer(rewards, many=True)

        return Response({
            "rewards": serializer.data,
            "total_reward_points": total_points
        }, status=status.HTTP_200_OK)
    


class SendComplaintAPI(APIView):

    def post(self, request, id):
        try:
            # Get student using login id
            student = StudentTable.objects.get(LOGIN__id=id)

        except StudentTable.DoesNotExist:
            return Response(
                {"error": "Student with this login ID not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Serialize complaint data
        serializer = ComplaintSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(STUDENT=student)  # <-- correct foreign key
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        try:
            student = StudentTable.objects.get(LOGIN__id=id)

        except StudentTable.DoesNotExist:
            return Response(
                {"error": "Student with this login ID not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        complaints = ComplaintTable.objects.filter(STUDENT=student).order_by('-Date')
        serializer = ComplaintSerializer(complaints, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
    

class StudentRegAPIView(APIView):
    def post(self, request):
        reg_serial = StudentSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)

        if reg_serial.is_valid() and login_serial.is_valid():
            login = login_serial.save(UserType='Student')
            student = reg_serial.save(LOGIN=login)

            # 🔹 Generate QR code
        qr_data = (
    f"Student ID: {student.id}\n"
    f"Name: {student.name}\n"
    f"Age: {student.age}\n"
    f"Gender: {student.gender}\n"
    f"Department: {student.department}\n"
    f"Mobile: {student.mobilenumber}\n"
    f"Email: {student.email}\n"
    f"Address: {student.address}") 
        qr_img = qrcode.make(qr_data)

        buffer = BytesIO()
        qr_img.save(buffer, format='PNG')

        filename = f"student_{student.id}.png"
        student.Qr.save(filename, ContentFile(buffer.getvalue()), save=True)


        return Response(
                {"message": "Registration successful", "qr_code": student.Qr.url},
                status=status.HTTP_200_OK)
        
    
class viewprofile(APIView):
  def get( self,request ):
      userid=request.data.get('lid')
      profile=StudentTable.objects.filter(LOGIN_id=userid)
      serializer=StudentSerializer(profile, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
  def post(self, request):
      print(request.data)
      userid=request.data.get('lid')
      user = StudentTable.objects.get(LOGIN_id = userid)
      serializer=StudentSerializer(user, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)   


class ViewProductAPI(APIView):
    def get(self,request):
        c=ProductTable.objects.all()
        d=ProductSerializer(c, many=True)
        return Response(d.data, status=status.HTTP_200_OK)



  
   

      
             