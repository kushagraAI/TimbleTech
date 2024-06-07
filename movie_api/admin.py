from django.contrib import admin
from .models import CustomUser, Movie, Review
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# @admin.register(CustomUser,Movie,Review, site=custom_admin_site)

admin.site.site_title = "timble tech"
admin.site.site_header = "Timble Tech"
admin.site.index_title = "Welcome to Timble Tech"

# @admin.register(CustomUser,Movie,Review)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['rating', 'comment']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
