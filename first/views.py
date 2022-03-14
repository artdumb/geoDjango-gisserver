from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.core.serializers import serialize
from .models import Post, Review
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import ReviewSerializer, PostSerializer
from rest_framework import status
from django.http.response import HttpResponse
from django.views.decorators    .csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.gis.geos import GEOSGeometry
import json


# 리스트 조회 (get) api
@api_view(['GET'])
def listpostAPI(request):
    modelDB = Post.objects.all()
    # 다수의 데이터를 받고자 할때(many=true)
    serializers = PostSerializer(modelDB, many=True)
    return Response(serializers.data)


# Create your views here.
# 개별 게시물 조회, 게시물 추가 api
@method_decorator(csrf_exempt, name='dispatch')
class postAPI(APIView):
    # def get(self, request, id):
    #     obj = get_object_or_404(Post, pk=id)
    #     serializers = PostSerializer(obj)
    #     return Response(serializers.data)

    def post(self, request):
        data = json.loads(request.body)
        contentt = data['features'][0]['properties']['content']
        titlee = data['features'][0]['properties']['title']
        geom = data['features'][0]['geometry']
        pnt = GEOSGeometry(str(geom))
        # KEY_ERROR check
        if not (contentt):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        Post.objects.create(
            content=contentt,
            title=titlee,
            geom=pnt
        )

        return JsonResponse({'message': 'SUCCESS'}, status=200)
