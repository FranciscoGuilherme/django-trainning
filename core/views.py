from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_list_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Knowledge
from core.serializers.knowledge_serializer import KnowledgeSerializer

class KnowledgeList(APIView):
    def get(self, request):
        knowledge = Knowledge.objects.all()
        serializer = KnowledgeSerializer(knowledge, many = True)

        return Response(serializer.data)

    def post(self):
        pass
