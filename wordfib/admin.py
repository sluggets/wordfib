from django.contrib import admin
from wordfib.models import WordAndTrue, FakeDefinitions, CorrectGuess

# Register your models here.
class FakeInline(admin.TabularInline):
    model = FakeDefinitions
    extra = 7

class WordAndTrueAdmin(admin.ModelAdmin):
    inlines = [FakeInline]
    search_fields = ['word']

admin.site.register(WordAndTrue, WordAndTrueAdmin)
admin.site.register(CorrectGuess)
