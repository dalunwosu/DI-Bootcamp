from django.shortcuts import render

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

func = lambda d: d['age']
def people_list(request):
    people.sort(key = func)
    context = {'people': people }
    return render (request, 'people.html', context)

def person_list (request, id: int):
    person = people[id - 1]
    context = {'person': person }
    return render (request, 'person.html', context)