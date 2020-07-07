from rest_framework import serializers
from usercelebrate.models import Celebrate

class CelebrateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrate
        fields = "__all__"