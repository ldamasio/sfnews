from django.db import models
from fastapi import FastAPI
from pydantic import BaseModel as _BaseModel

class Count(BaseModel):
    count: int

class Article(BaseModel):
    uid: int
    title: str
    url: str
    imageurl: str
    newssite: str