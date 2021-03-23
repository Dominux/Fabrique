from rest_framework.response import Response
from surveys.serializers import AnswerSerializer, SurveySerializer
from surveys.models import Answer, Survey
from rest_framework import viewsets
from rest_framework.decorators import action


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.active()
    serializer_class = SurveySerializer


class AnswerViewSet(SurveySerializer):
    def create(self, request, *args, **kwargs):
        for answer in request.body.get('answer'):
            serializer = AnswerSerializer(data=answer)
            
            Answer.objects.create(
                user_id=serializer.validated_data['user_id'],
                question=serializer.validated_data['question'],
                answer_text=serializer.validated_data['answer_text'],
            )

        return Response("Successfully", status=201)

    def list(self, request, *args, **kwargs):
        user_id = request.data.get("id")

        answers = Answer.objects.filter(user_id=user_id)
        return AnswerSerializer(data=answers)
