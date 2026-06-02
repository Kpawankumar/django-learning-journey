from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name' : 'pawan','age':20},
        {'name' : 'kaushal','age':25},
        {'name' : 'pankaj','age':28},
        {'name' : 'aadesh','age':20},
        {'name' : 'jain','age':80}
    ]
    Text = """Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum adipisci, quod maxime recusandae esse autem culpa quis iste facere, quas beatae a nulla! Ducimus numquam praesentium laborum nihil ex illo."""

    return render(request, "index.html",context={'peoples':peoples,'Text':Text})

def contact(request):
    return render(request, "contact.html" )

def about(request):
    return render(request, "about.html" )
def second(request):
    return HttpResponse("""<h1>this is a second route</h1>
                        <p>this is a demo page</p>
                        <hr>
                        <h3 style="color:red">this is h3 heading</h3>""")

