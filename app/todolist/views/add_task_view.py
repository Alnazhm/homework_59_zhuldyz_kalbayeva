from todolist.models import Tasks
from django.views.generic import CreateView
from todolist.forms import TaskForm


class TaskAddView(CreateView):
    template_name = 'create_task.html'
    form_class = TaskForm
    model = Tasks