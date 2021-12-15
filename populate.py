import psycopg
import requests
import json
import sys
import os
import django
sys.path.append('prjSfnews')
os.environ['DJANGO_SETTINGS_MODULE'] = 'prjSfnews.settings'
django.setup()
from base.models import Count, Article

def original_count():
    request = requests.get("https://api.spaceflightnewsapi.net/v3/articles/count")
    decoded_count = request.content.decode('utf-8')
    return decoded_count
original_count_int = int(original_count())
 
interno_count = Count.objects.first().count

dif_count = original_count_int - int(interno_count)
b = original_count_int - dif_count
c = 0
d = interno_count + 1
novo_count = interno_count
while (c < dif_count):
    url_nova = "https://api.spaceflightnewsapi.net/v3/articles/" + str(d)
    request = requests.get(url_nova)
    article_result = request.content.decode('utf-8')        
    if (article_result != "Not Found"):
        e = json.loads(article_result)
        pretty_response = json.dumps(e, indent=4)
        print ('Coletado da agência ...   ', e['newsSite'])
        print(pretty_response)
        f_uid=int(e['id'])
        f_title=str(e['title'])
        f_url=str(e['url'])
        f_imageurl=str(e['imageUrl'])
        f_newssite=str(e['newsSite'])
        f = Article(uid=f_uid, title=f_title, url=f_url, imageurl=f_imageurl, newssite=f_newssite)
        f.save()    
    novo_count = novo_count + 1
    print('%s' % novo_count)
    Count.objects.update(count=novo_count)
    d = d + 1
    c = c + 1


print ('[SFNEWS] Banco de dados alimentado.')