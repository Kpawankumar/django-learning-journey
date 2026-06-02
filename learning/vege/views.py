# from django.shortcuts import render
# from .models import *

# # Create your views here.

# def receipes(request):
#     if request.method == "POST":
#         print(request.POST)
#         print(request.FILES)

#         data = request.POST
#         image = request.FILES.get("receipe_image") or ""

#         Receipe.objects.create(
#             receipe_name=data.get("receipe_name", ""),
#             receipe_description=data.get("receipe_description", ""),
#             receipe_image=image,
#         )

#     return render(request, "receipes.html")

from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def receipes(request):

    if request.method == "POST":

        print("POST:", request.POST)
        print("FILES:", request.FILES)

        data = request.POST

        # template uses `recipe_*` names (note spelling)
        receipe_image = request.FILES.get('recipe_image') or ""
        receipe_name = data.get('recipe_name', "") or ""
        receipe_description = data.get('recipe_description', "") or ""

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            )
        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()
    context={'receipes' : queryset}
    return render(request, 'receipes.html', context )