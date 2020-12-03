from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from upcomingevents.models import Event, Venue, MyClubUser
from upcomingevents.forms import VenueForm
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def all_events(request):
    events_list = Event.events.all()
    return render(request, 'upcomingevents/events_list.html', {'events_list':events_list})


# Create your views here.
def index(request, year=date.today().year, month=date.today().month):
    # usr = request.user
    # ses = request.session
    # paht = request.path
    # path_info = request.path_info
    # headers = request.headers
    # assert False
    announcements = [
        {
        'date':'6-10-2020',
        'announcement':'Club Registration Open'
        },

        {
            'date':'6-15-2020',
            'announcement':'John Smith Elected new President'
        }

    ]

    year = int(year)
    month = int(month)

    if year < 2000 or year > 2099:
        year = date.today().year

    month_name = calendar.month_name[month]
    title = 'My Club Event Calendar - %s %s' % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse('<h1>%s</h><p>%s</p>' % (title, cal))
    return TemplateResponse(request, 'upcomingevents/index.html', {'title':title, 'cal':cal, 'announcements':announcements})

@login_required(login_url=reverse_lazy('login'))
def add_venue(request):
    assert False
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'upcomingevents/add_venue.html', {'form':form, 'submitted':submitted})

def list_subscribers(request):
    p = Paginator(MyClubUser.objects.all(), 3)
    page = request.GET.get('page')
    subscribers = p.get_page(page)
    return render(request, 'upcomingevents/subscribers.html', {'subscribers':subscribers})

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)