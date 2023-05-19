from django import forms

class CreateTask(forms.Form):
  title = forms.CharField(label="Title", max_length=200, widget= forms.TextInput(attrs={'class': 'input'}))
  description = forms.CharField(label="Description",widget=forms.Textarea(attrs={'class':'input'}))

class CreateProject(forms.Form):
  name = forms.CharField(label="Name", max_length=200, widget= forms.TextInput(attrs={'class': 'input'}))