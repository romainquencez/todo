#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == '__main__':
    local_file = Path('todo/settings/local.py')
    if local_file.is_file():
        os.environ.setdefault(
            'DJANGO_SETTINGS_MODULE', 'todo.settings.local')
    else:
        os.environ.setdefault(
            'DJANGO_SETTINGS_MODULE', 'todo.settings.production')

    from django.core.management import execute_from_command_line

    try:
        execute_from_command_line(sys.argv)
    except ImportError as e:
        print(e)
