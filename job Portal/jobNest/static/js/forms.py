# for custom forms > [eita lagbe na]
from django import forms
class NameForm(forms.Form):
    # ekdom model er moto, just null true, auto_now egulo lagbe na and forms. hobe, model na
    # must be level diye diba, html a jemn kore html page a <label for="status">Status</label> dita

    name = forms.CharField(label="Your name", max_length=100)
    age = forms.IntegerField(label="Your name")

# for model forms > [eita lagbe]
from django import forms
from .models import YourModel # Replace YourModelName with your actual model
    class YourModelForm(forms.ModelForm):
        class Meta:
            model = YourModel
            fields = ['name', 'age', 'userType', 'email'] # Model theke > 'create at, foren key newa jabe na'

## views.py
from django.shortcuts import render, redirect
from .forms import YourModelForm

def create_your_model(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST)
        if form.is_valid():
            form.save() # Saves the data to the database
            return redirect('success_url') # Redirect after successful submission
    return render(request, 'your_template.html', {'form': form})

## addPageInHTML.html
<form method="POST">
    {% csrf_token %}
    {{ form }} # or form.as_table, form.as_ul, or render fields individually

    # form: For full form
    # form.as_p: Render as paragraphs
    # form.as_table: Render as a table
    # form.as_ul: Render as an unordered list

    <button type="submit">Submit</button>
</form>