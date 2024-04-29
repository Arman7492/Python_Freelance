from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.db.models import OuterRef, Exists
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from freelance.models import Order, OrderRequest, UserProfile
from ratings.models import RatingOrder
from ratings.forms import RatingForm


class RatingListView(LoginRequiredMixin, ListView):
    model = RatingOrder
    template_name = "ratings/rating_list.html"
    form_class = RatingForm
    success_url = reverse_lazy("ratings:rating_list")
    content_object_name = "ratings"

class RatingUpdateView(LoginRequiredMixin, UpdateView):
    model = RatingOrder
    template_name = "ratings/rating_update.html"
    form_class = RatingForm
    success_url = reverse_lazy("ratings:rating_list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get('order')
        if queryset is None:
            queryset = RatingOrder.objects.filter(order_id=pk)
            self.pk = queryset.first().pk

        user_type = {"Customers": "customer", "Executors": "executor"}.get(
            self.request.user.groups.first().name, 'customer'
        )

        # Получаем или создаем заказ
        order = get_object_or_404(Order, pk=pk)

        # Попытаемся найти уже существующий RatingOrder
        rating_order = queryset.first()

        # Если RatingOrder не найден, создаем новый
        order_request = OrderRequest.objects.filter(
            order=order, status__in=["accepted"]
        ).distinct().first()

        if user_type == "customer":
            user = order_request.executor.profile
        else:
            user = order.customer.profile

        if not rating_order:
            rating_order = RatingOrder.objects.create(order=order, user=user)
            self.pk = rating_order.pk
        return rating_order
    

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # stars = request.POST
        stars = '5'
        if form.is_valid():
            return self.form_valid(form)
        else:
            if form.error_class:
                form.error_class = None
                self.object = self.get_object()
                form = self.get_form()
                if form.save(commit=False):
                    form.save()
                    user = UserProfile.objects.get(user=form.instance.user.user)
                    user.rating = (user.rating + float(stars)) / 2
                    user.save()
                    return redirect(self.get_success_url())
                else:
                    return self.form_invalid(form)
            return self.form_invalid(form)

