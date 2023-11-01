from .models import Advocate
from rest_framework.serializers import ModelSerializer

class AdvocateSeriazer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'