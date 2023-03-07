from django.shortcuts import render
from .models import Family, Animals

def animals_list(request):
    animals = Animals.objects.all().order_by('family__name','name')
    context = {'animals': animals}

    return render(request, 'animals.html', context)


def family_list(request):
    families = Family.objects.all()
    context = {'families': families}

    return render(request, 'families.html', context)

def animal(request, id:int):
    animal_specific = Animals.objects.get(id = id)
    context = {'animal': animal_specific}
    return render (request,'animal.html',context)

def family(request, id:int):
    family_specific = Family.objects.get(id = id)
    family_animals = family_specific.animals_set.all()
    count = family_animals.count()
    context = {'family': family_specific, 'animals': family_animals, 'count': count}
    return render (request,'family.html',context)

def animal_speed(request):
    animals = Animals.objects.all().filter(speed__gt = 30).order_by('speed')
    context = {'animals': animals}

    return render(request, 'animalspeed.html', context)