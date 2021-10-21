from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'massage', 'date_add', 'public')
 

admin.site.register(Note, NoteAdmin)
