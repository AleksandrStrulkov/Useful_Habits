from django.contrib import admin

from habit_app.models import Habit


# Register your models here.
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'date', 'place', 'time_when_execute', 'action', 'nice_habit', 'related_habit',
                    'periodicity', 'reward', 'lead_time', 'is_public')
    list_filter = ('name',)
    search_fields = ('name', 'action',)
