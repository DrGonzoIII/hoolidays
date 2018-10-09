from django.shortcuts import render
from .models import Holidays


# Create your views here.
def index(request):
    holidays_list = Holidays.objects.order_by('holiday_date')[:5]
    context = {'holidays_list': holidays_list}
    return render(request, 'holidays/index.html', context)
