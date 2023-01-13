from django.contrib import admin
from .models import CartItem


class ItemSelledFilter(admin.SimpleListFilter):
    title = 'Товар продан (default=Yes)'
    parameter_name = 'selled'

    def lookups(self, request, model_admin):
        return (('no', 'Нет'), )

    def queryset(self, request, queryset):
        ''' selled=True is default queryset '''
        if self.value() == 'no':
            return queryset.filter(selled=False)
        return queryset.filter(selled=True)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin): 
    fields_need = ['name', 'price', 'created_at', ]
    list_display = fields_need
    readonly_fields = fields_need
    list_filter = [ItemSelledFilter, ] 
