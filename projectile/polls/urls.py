from django.urls import path, include
from polls.views import QuestionList, QuestionDetail, QuestionVote, ContactFormCreate, ContactFormDetail


urlpatterns = [
    path(
        'questions/', 
    QuestionList.as_view(), 
    name='question_list'
    ),

    path(
        'questions/<int:pk>/', 
    QuestionDetail.as_view(), 
    name='question_detail'
    ),

    path(
        'questions/<int:pk>/vote',
    QuestionVote.as_view(),
    name='question_vote'
    ),

    path(
        'contact/', 
    ContactFormCreate.as_view(), 
    name='create_contact_details'),

    path(
        'contact/<int:pk>/', 
        ContactFormDetail.as_view(),
        name='contact_details'
    ),
]