# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers

from note.models import NoteCategory
from note.models import Note


def view_save_note(request):
    if request.POST:
        y = request.POST['y-location']
        x = request.POST['x-location']
#        import pdb;pdb.set_trace()
        description = request.POST['description']
        note_id = request.POST['note_id']
        url = request.META['HTTP_REFERER']

        if note_id and note_id != 'new' :
            note = Note.objects.get(id=note_id)
        else:        
            note = Note()

        note.x_location = x
        note.y_location = y
        note.url  = url
        note.description = description
        note.is_ticket_shown = True
        note.is_active = True

        note_category = NoteCategory.objects.get(id=1)
        note.note_category = note_category
        note.save()
        
    return HttpResponse('Success')


def view_notes_for_page(request):
    url = request.META['HTTP_REFERER']
    notes = Note.objects.filter(url = url).values('id','description', 'x_location', 'y_location', 'is_ticket_shown', 'is_active')
    list_of_notes = []
    for note in notes:
        print note
        list_of_notes.append(note)    
    return HttpResponse(simplejson.dumps(list_of_notes))


def view_properties(request,property_template):
    note_id = request.GET['note_id']
    note_object = Note.objects.get(id=note_id)    
    from note.forms import NotePropertyForm
    if request.method == 'POST':
        note_property_form = NotePropertyForm(request.POST)
        if note_property_form.is_valid():
            description = note_property_form.cleaned_data['note_description']
            status = note_property_form.cleaned_data['note_status']
            show_ticket = note_property_form.cleaned_data['show_ticket']
            active = note_property_form.cleaned_data['active']
            note_category_id = note_property_form.cleaned_data['note_category']
            Note.objects.update_note(note_id, note_category_id, status, description, active, show_ticket)
            import pdb; pdb.set_trace()

    note_data = {}
    note_data['note_description'] = note_object.description
    note_data['note_status'] = note_object.status
    note_data['show_ticket'] = note_object.is_ticket_shown
    note_data['active'] = note_object.is_active
    note_data['note_category'] = note_object.note_category.id
    note_property_form = NotePropertyForm(data=note_data)
    return render_to_response(property_template, locals())

