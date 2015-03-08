from django.contrib import admin
from .models import Project
from blogging.models import Post


class LinkInline(admin.TabularInline):
        model = Post.project.through


class ProjectAdmin(admin.ModelAdmin):
        inlines = [LinkInline, ]

admin.site.register(Project, ProjectAdmin)
