from rest_framework import serializers
from . models import BusinessRule

class BusinessRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessRule
        fields = ('tags', 'information')
