#!/usr/bin/env python
"""
Script para eliminar usuarios duplicados de la base de datos
Uso: python delete_user.py <username>
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_analytics_server.settings')
django.setup()

from django.contrib.auth.models import User

if len(sys.argv) < 2:
    print("Uso: python delete_user.py <username>")
    print("\nUsuarios existentes:")
    for user in User.objects.all():
        print(f"  - {user.username}")
    sys.exit(1)

username = sys.argv[1]
try:
    user = User.objects.get(username=username)
    user.delete()
    print(f"✓ Usuario '{username}' eliminado exitosamente")
except User.DoesNotExist:
    print(f"✗ Usuario '{username}' no existe")
    sys.exit(1)
