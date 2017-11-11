from django.contrib import admin

# Register your models here.
from .models import UserNotes
 
class NotesAdmin(admin.ModelAdmin):
    class Meta:
        model = UserNotes
    fields = ('title', 'text')
    classes = ('wide')
 
admin.site.register(UserNotes,NotesAdmin)
