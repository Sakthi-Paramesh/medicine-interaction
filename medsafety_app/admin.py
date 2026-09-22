from django.contrib import admin
from .models import User, Medicine, SavedMedicine, SearchHistory

admin.site.register(User)
admin.site.register(Medicine)
admin.site.register(SavedMedicine)
admin.site.register(SearchHistory)
