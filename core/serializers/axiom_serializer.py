from rest_framework import serializers
from core.models import Axiom

class AxiomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axiom
        fields = (
            'valid',
            'sentence',
            'createdAt',
            'deletedAt'
        )
