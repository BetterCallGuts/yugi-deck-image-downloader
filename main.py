import requests
from bs4 import BeautifulSoup
import os



names_agin = []
def download_image(card_id, card_name=None):
  card_name+= "1"
  url     = "https://www.arab-duelists.com/"
  asseturl= "assets/img/cards/"
  s = f"{url}{asseturl}{card_id}.jpg"
  re      =  requests.get(s)
  
  names_agin.append(card_name)
  if card_name in names_agin:
    count = card_name[-1]
    count = int(count)
    count +=1
    card_name = card_name[:-1]
    card_name += str(count)
  with open(f"images/{card_name}.jpg", "wb" ) as f:
    
    f.write(re.content)
    
def get_card_name(card_id):
  
  re = requests.get(f"https://www.arab-duelists.com/?p=card&id={card_id}")
  soup = BeautifulSoup(re.content, "lxml")

  name = soup.find("h1", {"style" : "font-size:20px;margin:0"})
  return name

def main(filename):
  a =1
  with open(f"data_ydk/{filename}", "r") as f:
    for i in f.readlines():
      if "main" in i  or "side" in i or "extra" in i:
        continue
      name = get_card_name(f"{i}")
      if name is None:
        continue
      
      # names.append(name)
      download_image(str(i).strip("\n"), name.text)
      print("done", a)
      a +=1

for i in os.listdir("data_ydk"):
  if i.split(".")[-1] == "ydk":
    main(i)