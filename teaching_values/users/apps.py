from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "teaching_values.users"
    verbose_name = "usuarios"

    def ready(self):
        try:
            import teaching_values.users.signals  # noqa: F401
        except ImportError:
            pass
