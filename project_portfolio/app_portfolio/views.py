from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from .models import Project

def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.get('tags', '')
        tags_list = [tag.strip() for tag in tags.split(',')] if tags else []
        image = request.FILES.get('image')
        if image:
            project = Project(title=title, description=description, tags=tags_list, image=image)
        else:
            project = Project(title=title, description=description, tags=tags_list)
        
        project.save()

        return redirect('projects')  # redireciona para a lista de projetos após salvar

    return render(request, 'create_project.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('projects')