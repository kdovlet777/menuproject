from django.shortcuts import render
from menuapp.models import MenuItem

def base(request):
    main_menu_items = MenuItem.objects.filter(menu_name='main_menu')
    context = {
        'main_menu': main_menu_items,
    }
    return render(request, 'base.html', context)