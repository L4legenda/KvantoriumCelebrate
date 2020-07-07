from rest_framework import serializers
from userlist.models import Children

class ChildDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = "__all__"