from .models import Post, Review
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class PostSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = Post
        geo_field = "geom"
        fields = ('title', 'content', 'created_at', 'updated_at')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
