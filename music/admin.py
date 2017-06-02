from django.contrib import admin
from .models import Album,Song,SignUp
from .forms import SignUpForm

admin.site.register(Song)


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["full_name","__unicode__","timestamp","updated"]
    form = SignUpForm
    class Meta:
        model = SignUp

admin.site.register(SignUp,SignUpAdmin)

class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', "location"]
    # list_display_links = ['']
    search_fields = ['__str__']

    class Meta:
        model = Album

admin.site.register(Album, AlbumModelAdmin)