from django.urls import path, re_path
from . import views
from .views import ListViewDemo, DetailViewDemo, CreateViewDemo, UpdateViewDemo, DeleteViewDemo, ArchiveIndexViewDemo, MonthArchiveViewDemo
from django.views.generic.dates import ArchiveIndexView
from .models import Event
from upcomingevents.forms import SurveyForm1, SurveyForm2, VenueForm, EventForm
from upcomingevents.views import SurveyWizard, ModelFormWizard



urlpatterns = [
    path('new/', ModelFormWizard.as_view([VenueForm, EventForm]), name='wizard-demo'),
    path('', views.index, name='index'),
    path('eventarchive/', ArchiveIndexViewDemo.as_view()),
    path('<int:year>/<int:month>/', MonthArchiveViewDemo.as_view(), name='event-montharchive'),
    path('add_venue/', views.add_venue, name='add_venue'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),
    # path('events/', views.all_events, name='all_events'),
    path('events/', ListViewDemo.as_view(), name='show-events'),
    path('event/<int:pk>', DetailViewDemo.as_view(), name='event-detail'),
    path('event/add', CreateViewDemo.as_view(), name='add-event'),
    path('event/update/<int:pk>', UpdateViewDemo.as_view(), name='update-event'),
    path('event/delete/<int:pk>', DeleteViewDemo.as_view(), name='delete-event'),
    path('gencsv', views.gen_csv, name='generate-csv-file'),
    path('gentext', views.gen_text, name='generate-text-file'),
    path('genpdf', views.gen_pdf, name='generate-pdf-file'),
    path('getsubs', views.list_subscribers, name='list-subscribers'),
    path('tdemo', views.template_demo, name='tdemo'),
    path('condemo/', views.context_demo, name='condemo'),
    path('committee', views.committee_formset, name='committee'),
    path('allevents/', views.demo_views.all_events, name='all-events'),
    path('survey/', SurveyWizard.as_view([SurveyForm1, SurveyForm2]), name='survey'),
]



