from rest_framework import serializers
from emp.models import Emp_Info

class Emp_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Emp_Info
        fields='__all__'