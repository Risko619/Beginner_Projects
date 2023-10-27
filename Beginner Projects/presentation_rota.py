""" This program randomly selects students to share something every week"""

# random is a module that performs random selections
# choice is a function in the random module that randomly selects a value from a list.
from random import choice
# multimode is a function in the statistics module, which will find out which student appears most frequently in the rota.
from statistics import multimode

rota = []
students = ["Norm", "Gina", "Michael", "Jacob", "Rosa", "Raymond", "Terence", "Amy", "Charles", "Kevin"]

# This is a 20-week program, so we run it 20 times
for i in range(20):
  selected = choice(students)
  rota.append(selected)
  print(f'For week {i+1}, {selected} has been selected to share a reflection.')

# Here we find out who will be doing the most number of presentations
most_frequent_presenter = multimode(rota)

# Here we announce who'll be presenting most often, whether several or 1 person.
if len(most_frequent_presenter) > 1:
  print(f"The people we'll be hearing the most from are {most_frequent_presenter}.")
else:
  print(f"The person we'll be hearing the most from is {most_frequent_presenter[0]}.")


# Additional Tasks

''' 
check who shared the least.
try using other functions from modules imported.
'''