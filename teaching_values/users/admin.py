from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from teaching_values.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ["username", "name", "is_superuser"]
    list_filter = ["is_superuser"]
    search_fields = ["name"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Datos de usuario",
            {"fields": ("name",)},
        ),
        (
            "Permisos de administrador",
            {
                "classes": ("collapse",),
                "fields": (
                    ("is_active",),
                    ("is_staff",),
                    ("is_superuser",),
                    # ("groups"),
                    # ("user_permissions"),
                ),
            },
        ),
        ("Metadata", {"classes": ("collapse",), "fields": ("modified", "created")}),
    )
    readonly_fields = ["created", "modified"]
