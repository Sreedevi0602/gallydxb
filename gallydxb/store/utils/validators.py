import os
from django.core.exceptions import ValidationError

def validate_video_file_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.mp4', '.webm', '.mov', '.avi']
    if ext not in valid_extensions:
        raise ValidationError(
            f"Unsupported video file extension '{ext}'. Allowed types: {', '.join(valid_extensions)}."
        )