import os
import requests
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
        print("     >file already cleaned")

    list = os.listdir(dir_title)

    for i in range (0, len(os.listdir(dir_title))):
        if not (dir_title in list[i]):
            os.replace(dir_title + "\\" + list[i], "{}\\{} {}".format(dir_title,  dir_title, list[i]))
        else:
            print("     > Directory '{}' already named".format(list[i]))
    #metadata
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
