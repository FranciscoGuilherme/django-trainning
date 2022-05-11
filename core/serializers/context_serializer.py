from rest_framework import serializers
from core.models import Context

class ContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Context
        fields = (
            'description',
            'action_id',
            'knowledge_id',
            'createdAt',
            'deletedAt'
        )
