from rest_framework import serializers
from .models import Answer, Question, Survey


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'survey',
            'text',
            'type',
        )


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = (
            'id',
            'title',
            'end_date',
            'questions',
            'description',
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id'
            'user_id',
            'question',
            'answer_text',
        )
