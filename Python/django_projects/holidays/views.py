from django.shortcuts import render
from .models import Holidays
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    holidays_list = Holidays.objects.filter(
                    user=request.user).order_by('start_date')[:5]
    context = {
                'holidays_list': holidays_list,
                'num_visits': num_visits
              }
    return render(request, 'index.html', context)
