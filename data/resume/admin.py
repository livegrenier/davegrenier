from django.contrib import admin

from .models import about
from .models import experiance
from .models import skill
from .models import intro
from .models import photo

admin.site.register(photo)
admin.site.register(intro)
admin.site.register(about)
admin.site.register(experiance)
admin.site.register(skill)
