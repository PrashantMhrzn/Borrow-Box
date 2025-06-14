from django.contrib import admin
from .models import *

# Text changes in admins page
admin.site.site_title = 'Borrow Box'
admin.site.site_header = 'Borrow Box Admin'
admin.site.index_title = 'Welcome to Borrow Box Admins Page'

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre__category', 'author__name')
    search_fields = ('title', 'genre__category', 'author__name')
    list_filter = ('title', 'genre__category', 'author__name')

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Author, AuthorAdmin)

class GenreAdmin(admin.ModelAdmin):
    search_fields = ('category',)

admin.site.register(Genre, GenreAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'book__title', 'rating')
    search_fields = ('user__username','book', 'rating')
    list_filter = ('user__username', 'book__title', 'rating')


admin.site.register(Review, ReviewAdmin)

class ReserveAdmin(admin.ModelAdmin):
    search_fields = ('user__username','book__title',)
    list_filter = ('user__username', 'book__title', 'reserve_date', 'status')


admin.site.register(Reserve, ReserveAdmin)
# admin.site.register(Fine)
class BorrowAdmin(admin.ModelAdmin):
    list_filter = ('user__username', 'book__title', 'borrow_date', 'return_date')
    search_fields = ('user__username', 'return_date')
admin.site.register(Borrow, BorrowAdmin)
