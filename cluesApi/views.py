from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Card, LatestVersion



class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestVersion
        fields = "__all__"


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


@api_view(["GET"])
def cardView(request):

    if request.method == "GET":
        cards = Card.objects.all()
        serializer = CardsSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    resObj = {"badRequest": "bad request"}
    return Response(resObj, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def latestVersion(request, clientVersion):
    if request.method == "GET":
        latestVersion = LatestVersion.objects.all().order_by('-timeStamp')[0]
        message = "you have the lastest cards" if clientVersion == latestVersion.version else "you don't have the lastest cards"
        isLatest = True if clientVersion == latestVersion.version else False
        serializer = VersionSerializer(latestVersion)
        latestVersionInt = int(str(latestVersion).split(" ")[-1])

        resObj = {
            "message": message,
            "isLatest": isLatest,
            "latestVersion": latestVersionInt
        }
        return Response(resObj, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
