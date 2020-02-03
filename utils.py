import requests
import json
import re
import ssl
from BeautifulSoup import BeautifulSoup as bs


#Add filters such that the user can go ahead and limit whether
#they want only gifs, images, posts with comments above this number,#posts with comments greater than 
#Make sure that the page number limit is 100. 
 
def annotate(number_of_pages, page_type):
  final_result = list()
  
  for c in range(1,number_of_pages+1): 

    type = 'Image'
    xkcd = requests.get("http://xkcd.com/{}".format(c))
    soup = bs(xkcd.text)
    comic = soup.find("div", {"id": "comic"})
    media_url = ""
    if comic is not None :
      if comic.img is None:
          print ("{} does not have an image tag".format(c))
          continue

    print(comic)
    media_url = "https://www."+comic.img["src"][2:]
    ssl.match_hostname = lambda cert, hostname: True
    print(media_url)
    #media_url = "http://xkcd.com/{}".format(c)#ii.find('img', attrs = {'class' : 'badge-item-img'})['src']
    # post_url = ii['data-entry-url']
    # votes = ii['data-entry-votes']
    # comments = ii['data-entry-comments']
    comic_title = soup.find("div", {"id": "ctitle"})
    #print(comic_title.text)
    title = "XKCD " #comic_title
    print(media_url)
    final_result.append({
      "type" : type , 
      "title" : title,
      "media_url" : media_url
      })
  return final_result

def get_posts_from_page(number_of_pages = 2, media_type = 'all', page_type = None, more_votes_than = 0, more_comments_than = 0):
  data = annotate(number_of_pages, page_type)
  data = [el for el in data if el['type'] == 'Image']
  jsonData = json.loads(json.dumps(data));
  return jsonData


