#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import platform
import sys


def main():
    """Run administrative tasks."""

    # 운영 체제 확인
    current_os = platform.system()
    current_distribution = ""

    if current_os == "Linux":
        # 배포판 이름 확인
        if os.path.isfile("/etc/os-release"):
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("NAME="):
                        current_distribution = line.strip().split("=")[1].strip('"')
                        break

        # Amazon Linux 여부 확인
        if "Amazon" in current_distribution:
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.product")
        else:
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development_sqlite")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development_sqlite")

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


# cicd test 17:08
