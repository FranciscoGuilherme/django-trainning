from rest_framework import serializers
from core.models import Atom

class AtomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atom
        fields = (
            'term',
            'createdAt',
            'deletedAt'
        )
