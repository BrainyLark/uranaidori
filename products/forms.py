from django import forms

class TaskForm(forms.Form):
    task = forms.ChoiceField(
        choices=[('', '-----choose training task-----'),
                 ('1', 'Regression Model'),
                 ('2', 'Classification Model')],
        label='Choose your task: ',
        widget=forms.Select(attrs={
            "onchange" : "handleSubmission(this, 'task')"
        })
    )
    level = forms.CharField(max_length=50, widget=forms.HiddenInput())

class CategoricalForm(TaskForm):
    algorithm = forms.ChoiceField(
        choices=[('', '-----choose classification algorithm-----'),
                 ('1', 'Logistic Regression (Binary)'),
                 ('2', 'Support Vector Machine (Gaussian Kernel)')],
        label='Choose your algorithm: ',
        widget=forms.Select(attrs={
            "onchange" : "handleSubmission(this, 'categorical_algorithm')"
        }),
        required=False
    )

class RegressionForm(TaskForm):
    algorithm = forms.ChoiceField(
        choices=[('', '-----choose regression algorithm-----'),
                 ('1', 'Linear Regression'),
                 ('2', 'Polynomial Regression')],
        label='Choose your algorithm: ',
        widget=forms.Select(attrs={
            "onchange" : "handleSubmission(this, 'regression_algorithm')"
        }),
        required=False
    )