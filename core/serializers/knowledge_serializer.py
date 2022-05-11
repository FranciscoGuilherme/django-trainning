from rest_framework import serializers
from core.models import Knowledge

class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = (
            'valid',
            'sentence',
            'createdAt',
            'deletedAt'
        )
