from newsapi import NewsApiClient
import json
from datetime import date
from datetime import timedelta
import pprint 

today = date.today()
yesterday = today - timedelta(days = 1 )

pp = pprint.PrettyPrinter()
pp.pprint("Enter topic")
x = input()


newsapi = NewsApiClient(api_key='7f28dbaf34614d8aba94712f788a805b')

all_articles = newsapi.get_everything(q=x,from_param=date.today(),to=yesterday,language='en')

response=[]

for art in all_articles['articles']:
    response.append(art['title'] + " -> " + art['url']);
    
out_file = open('response.txt','w')

json.dump(response, out_file, indent=4)   

out_file.close()

pp.pprint(response)