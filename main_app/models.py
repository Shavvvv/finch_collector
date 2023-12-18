from django.db import models
from django.urls import reverse

# Create your models here.


class Food(models.Model):
    item = models.CharField(max_length=50)
    foodgroup = models.CharField(max_length=20)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('foods_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    # models.CharField are called field types if you want to google others
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    foods = models.ManyToManyField(Food)

    def __str__(self):
        return self.name
    
      # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    

COMPANIES=(
         ('G', 'Geico Pets'),
    ('E', 'Eagle Eye'),
    ('P', 'Pettigree insurance')
    )
    


class Insurance(models.Model):
  date  = models.DateField()
  company = models.CharField(
      max_length=1,
      choices=COMPANIES,
      default=COMPANIES[0][0])
  
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_company_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']