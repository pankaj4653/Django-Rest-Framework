from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def index(request):
	if request.method == "POST":
	    return Response(data = {"message":"Got Some Data!","Data": request.data} ,status =status.HTTP_200_OK)
	elif(request.method == "GET"):
		return Response(data = {"message" : "This is by Get method"},status = status.HTTP_200_OK)
	else:
		return Response({"message" : "This is Not the Right Method" })

