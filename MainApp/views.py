from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return render(request, "index.html")


def items_list(request):
    items = Item.objects.all()
    contex = {
        "items": items
    }
    return render(request, "items.html", contex)


def item(request, id):
    # for i in items:
    #     if int(i["id"]) == int(id):
    #         return render(request, "item_page.html", i)
    try:
        item = Item.objects.get(pk=id)
        contex = {"item": item}
        return render(request, "item_page.html", contex)
    except ObjectDoesNotExist:
        raise Http404(f"Товар с id={id} не найден")
