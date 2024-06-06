from django.shortcuts import render
from django.http import HttpResponse

class State:
    def __init__(self, cmd: int, task: str, algorithm: str):
        self.last_cmd = cmd
        self.task = task
        self.algorithm = algorithm

# Create your views here.
def index(request):

    if request.method == 'POST':
        cmd = request.POST['cmd']
        if cmd == 'task_chosen':
            task: str = request.POST['task']
            state = State(cmd, task, None)

        elif cmd == 'algorithm_chosen':
            task: str = request.POST['task_chosen']
            algorithm: str = request.POST['algorithm']
            state = State(cmd, task, algorithm)

        else:
            state = State(0, None, None)

    else:
        state = State(0, None, None)

    return render(request, 'train/main.html', {'state': state})