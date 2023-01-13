from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from cart.models import CartItem
from django.utils.safestring import mark_safe


class ItemSelledFilter(admin.SimpleListFilter):
    ''' Required to get users who have bought at least one product '''
    title = 'Реальный покупатель (default=Yes)'
    parameter_name = 'real_buyer'

    def lookups(self, request, model_admin):
        return (('no', 'Нет'), )

    def queryset(self, request, queryset):
        ''' users_filter is default queryset '''
        users_filter = User.objects.none()
        for user in queryset:
            if any(item.selled == True for item in user.items.all()):
                users_filter |= User.objects.filter(id=user.id)

        if self.value() == 'no':
            return queryset.exclude(id__in=users_filter)
        return users_filter


class CartItemTabularInline(admin.TabularInline):
    model = CartItem
    fields_need = ['id_product', 'name', 'created_at', 'price', ]
    fields = fields_need
    readonly_fields = fields_need
    can_delete = False
    extra = 0

    def id_product(self, obj):
        return obj.item.id


admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields_need = ['username', 'last_login', 'first_name', 'email', 
                   'get_city', 'get_house', 'get_street', 
                   'get_number_phone', 'get_comments', ]  
    
    fields = fields_need 
    readonly_fields = fields_need
    list_display = fields_need 
    inlines = [CartItemTabularInline, ]
    list_filter = [ItemSelledFilter, ]     

    def get_city(self, obj):
        return obj.profile.city

    def get_street(self, obj):
        return obj.profile.street

    def get_house(self, obj):
        return obj.profile.house

    def get_number_phone(self, obj):
        return obj.profile.number_phone

    def get_comments(self, obj):
        return obj.profile.comments                
        
    get_city.__name__ = 'ГОРОД'
    get_street.__name__ = 'УЛИЦА'
    get_house.__name__ = 'ДОМ'
    get_number_phone.__name__ = 'ТЕЛЕФОН'
    get_comments.__name__ = 'КОММЕНТАРИИ К ЗАКАЗУ'


