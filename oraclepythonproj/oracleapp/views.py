from django.shortcuts import render

from .models import locations

def index(request):
      location_list = locations.objects.all().order_by('location_id')
      cont = {'locations': location_list}
      return render(request, 'index.html', cont)

