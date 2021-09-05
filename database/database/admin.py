from django.contrib import admin

from .models import User, Status_data, Directory, File ,File_section, Section_category, Section_status, FramaOutput, Group_project, Group_task

admin.site.register(User)

admin.site.register(Status_data)

admin.site.register(Directory)

admin.site.register(File)

admin.site.register(File_section)

admin.site.register(Section_status)

admin.site.register(Section_category)

admin.site.register(FramaOutput)

admin.site.register(Group_project)

admin.site.register(Group_task)

