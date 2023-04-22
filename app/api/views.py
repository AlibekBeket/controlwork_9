from rest_framework.views import APIView
from rest_framework.response import Response

from gallery.models import Photo


class FavoriteAddView(APIView):
    def post(self, request, *args, **kwargs):
        user_add = self.request.user
        users = Photo.objects.filter(id=self.kwargs['pk']).first().favorite.all()
        for user in users:
            if user == user_add:
                return Response(status=200)
        object = Photo.objects.filter(id=self.kwargs['pk']).first()
        object.favorite = user_add
        return Response(status=204)


class FavoriteDeleteView(APIView):
    def post(self, request, *args, **kwargs):
        user_delete = self.request.user
        users = Photo.objects.filter(id=self.kwargs['pk']).first().favorite.all()
        for user in users:
            if user == user_delete:
                user.delete()
        else:
            Response(status=200)
        return Response(status=204)
