from django.contrib import admin

from .models import AnnouncedPuResults, Agentname, States, Lga, Party, PollingUnit, Ward 





admin.site.register(AnnouncedPuResults)
admin.site.register(Agentname)
admin.site.register(States)
admin.site.register(Lga)
admin.site.register(Party)
admin.site.register(PollingUnit)
admin.site.register(Ward)