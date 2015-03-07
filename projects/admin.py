from django.contrib import admin
from .models import Project



class PostAdmin(admin.ModelAdmin):
        fieldsets = [
                (None, {'fields': ['author', 'title', 'project', 'text']}),
                ('Date Information', {'fields': ['created_date', 'published_date']}),
        ]

        list_display = ('title', 'created_date', 'published_date')


admin.site.register(Project)
