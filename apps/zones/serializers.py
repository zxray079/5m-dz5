from rest_framework import serializers

from .models import Zone, Visitors


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

    def validate_latitude(self, value):
        if value < -90 or value > 90:
            raise serializers.ValidationError(
                'Широта должна быть от -90 до 90.'
            )
        return value

    def validate_longitude(self, value):
        if value < -180 or value > 180:
            raise serializers.ValidationError(
                'Долгота должна быть от -180 до 180.'
            )


class VisitorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = '__all__'

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                'Имя должно содержать минимум 2 символа.'
            )
        return value