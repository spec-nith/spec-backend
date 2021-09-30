import tempfile

from django.test import override_settings

common_settings = override_settings(
    DEFAULT_FILE_STORAGE="django.core.files.storage.FileSystemStorage",
    PASSWORD_HASHERS=("django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",),
    MEDIA_ROOT=tempfile.gettempdir(),
)
