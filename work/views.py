from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Work
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.db.models import Q
# Create your views here.
class listview(ListView):
    model = Work
    template_name = 'home.html'
    context_object_name = 'works'
class detailview(DetailView):
    model = Work
    template_name = 'detail.html'
    context_object_name = 'works'

# def home(request):
#     return render(request, 'home.html',{})

class createview(CreateView):
    model = Work
    template_name = 'add_work.html'
    fields = ['title']
    success_url = '/'
class updateview(UpdateView):
    model = Work
    template_name = 'edit.html'
    fields = ['title']
    context_object_name = 'works'
    success_url = '/'
    def valid_form():
        instance = form.save()
        return redirect('detail',instance.pk)

class deleteview(DeleteView):
    model = Work
    template_name = 'delete.html'
    success_url='/'   

def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        result = Work.objects.filter(Q(title__icontains=search_term))
        context = {'search_term':search_term,'results':result}
        return render(request,'search.html',context)
    else:
        return redirect('listview')

