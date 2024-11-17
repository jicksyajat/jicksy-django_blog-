from django.shortcuts import render
from .models import *

# Create your views here.
def base(request):
    return render(request,'base.html')


def home(request):
    return render(request,'home.html')


from .forms import usercreationform
# user cration using form
def usercreation(request):
    if request.method =="POST":
        form =usercreationform(request.POST)
        if form.is_valid():
            form.save()
    form=usercreationform()
    dict_form ={
            'form':form
    }
    return render(request,'usercreation.html',dict_form)



# list all data using listview
from django.views.generic import ListView
class tasklistview(ListView):
    model=PostModel
    template_name='listtemplate.html'
    context_object_name='post'
    ordering = ['-pdate']



# detailed view using detailview
from django.views.generic.detail import DetailView
class taskDetailstview(DetailView):
    model=PostModel
    template_name='detailsview.html'
    context_object_name='post'    



# create new page using create view
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model=PostModel
    template_name='createview.html'
    fields='__all__'
    success_url=reverse_lazy('homeblog')
    # form_class=usercreationform
    def form_valid(self, form):        
        return super().form_valid(form)



# edit existing page using updateview
from django.views.generic.edit import UpdateView,DeleteView
class TaskUpdateView(UpdateView):
    model=PostModel
    template_name='UpdateView.html'
    fields='__all__'
    context_object_name='post'

    def get_success_url(self):
        return reverse_lazy('homeblog')


# detete a post using delete view
class TaskDeleteView(DeleteView):
    model=PostModel
    template_name='DeleteView.html'
    success_url=reverse_lazy('homeblog')
    context_object_name='post'

