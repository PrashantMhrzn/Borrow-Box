from django.contrib import admin
from .models import *

# Text changes in admins page
admin.site.site_title = 'Borrow Box'
admin.site.site_header = 'Borrow Box Admin'
admin.site.index_title = 'Welcome to Borrow Box Admins Page'

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'genre')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Reserve)
# admin.site.register(Fine)
admin.site.register(Borrow)
