from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView,UpdateView, DeleteView

from .models import Finch,Insurance

from .forms import InsuranceForm

# Add this finch list below the imports
"""
finches = [
   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
 ]
 """


# Create your views here.

#CLASS BASED VIEWS

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
 # fields = ['name', 'type', 'description']
  #success_url = '/finches/{finch_id}'
  success_url = '/finches'


class FinchUpdate(UpdateView):
  model = Finch
 
  fields = ['type', 'description']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'



# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
   
   finches=Finch.objects.all()
   
   return render(request,'finches/index.html', {'finches':finches})



def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)

  insurance_form = InsuranceForm()

  return render(request, 'finches/detail.html', { 'finch': finch, 'insurance_form':insurance_form })





def add_insurance(request, finch_id):
  
 form = InsuranceForm(request.POST)
 if form.is_valid():
  new_insurance = form.save(commit=False)
  new_insurance.finch_id = finch_id
  new_insurance.save()
  return redirect('detail', finch_id=finch_id)




   
