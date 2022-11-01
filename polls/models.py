from dis import Instruction
from django.db import models

class Recipe(models.Model):
  name = models.CharField(max_length=200)
  ingredient1 = models.TextField(default='')
  ingredient2 = models.TextField(default='')
  ingredient3 = models.TextField(default='')
  ingredient4 = models.TextField(default='')
  ingredient5 = models.TextField(default='')
  ingredient6 = models.TextField(default='')
  instruction = models.TextField(default='')
  def __str__(self):
        return self.name