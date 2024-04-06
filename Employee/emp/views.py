from django.shortcuts import render
from rest_framework import viewsets
from emp.models import Emp_Info
from emp.serializers import Emp_Info_Serializer


# Create your views here.
class EmpViewset(viewsets.ModelViewSet):
    queryset = Emp_Info.objects.all()
    serializer_class = Emp_Info_Serializer

    
