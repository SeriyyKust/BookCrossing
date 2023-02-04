from .models import Profile
from .serializers import ProfileGetSerializer, ProfileUpdateSerializer


class ManagerProfile:
    def __init__(self, pk):
        if pk is None:
            self.obj = Profile.objects.all()
            self.many = True
        else:
            self.obj = self.__get_or_none(Profile, pk=pk)
            self.many = False

    @staticmethod
    def __get_or_none(model, *args, **kwargs):
        try:
            return model.objects.get(*args, **kwargs)
        except model.DoesNotExist:
            return None

    def get_serializer_data(self):
        return ProfileGetSerializer(self.obj, many=self.many).data

    def has_object(self):
        if self.many:
            return False if self.obj.count() == 0 else True
        else:
            return False if self.obj is None else True

    def update(self, new_data):
        if self.has_object():
            serializer = ProfileUpdateSerializer(instance=self.obj, data=new_data)
            if serializer.is_valid():
                serializer.save()
                return serializer.data | {"status": True}
            else:
                return serializer.errors | {"status": False}
        else:
            return None
