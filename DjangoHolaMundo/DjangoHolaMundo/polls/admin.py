from django.contrib import admin

# Register your models here.
from .models import Question, Choice

##class ChoiceInline(admin.TabularInline): ...

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionModelAdmin(admin.ModelAdmin):
    ##fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    

    

#admin.site.register(Question)
admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice)