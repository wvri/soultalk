from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
#from .models import PsychologistProfile
#admin.site.register(PsychologistProfile)
from .models import PsychologyTip
from .models import Psychologist

admin.site.register(CustomUser, UserAdmin)
admin.site.register(PsychologyTip)
admin.site.register(Psychologist)