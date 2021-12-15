from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
import django
sys.path.append('prjSfnews')
os.environ['DJANGO_SETTINGS_MODULE'] = 'prjSfnews.settings'
django.setup()
from base.models import Count, Article
from django.core import serializers
import json
#from typing import List
from django.core.serializers.json import DjangoJSONEncoder



class PyCount(BaseModel):
    count: int

class PyArticle(BaseModel):
    id_: int
    title: str
    url: str
    imageurl: str
    newssite: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"200 OK": "Back-end Challenge 2021 🏅 - Space Flight News"}

@app.get("/articles/")
def read_articles():
    articles = serializers.serialize("json", Article.objects.all(), fields=('uid', 'title', 'url', 'imagesurl', 'newssite'))
    return articles

@app.post("/articles/")
async def send_articles():
    return {"200 OK": "Back-end Challenge 2021 🏅 - Space Flight News"}

@app.get("/articles/count")
def read_count():
    item = Count.objects.first().count
    return item

@app.get("/articles/{item_id}")
def read_item(item_id: int):
    this_article = json.dumps(serializers.serialize("json", Article.objects.filter(uid=item_id), fields=('uid', 'title', 'url', 'imagesurl', 'newssite')), sort_keys=True, indent=4)
    return this_article

@app.put("/articles/{item_id}")
def send_article():
    return {"200 OK": "Back-end Challenge 2021 🏅 - Space Flight News"}

@app.delete("/articles/{item_id}")
def del_article():
    return {"200 OK": "Back-end Challenge 2021 🏅 - Space Flight News"}