import requests
import os
#os.system("pip install mangadex-downloader --upgrade")


title = input("     > What manga would you like to search for \n     > ")
base_url = "https://api.mangadex.org"
title_url = "https://mangadex.org/title/"
r = requests.get(
    f"{base_url}/manga",
    params={"title": title}
)
#uh = (str(r.json()["data"]))
#f = open("json.txt", "w", encoding='utf-8')
#f.write(uh)
#f.close()
titles=([manga["attributes"]["title"]['en'] for manga in r.json()["data"]])
ids=([manga["id"] for manga in r.json()["data"]])
urls=[title_url + x for x in ids]
dict_output = dict(zip(titles, urls))
#print(dict_output)

print("\n     > Manga results\n    ")
for d in titles:
    print("     > ({})".format(titles.index(d) + 1) , d)
print("\n     > Choose manga based on number ")
chosen_manga = int(input("     > ")) - 1
dir_title = titles[chosen_manga]
num = urls[chosen_manga]

if input("     > add covers? (y/n)\n     > ") == "y":
    os.system('mangadex-dl {} --save-as "pdf-volume" --use-volume-cover -uvc --progress-bar-layout=none' .format(num))
else:
    os.system('mangadex-dl {} --save-as "pdf-volume" --progress-bar-layout=none' .format(num))
print("     >finsihed downloading")
try:
    os.remove(dir_title + "\\cover.jpg")
    os.remove(dir_title + "\\download.db")
except FileNotFoundError:
    print("     >file already cleaned")

list = os.listdir(dir_title)

for i in range (0, len(os.listdir(dir_title))):
    if not (dir_title in list[i]):
        os.replace(dir_title + "\\" + list[i], "{}\\{} {}".format(dir_title,  dir_title, list[i]))
    else:
        print("     > Directory '{}' already named".format(list[i]))
print("     > Done!")