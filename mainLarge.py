from art import *
import os, sys
import requests
#libraries, os, requests, colorama, art 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

def prCyan(skk): print("\033 {}\033" .format(skk))
tprint(" KOBO PINE")
print("                /\ \n               /  \ \n              /    \ \n             /      \ \n             ⎺/    \⎺ \n             /      \ \n            /        \ \n           /          \ \n           ⎺⎺/      \⎺⎺ \n            /        \ \n           /          \ \n          /            \ \n          ⎺⎺⎺⎺⎺|__|⎺⎺⎺⎺⎺ \n\n")
print("     > welcome To Kobo Pine manga donwloader for Ebook and other uses")
print("     > would you like to (1) download a single manga or (2) download manga using a mangadex list")
print("     > mangadex lists may take up to an hour to update after created or edited")
ans = input("{}" .format("    > "))

def mangadld():
    title = input("     > What manga would you like to search for \n     > ")
    base_url = "https://api.mangadex.org"
    title_url = "https://mangadex.org/title/"
    r = requests.get(
        f"{base_url}/manga",
        params={"title": title}
    )
    #
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

    if input("     > Add metadata? (y/n):\n     >") != "y":
        input("     > Done! \n     > press enter to exit...")
    else:
        from PyPDF2 import PdfReader, PdfWriter
        import json
        base_url = "https://api.mangadex.org"
        r = requests.get(f"{base_url}/manga",params={"title": dir_title})
        hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
        author_url =  "https://api.mangadex.org/author/" + r.json()['data'][0]["relationships"][0]["id"]
        n = requests.get(author_url, headers=hearders)
        al = n.text
        author_dict = (json.loads('{"' + al[al.find('<body>') + 7 : al.find('</body>')] + "}"))
        
        author = (author_dict['data']['attributes']['name'])
        tags = []
        for i in r.json()["data"][0]["attributes"]["tags"]:
            tags.append(i["attributes"]["name"]["en"])    
        files = os.listdir(dir_title)

        directory = os.getcwd()
        
        for f in files:
            try:
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
                        "/Subject": str(tags),
                        "/Keywords": f.split(" Vol.")[0],
                    }
                )

                # Save the new PDF to a file
                os.chdir(dir_title)
                with open(f, "wb") as f:
                    writer.write(f)
                os.chdir(directory)
                print("     > added metadata to volume {}".format(f))
            except:
                print("     > volume {} failed to write metadata".format(f))
        
    print("     > metadata:\n     > Title: {}\n     > Author {}\n     > Main Tag: {}".format(dir_title, author, tags))
    input("     > Done! \n     > press enter to exit...")

def manga_list_dld():
    list2 = os.listdir(os.getcwd())
    user_id = input("     > please paste your user id here to get a list of your public manga lists: \n     > ctrl + click here to find your id https://mangadex.org/user/me \n     > ")
    os.system('mangadex-dl "list:{}" --save-as "pdf-volume" --use-volume-cover -uvc --progress-bar-layout=none' .format(user_id))
    new_manga = [item for item in os.listdir(os.getcwd()) if item not in list2]
    print("     > titles" + str(new_manga))

    for curr_manga in new_manga:
        dir_title = curr_manga
        try:
            os.remove(dir_title + "\\cover.jpg")
            os.remove(dir_title + "\\download.db")
        except FileNotFoundError:
            print("     > file already cleaned")

        list = os.listdir(dir_title)

        for i in range (0, len(os.listdir(dir_title))):
            if not (dir_title in list[i]):
                os.replace(dir_title + "\\" + list[i], "{}\\{} {}".format(dir_title,  dir_title, list[i]))
            else:
                print("     > Directory '{}' already named".format(list[i]))
        #get metadata
        from PyPDF2 import PdfReader, PdfWriter
        import json
        base_url = "https://api.mangadex.org"
        r = requests.get(f"{base_url}/manga",params={"title": dir_title}) # finds the mangas url
        hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
        author_url =  "https://api.mangadex.org/author/" + r.json()['data'][0]["relationships"][0]["id"]
        n = requests.get(author_url, headers=hearders)
        al = n.text
        author_dict = (json.loads('{"' + al[al.find('<body>') + 7 : al.find('</body>')] + "}"))
        
        author = (author_dict['data']['attributes']['name'])
        tags = []
        for i in r.json()["data"][0]["attributes"]["tags"]:
            tags.append(i["attributes"]["name"]["en"])    
        files = os.listdir(dir_title)

        directory = os.getcwd()
        
        for f in files:
            try:
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
                        "/Subject": str(tags),
                        "/Keywords": f.split(" Vol.")[0],
                    }
                )

                # Save the new PDF to a file
                os.chdir(dir_title)
                with open(f, "wb") as f:
                    writer.write(f)
                os.chdir(directory)
                print("     > added metadata to volume {}".format(f))
            except:
                print("     > volume {} failed to write metadata".format(f))
        
        print("     > metadata:\n     > Title: {}\n     > Author {}\n     > Main Tag: {}".format(dir_title, author, tags))

if ans == "1":
    mangadld()
elif ans == "2":
    manga_list_dld()
