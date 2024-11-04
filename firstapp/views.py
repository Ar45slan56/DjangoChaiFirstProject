from django.shortcuts import render, get_object_or_404
from .models import ChaiVriety, Store
from .forms import ChaiVrietyForm


def all_home(request):
    chais = ChaiVriety.objects.all()
    return render(request, 'all_home.html', {'chais': chais})


def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVriety, pk=chai_id)
    return render(request, 'chai_detail.html', {'chai': chai})


def chai_store_view(request):
    stores = None
    chai_varity = None
    if request.method == 'POST':
        form = ChaiVrietyForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['ChaiVriety']
            stores = Store.objects.filter(chai_variety=chai_varity)
    else:
        form = ChaiVrietyForm()

    # Pass a single dictionary to the render function
    return render(request, 'chai_store.html', {'stores': stores, 'form': form})
