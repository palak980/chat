from django import forms
from .models import *

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name','participants'] 

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content'] 