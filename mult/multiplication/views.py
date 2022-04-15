from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status, generics

class multiplication(generics.GenericAPIView):

    def get(self, request):
        return Response(data={"message":"multiplication session"}, status=status.HTTP_200_OK)

    def post(self, request):
        num1 = request.POST['op1']
        num2 = request.POST['op2']
        
        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            answer = a*b
            return Response(answer, status=status.HTTP_200_OK)

        else: 
            answer = 'Need to be numbers'
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)


        


    
