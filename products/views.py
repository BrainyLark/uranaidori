from django.shortcuts import render
from django.http import HttpResponse
from .forms import TaskForm, CategoricalForm, RegressionForm

def index(request):

    if request.method == 'POST':

        level = request.POST['level']

        if level == 'task':
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task = task_form.cleaned_data['task']
                if task == '1':
                    form = RegressionForm(request.POST)
                elif task == '2':
                    form = CategoricalForm(request.POST)
                else:
                    form = TaskForm()
            
        elif level in ['regression_algorithm', 'categorical_algorithm']:
            
            if level == 'regression_algorithm':
                algorithm_form = RegressionForm(request.POST)    
            else:
                algorithm_form = CategoricalForm(request.POST)
            
            if algorithm_form.is_valid():
                return HttpResponse("You have chosen algorithm: " + algorithm_form.cleaned_data['algorithm'])
            
    else:
        form = TaskForm()

    return render(request, 'products/index.html', {'form' : form})