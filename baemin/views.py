from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Shop
from .forms import OrderForm


def shop_list(request):
    shop_list = Shop.objects.all()
    return render(request, 'baemin/shop_list.html', {
        'shop_list': shop_list,
    })

@login_required
def order(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = OrderForm(shop, request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.shop = shop
            order.user = request.user
            order.save()

            form.save_m2m() # NOTE:  필히 호출. form.save() 내에서 save_m2m()이 호출되는데, commit=False시에는 호출되지 않음.
            return redirect('profile')

    else:
        form = OrderForm(shop)
    return render(request, 'baemin/order.html', {
        'form': form,
    })
