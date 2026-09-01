#!/usr/bin/env python
"""
Script para verificar la configuración de archivos estáticos
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_analytics_server.settings')
django.setup()

from django.conf import settings
import pathlib

print("=" * 60)
print("DIAGNÓSTICO DE ARCHIVOS ESTÁTICOS")
print("=" * 60)

print(f"\n📍 DEBUG: {settings.DEBUG}")
print(f"📍 STATIC_URL: {settings.STATIC_URL}")
print(f"📍 STATIC_ROOT: {settings.STATIC_ROOT}")
print(f"\n📁 STATICFILES_DIRS:")
for dir in settings.STATICFILES_DIRS:
    print(f"   - {dir}")
    exists = os.path.exists(dir)
    print(f"     ¿Existe? {exists}")
    if exists:
        files = os.listdir(dir)
        print(f"     Archivos: {len(files)}")

print(f"\n📦 STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")

print(f"\n✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")

# Verificar si existe STATIC_ROOT
static_root = pathlib.Path(settings.STATIC_ROOT)
print(f"\n📁 STATIC_ROOT existe? {static_root.exists()}")
if static_root.exists():
    files_count = len(list(static_root.rglob('*')))
    print(f"   Archivos en STATIC_ROOT: {files_count}")
    
    # Mostrar archivos CSS
    css_files = list(static_root.rglob('*.css'))
    print(f"   Archivos CSS: {len(css_files)}")
    for css in css_files[:5]:
        print(f"     - {css.relative_to(static_root)}")

print("\n" + "=" * 60)
