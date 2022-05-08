from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import BusinessRule
from . serializers import BusinessRuleSerializer

class BusinessList(APIView):
    def get(self, request):
        businessRule = BusinessRule.objects.all()
        serializer = BusinessRuleSerializer(businessRule, many = True)

        return Response(serializer.data)

    def post(self):
        pass
