from django.contrib import admin

from .models import about
from .models import experience
from .models import skill
from .models import skill_icon
from .models import intro
from .models import photo

admin.site.register(photo)
admin.site.register(intro)
admin.site.register(about)
admin.site.register(experience)
admin.site.register(skill)
admin.site.register(skill_icon)
