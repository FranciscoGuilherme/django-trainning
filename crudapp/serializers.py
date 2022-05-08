from rest_framework import serializers
from . models import BusinessRule

class businessRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessRule
        fields = ('tags', 'information')
