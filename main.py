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

if input("    > Add metadata? (y/n):\n     >") != "y":
    print("     > Done!")
else:
    from PyPDF2 import PdfReader, PdfWriter
    import json
    hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    author_url =  "https://api.mangadex.org/author/" + [manga["relationships"][0]["id"] for manga in r.json()["data"]][0]
    n = requests.get(author_url, headers=hearders)
    al = n.text
    author_dict = (json.loads('{"' + al[al.find('<body>') + 7 : al.find('</body>')] + "}"))
    author = (author_dict['data']['attributes']['name'])
    tags = r.json()["data"][0]['attributes']["tags"][0]['attributes']['name']['en']
    files = os.listdir(dir_title)

    directory = os.getcwd()
    for f in files:
        reader = PdfReader(dir_title + "\\" + f)
        writer = PdfWriter()
        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Add the metadata
        writer.add_metadata(
            {
                "/Title": f,
                "/Author": author,
                "/Subject": tags,
                "/Keywords": f.split(" Vol.")[0],
            }
        )

        # Save the new PDF to a file
        os.chdir(dir_title)
        with open(f, "wb") as f:
            writer.write(f)
        os.chdir(directory)
print("     > Done!")