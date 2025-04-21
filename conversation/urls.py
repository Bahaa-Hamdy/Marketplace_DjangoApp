from django.urls import path

from . import views


urlpatterns = [
    path('inbox/new/<int:item_pk>/' , views.new_conversation , name='new'),
    path('inbox/' , views.inbox , name='inbox'),
    path('inbox/<int:pk>/' , views.inboxdetail , name='inboxdetail'),
]