from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MenuOrder, MenuSection


class MenuSectionInline(admin.TabularInline):
    model = MenuSection
    extra = 1


@admin.register(MenuOrder)
class MenuOrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'event_name',
        'event_date'
    )

    inlines = [MenuSectionInline]