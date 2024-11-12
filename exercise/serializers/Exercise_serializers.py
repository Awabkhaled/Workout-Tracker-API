from rest_framework import serializers
from exercise.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for the Exercise model enpoints"""
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'user']
        read_only_fields = ['id', 'user']

    def validate_name(self, value):
        """Validate that the exercise name is unique for the user"""
        user = self.context['request'].user
        exercise_id = self.instance.id if self.instance else None

        # Check for duplicates, excluding the current instance
        if Exercise.objects.filter_CI(name=value, user=user
                                      ).exclude(pk=exercise_id).exists():
            raise serializers.ValidationError(
                f"An exercise with the name '{value}' already exists.")

        return value

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        exercise = Exercise.objects.create(**validated_data)
        return exercise

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ExerciseListSerializer(serializers.ModelSerializer):
    """Serializer for the Exercise model list enpoint"""
    class Meta:
        model = Exercise
        fields = ['id', 'name']
        read_only_fields = ['id']