from django import forms
from .models import PostModel


class Dateinput(forms.DateInput):
    input_type= 'date'

class usercreationform(forms.ModelForm):
    class Meta:
        model=PostModel
        fields='__all__'

        widgets ={
            'booking_date': Dateinput(),
        }

        labels={
            'title' : "Title",
            'content' :"Content",
            'pdate' : "Publication  Date",
            'author':'Author'
        }




        