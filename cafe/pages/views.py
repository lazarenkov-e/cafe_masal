from django.shortcuts import render
from pages.models import Worker


def index_page(request):
    # Worker.objects.get(id=3).delete() [j[j]]
    all_workers = Worker.objects.all()
    for i in all_workers:
        print(i.name, i.lastname, i.salary, i.id)
    return render(request, 'index.html')
