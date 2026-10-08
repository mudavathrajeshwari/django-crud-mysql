from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer


def index(request):
    if request.method == "POST":
        cid = request.POST.get("cid")
        cname = request.POST.get("cname")
        cemail = request.POST.get("cemail")
        ccity = request.POST.get("ccity")

        Customer.objects.create(
            cid=cid,
            cname=cname,
            cemail=cemail,
            ccity=ccity
        )
        return redirect("index")

    customers = Customer.objects.all()
    return render(request, "index.html", {"customers": customers})


def customer_edit(request, cid):
    customer = get_object_or_404(Customer, cid=cid)

    if request.method == "POST":
        customer.cname = request.POST.get("cname")
        customer.cemail = request.POST.get("cemail")
        customer.ccity = request.POST.get("ccity")
        customer.save()
        return redirect("index")

    return render(request, "customer_edit.html", {"customer": customer})


def customer_delete(request, cid):
    customer = get_object_or_404(Customer, cid=cid)
    customer.delete()
    return redirect("index")