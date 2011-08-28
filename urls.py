from django.conf.urls.defaults import *
import os
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^powernote/', include('powernote.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(ROOT_PATH,'site_media/')}),
)


urlpatterns += patterns('photoapp.views',
    (r'^photo/home/$', 'view_photo_home', {'photo_home_template': 'photoapp/photo_home.html'}, 'photo_home'),
    (r'^photo/register/$', 'view_photo_register', {'photo_home_register_template': 'photoapp/photo_register.html'}, 'photo_register'),                        
)
 
urlpatterns += patterns('note.views',
    (r'^save_note/$', 'view_save_note', {}, 'save_note'),
    (r'^notes_for_page/$', 'view_notes_for_page', {}, 'page_notes'),        
    (r'^properties/$','view_properties', {'property_template':'note/note_property.html'}, 'note_properties'),        
    (r'^test_ajax/$', 'view_ajax_test', {}, 'test_ajax'),
)
