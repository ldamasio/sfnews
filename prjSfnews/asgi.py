"""
ASGI config for prjSfnews project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from fastapi import FastAPI
from polls.routers import choices_router
from polls.routers import questions_router

fastapp = FastAPI()
fastapp.include_router(questions_router, tags=["questions"], prefix="/question")
fastapp.include_router(choices_router, tags=["choices"], prefix="/choice")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prjSfnews.settings')

application = get_asgi_application()
