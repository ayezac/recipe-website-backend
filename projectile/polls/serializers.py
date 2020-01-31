from .models import Question, Choice, ContactForm
from rest_framework import serializers

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id','choice_text', 'votes']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True)
    class Meta:
        model = Question
        fields = ['id','question_text', 'pub_date', 'choices']

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['id', 'name', 'email', 'country', 'message', 'get_newsletter']


