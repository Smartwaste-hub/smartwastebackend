from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

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
    
