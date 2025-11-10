"""
URL configuration for SmartWaste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from SmartWasteApp.views import *

urlpatterns = [
    path('', LoginPage.as_view(), name="LoginPage"),

    # ///////////////////////////////// ADMIN ///////////////////////////

    path('AddBin', AddBin.as_view(), name="AddBin"),
    path('ManageContractor', ManageContractor.as_view(), name="ManageContractor"),
    path('AcceptContractor/<int:lid>', AcceptContractor.as_view(), name="AcceptContractor"),
    path('RejectContractor/<int:lid>', RejectContractor.as_view(), name="RejectContractor"),
    path('MonitorBin', MonitorBin.as_view(), name="MonitorBin"),
    path('OverSeeReward', OverSeeReward.as_view(), name="OverSeeReward"),
    path('VerifyUser', VerifyUser.as_view(), name="VerifyUser"),
    path('AcceptUser/<int:lid>', AcceptUser.as_view(), name="AcceptUser"),
    path('RejectUser/<int:lid>', RejectUser.as_view(), name="RejectUser"),
    path('Complaints', Complaints.as_view(), name="Complaints"),
    path('ComplaintReply/<int:cid>', ComplaintReply.as_view(), name="ComplaintReply"),
    path('ViewBins',ViewBins.as_view(), name="ViewBins"),
    path('EditBin/<int:id>', EditBin.as_view(), name="EditBin"),
    path('DeleteBin/<int:id>', DeleteBin.as_view(), name="DeleteBin"),
    
    #/////////////////////////////CONTRACTOR/////////////////////////////

    path('Maintenence', Maintenence.as_view(), name="Maintenence"),
    path('BinStatus', Binstatus.as_view(), name="BinStatus"),
    path('Admindashboard',Admindashboard.as_view(),name='Admindashboard'),
    
    ]
