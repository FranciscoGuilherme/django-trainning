from rest_framework import serializers
from core.models import Action

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = (
            'description',
            'atom_id',
            'axiom_id',
            'createdAt',
            'deletedAt'
        )
