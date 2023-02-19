from django.shortcuts import render
from django.utils import timezone


# Create your views here.
def function_test(request):
    today = timezone.now()
    today_date = today.astimezone().date()
    first_day = today_date.replace(day=1)
    print(first_day)
    return render(request, 'unit/function_test.html')