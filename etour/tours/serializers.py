from rest_framework.serializers import ModelSerializer
from .models import Tour, Location


class TourSerializer(ModelSerializer):
    image = ModelSerializer(source='image')

    def get_image(self, obj):
        request = self.context['request']
        # if obj.image and obj.image.name.startswith("/static"):
        #     pass
        # else:
        path = '/static/%s' % obj.image.name

        return request.build_absolute_uri(path)

    class Meta:
        model = Tour
        fields = ["id", "name", "image", "created_date", "active", "price", "locations"]


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name", "active", "description", "created_date"]