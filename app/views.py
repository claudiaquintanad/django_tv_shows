from app.models import Show
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return redirect("/shows")

def all_shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)
    
def render_add (request):
    return render(request, 'add_show.html')

def addshow(request):
    agregar_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['date'],
        description = request.POST['des'],
    )
    return redirect(f"/shows/{agregar_show.id}")

def editshow(request, val):
    variable = {
        'programa': Show.objects.get(id=val)
    }
    return render(request, 'edit.html', variable)

def edit(request):
    print(request.POST)
    edtitle = request.POST['ed_title']
    ednetwork = request.POST['ed_network']
    edrelease_date = request.POST['ed_date']
    eddescription = request.POST['ed_des']
    id_programa = request.POST['id_show']
    programa2 = Show.objects.get(id= id_programa)
    programa2.title = edtitle
    programa2.network = ednetwork
    programa2.release_date = edrelease_date
    programa2.description = eddescription
    programa2.save()
    return redirect("/shows")

def oneshow(request, val):
    variable = {
        'programa': Show.objects.get(id=val)
    }
    return render(request, 'one_show.html', variable)

def delete(request, val):
    delete_show = Show.objects.get(id=val)
    delete_show.delete()
    return redirect("/shows")