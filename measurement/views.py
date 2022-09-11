from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from .models import Datchik, Temp
from .serializers import DatchikSerializer, MeasureSerializer
import datetime
import json


#
class DemoView(APIView):
    def get(self, request):
        datchiks = Datchik.objects.all()
        ser = DatchikSerializer(datchiks, many=True)
        return Response(ser.data)

    def post(self, request):
        print(request)
        print(request.query_params)
        n = request.query_params.get("name")
        desc = request.POST.get("description")
        # Datchik(name= str(n),discription= str(desc)).save()
        return Response({'st': 'post_ok', str(n): str(desc)})


class SensorsView(APIView):
    def get(self, request, pk):
        queryset = Datchik.objects.select_related().get(id= pk)
        ser = DatchikSerializer(queryset)
        return Response(ser.data)

    def patch(self, request, pk):
        disc = request.query_params.get("description")
        if str(disc) != "None":
            Datchik.objects.filter(id=pk).update(description=disc)
        else:
            print(disc)
        return Response({'patch_st': 'ok', 'description': str(disc)})


class MeasureView(APIView):
    def get(self, request):
        mesurements = Temp.objects.all()
        ser = MeasureSerializer(mesurements, many=True)
        return Response(ser.data)

    def post(self, request):
        print('sdfsdfs')
        print(request)
        params = json.loads(request.body.decode())
        print(params)
        s = int(params.get("sensor"))
        t = float(params.get("temperature"))
        Temp(sensor=Datchik.objects.all().filter(id=s)[0], temperature=t, created_at=datetime.datetime.now()).save()
        return Response({'st': 'post_ok', str(s): str(t)})

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
