from django.db import models
import random

class FirstName(models.Model):
  name = models.CharField(max_length=25)
  def __str__ (self):
    return self.name

class SecondName(models.Model):
  name = models.CharField(max_length=25)
  def __str__ (self):
    return self.name

class FullName(models.Model):
  dj_name = models.CharField(max_length=51, default="")
  first_name = models.ForeignKey(FirstName, on_delete=models.CASCADE)
  second_name = models.ForeignKey(SecondName, on_delete=models.CASCADE)

  def create_dj_name(self, mod1=FirstName, mod2=SecondName):
    first_names = list(mod1.objects.all())
    random_first_names = random.sample(first_names, 1)
    selected_first_name = random.choice(random_first_names)
    self.first_name = selected_first_name

    second_names = list(mod2.objects.all())
    random_second_names = random.sample(second_names, 1)
    selected_second_name = random.choice(random_second_names)
    self.second_name = selected_second_name
    
    self.dj_name = self.first_name.name + " " + self.second_name.name
    return self.dj_name

  def __str__ (self):
    return self.dj_name

  # Could check for dups in a `save` method
  def save_unique (self):
    existing = FullName.objects.filter(first_name=self.first_name, second_name=self.second_name)
    if not existing:
      print(self.dj_name + " is saved.")
      self.save() 
    else:
      print("Looks like that names taken already. Try again.")

  # Maybe extra
  def similar_names(self):
    names_list = list(FullName.objects.filter(first_name=self.first_name))
    names_list.extend(list(FullName.objects.filter(second_name=self.second_name)))
    return names_list

