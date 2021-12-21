from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ShortenerSerializer
from .models import Shortener


class ShortenerViewSet(viewsets.ModelViewSet):
    serializer_class = ShortenerSerializer
    queryset = Shortener.objects.all()
    lookup_field = 'short_url'

    def retrieve(self, request, short_url=None):
        queryset = Shortener.objects.all()
        shortener = get_object_or_404(queryset, short_url=short_url)

        shortener.times_followed += 1
        shortener.save()

        serializer = ShortenerSerializer(shortener)
        return Response(serializer.data)

    def list(self, request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        queryset = Shortener.objects.filter(owner=request.user).order_by('-created')
        serializer = ShortenerSerializer(queryset, many=True)
        return Response(serializer.data)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
