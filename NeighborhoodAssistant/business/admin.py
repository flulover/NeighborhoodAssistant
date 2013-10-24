from django.contrib import admin
from models import login, user, merchant, housing_estate,\
    user_define_merchant, user_search_history, merchant_service_item,\
    merchant_statistical_data, merchant_comment, user_favourite_merchant

admin.site.register(login)
admin.site.register(user)
admin.site.register(merchant)
admin.site.register(housing_estate)
admin.site.register(user_define_merchant)
admin.site.register(user_search_history)
admin.site.register(merchant_service_item)
admin.site.register(merchant_statistical_data)
admin.site.register(merchant_comment)
admin.site.register(user_favourite_merchant)

