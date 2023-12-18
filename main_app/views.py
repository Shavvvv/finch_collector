from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Finch,Insurance, Food

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
  fields = ['name', 'type', 'description']
 # fields = '__all__'
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

  id_list = finch.foods.all().values_list('id')
  # Now we can query for toys whose ids are not in the list using exclude
  foods_finch_doesnt_eat = Food.objects.exclude(id__in=id_list)

  insurance_form = InsuranceForm()

  return render(request, 'finches/detail.html', { 'finch': finch, 'insurance_form':insurance_form, 'foods': foods_finch_doesnt_eat })





def add_insurance(request, finch_id):
  
 form = InsuranceForm(request.POST)
 if form.is_valid():
  new_insurance = form.save(commit=False)
  new_insurance.finch_id = finch_id
  new_insurance.save()
  return redirect('detail', finch_id=finch_id)




   
def assoc_food(request, finch_id, food_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Finch.objects.get(id=finch_id).foods.add(food_id)
  return redirect('detail', finch_id=finch_id)


class FoodCreate(CreateView):
    model = Food
    fields = '__all__'


class FoodDetail(DetailView):
    model = Food


class FoodDelete(DeleteView):
    model = Food
    success_url = '/finches'
