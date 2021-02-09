from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Meme
from .serializers import MemeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.authentication import *
from .forms import *


class ListMeme(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        req_memes=100
        endp=min(len(Meme.objects.all()),req_memes)
        memes=Meme.objects.all().order_by('-id')[:endp]
        serializer = MemeSerializer(memes, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = MemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            js = {
                'id': str(serializer.data['id'])
            }
            return Response(js, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class DetailMeme(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)

    def get_object(self, pk):
        try:
            return Meme.objects.get(pk=pk)
        except Meme.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        meme = self.get_object(pk)
        serializer = MemeSerializer(meme)
        return Response(serializer.data)

    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)
        serializer = MemeSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            js = {
                'id': str(serializer.data['id'])
            }
            return Response(js, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DetailMeme(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Meme.objects.all()
#     serializer_class = MemeSerializer
#     permission_classes = (AllowAny,)

