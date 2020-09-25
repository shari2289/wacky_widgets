from django.shortcuts import render, redirect
from .models import Widget
from .widget_form import WidgetForm

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form})

def delete_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id).delete()
    return redirect('index')

def add_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('index')    