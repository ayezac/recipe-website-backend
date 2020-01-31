from .models import Question, Choice, ContactForm
from .serializers import QuestionSerializer, ChoiceSerializer, ContactFormSerializer
from rest_framework import generics, views, status, response

# Create your views here.

class QuestionGeneric:
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionList(QuestionGeneric, generics.ListAPIView):
    pass

class QuestionDetail(QuestionGeneric, generics.RetrieveAPIView):
    pass

class QuestionVote(views.APIView):
    def post(self, request, *args, **kwargs):
        question_pk = kwargs.get('pk', None)
        questions = Question.objects.filter(pk=question_pk)
        payload = request.data
        if questions.exists():
            question = questions.first()
            choice_pk = payload.get('choice', None)
            possible_choices = question.choice_set.filter(pk=choice_pk)
            if possible_choices.exists():
                choice = possible_choices.first()
                choice.votes += 1
                choice.save() 
                return response.Response(status=status.HTTP_200_OK)
        return response.Response('Not a valid choice or question',status=status.HTTP_400_BAD_REQUEST)

class ContactFormGeneric:
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class ContactFormCreate(ContactFormGeneric, generics.ListCreateAPIView):
    pass


class ContactFormDetail(ContactFormGeneric, generics.RetrieveUpdateDestroyAPIView):
    pass

