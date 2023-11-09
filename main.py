import requests
from bs4 import BeautifulSoup
import os

Arabic = True




# global name
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
  name = None
  if Arabic:
    name = soup.find("h1", {"style" : "font-size:20px;margin:0"})
  else:
    td_tags = soup.find_all("td")
    for i in td_tags:
      b = i.find("b")
      if b is not None:
        if "ا"  in str(b):
          pass
        else:
          name = b
          break
        # here
  return name

def main(filename):
  a =1
  with open(f"{filename}", "r") as f:
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

# for i in os.listdir("data_ydk"):

    


import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def upload_file():
    file_path = entry_file_path.get()
    if file_path:
        # print("Uploaded file:", file_path)
        if file_path.split(".")[-1] == "ydk":
            main(file_path)
    

root = tk.Tk()
root.title("File Upload GUI")

entry_file_path = tk.Entry(root, width=40)
entry_file_path.grid(row=0, column=0, padx=10, pady=10)

button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.grid(row=0, column=1, padx=10, pady=10)

button_upload = tk.Button(root, text="Upload", command=upload_file)
button_upload.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
