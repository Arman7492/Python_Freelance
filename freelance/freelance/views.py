from typing import Any
from django.views.generic import ListView, DetailView, TemplateView
from .models import Service, Order, Executor, Customer


class MainPageView(TemplateView):
    template_name = 'basic/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['message'] = 'Это главная страница проекта'
        return context
    
class ExecutorListView(ListView):
    model = Executor
    template_name = (
        'freelance/executor_list.html'
    )
    content_object_name = 'executors' #Укажите ваш путь к шаблону

class ExecutorDetailView(DetailView):
    model = Executor
    template_name = (
        'freelance/executor_detail.html' #Укажите ваш путь к шаблону
    )

