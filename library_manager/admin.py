from django.contrib import admin
from .models import Books, Members, Authors, Publishers, Loans,  Genres

admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Publishers)
admin.site.register(Genres)
admin.site.register(Members)
admin.site.register(Loans)

# Register your models here.
