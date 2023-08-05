from rest_framework import serializers

class serializers_link(serializers.Serializer):
    pathname=serializers.CharField(max_length=250)
    class Meta:
        fields = ['pathname']


