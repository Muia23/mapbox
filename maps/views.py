from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.views import APIView

# class GetRiskData(APIView):
#     def get(self,requestm format=None):


def index(request):
    
    context = {
        'title': "Mapbox Sample"
    }



    return render(request,'index.html', context)
