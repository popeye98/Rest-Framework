from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    name=serializers.CharField(required=False)  # so that while updating does not show this is required
    
    ranking=serializers.FloatField(required=False)
    employee_id=serializers.CharField(required=False)

    class Meta:
        model=Users
        #fields=('name','employee_id')
        fields='__all__'


