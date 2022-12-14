from django.contrib import admin

from todos_app.todos.models import Todo, Person, Category


# Option 2
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['text', 'owner']
    sortable_by = 'text'
    list_filter = ['owner']


# Option 1
# admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)
