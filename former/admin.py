from django.contrib import admin
from .models import question,Forms,answer
# Register your models here.
admin.site.register(question)
admin.site.register(Forms)
admin.site.register(answer)