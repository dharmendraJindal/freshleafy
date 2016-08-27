#!/usr/bin/env python
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/"

# Run Django.
if __name__ == "__main__":
    settings_module = "settings.base"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
