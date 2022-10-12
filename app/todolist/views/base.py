from todolist.models import Tasks
from django.views.generic import ListView

class IndexView(ListView):
    template_name = 'index.html'
    model = Tasks
    context_object_name = 'todo_tasks'











