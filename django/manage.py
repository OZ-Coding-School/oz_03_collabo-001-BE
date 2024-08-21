#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import platform
import sys


def main():
    """Run administrative tasks."""

    # 운영 체제 확인
    current_os = platform.system()

    if current_os == "Darwin":  # macOS
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development_sqlite")
    elif current_os == "Linux":
        # Amazon Linux를 더 정확하게 확인하려면 추가 검사가 필요할 수 있습니다.
        # 여기서는 Linux를 Amazon Linux로 가정합니다.
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.product")
    else:
        # 기본값 설정 (다른 OS의 경우)
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.product")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
