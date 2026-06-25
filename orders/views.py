from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import MenuOrder


def print_order(request, pk):
    order = get_object_or_404(MenuOrder, pk=pk)
    return render(
        request,
        "print_order.html",
        {"order": order}
    )

def print_order2(request, pk):
    order = get_object_or_404(
        MenuOrder,
        pk=pk
    )
    return render(
        request,
        "print_order2.html",
        {
            "order": order
        }
    )

def home(request):

    orders = MenuOrder.objects.order_by("-id")

    return render(
        request,
        "home.html",
        {
            "orders": orders
        }
    )

from django.shortcuts import render, redirect
from .models import MenuOrder, MenuSection


def new_order(request):

    if request.method == "POST":

        customer_name = request.POST.get("customer_name")
        event_name = request.POST.get("event_name")
        event_date = request.POST.get("event_date")

        order = MenuOrder.objects.create(
            customer_name=customer_name,
            event_name=event_name,
            event_date=event_date
        )

        categories = request.POST.getlist("category[]")
        items = request.POST.getlist("items[]")

        for category, item_text in zip(categories, items):

            if category.strip():

                MenuSection.objects.create(
                    order=order,
                    category=category,
                    items=item_text
                )

        return redirect("/")

    return render(request, "new_order.html")

def edit_order(request, pk):

    order = get_object_or_404(MenuOrder, pk=pk)

    if request.method == "POST":

        order.customer_name = request.POST.get("customer_name")
        order.event_name = request.POST.get("event_name")
        order.event_date = request.POST.get("event_date")

        order.save()

        order.sections.all().delete()

        categories = request.POST.getlist("category[]")
        items = request.POST.getlist("items[]")

        for category, item_text in zip(categories, items):

            if category.strip():

                MenuSection.objects.create(
                    order=order,
                    category=category,
                    items=item_text
                )

        return redirect("home")

    return render(
        request,
        "edit_order.html",
        {
            "order": order,
            "sections": order.sections.all()
        }
    )


def delete_order(request, pk):

    order = get_object_or_404(
        MenuOrder,
        pk=pk
    )

    order.delete()

    return redirect("home")