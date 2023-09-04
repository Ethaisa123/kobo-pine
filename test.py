import os
import requests
import json
import requests
base_url = "https://api.mangadex.org"
title = 'Migi tonari no Ukyo-san'

r = requests.get(f"{base_url}/manga",params={"title": title})
"""
x = (r.json()["data"])
chosen_id = ([manga["id"] for manga in r.json()["data"]])

chosen_id = "f49def38-26a2-4e71-a4ac-54473786a0c9"
base_url = "https://api.mangadex.org"
"""
y = {'result': 'ok', 
     'response': 'collection', 
     'data': [{'id': 'f49def38-26a2-4e71-a4ac-54473786a0c9', 
               'type': 'manga', 
               'attributes': {'title': {'en': 'Migi tonari no Ukyo-san'}, 
                                'altTitles': 
                                [{'ja': '右隣の右京さん'}, 
                                {'ja-ro': 'Migi tonari no Uyko-san'}, 
                                {'ja-ro': 'Migidonari no Ukyou-san'}, 
                                {'ja-ro': 'Migidonari no Ukyō-san'}, 
                                {'en': 'Ukyou-san On My Right'}], 
                                'description': {'en': "The story follows Ukyo-san and Sakata-kun who just got placed next to each other after changing seats. This one-shot was originally included in Jump RomCom Matsuri! as part of Shounen Jump's 2019 Valentine's Day celebrations.", 'fr': 'Une romance courte entre deux élèves qui peuvent être lu comme un livre ouvert.'}, 
                                'isLocked': False, 
                                'links': {'al': '108484', 'ap': 'migi-tonari-no-uyko-san', 
                                          'kt': 'migidonari-no-ukyou-san', 'mu': '183856', 
                                          'mal': '138965'}, 'originalLanguage': 'ja', 
                                'lastVolume': '', 
                                'lastChapter': '', 
                                'publicationDemographic': None, 
                                'status': 'completed', 'year': 2019,
                                'contentRating': 'safe', 
                                'tags': [{'id': '0234a31e-a729-4e28-9d6a-3f87c4966b9e', 'type': 'tag', 'attributes': {'name': {'en': 'Oneshot'}, 'description': {}, 'group': 'format', 'version': 1}, 'relationships': []}, 
                                        {'id': '423e2eae-a7a2-4a8b-ac03-a8351462d71d', 'type': 'tag', 'attributes': {'name': {'en': 'Romance'}, 'description': {}, 'group': 'genre', 'version': 1}, 'relationships': []}, 
                                        {'id': '4d32cc48-9f00-4cca-9b5a-a839f0764984', 'type': 'tag', 'attributes': {'name': {'en': 'Comedy'}, 'description': {}, 'group': 'genre', 'version': 1}, 'relationships': []}, 
                                        {'id': 'caaa44eb-cd40-4177-b930-79d3ef2afe87', 'type': 'tag', 'attributes': {'name': {'en': 'School Life'}, 'description': {}, 'group': 'theme', 'version': 1}, 'relationships': []}], 
                                'state': 'published', 'chapterNumbersResetOnNewVolume': False, 
                                'createdAt': '2019-10-27T22:48:48+00:00', 
                                'updatedAt': '2022-12-27T06:23:54+00:00', 
                                'version': 8, 
                                'availableTranslatedLanguages': ['en', 'id', 'vi', 'fr', 'pt-br', 'tr', 'it'], 
                                'latestUploadedChapter': 'd0207281-4829-4e69-a0e6-aee7af206e24'}, 
                                'relationships': [{'id': '74828944-5432-46fd-8859-cab89be785d6', 'type': 'author'}, {'id': '74828944-5432-46fd-8859-cab89be785d6', 'type': 'artist'}, {'id': 'f4ed7ee0-4551-4f9a-b811-440fde47cec8', 'type': 'cover_art'}]}
                                           ], 
     'limit': 10, 
     'offset': 0, 
     'total': 1}
x = {
'result': 'ok', 
'response': 'entity', 
'data': 
    {'id': 'f49def38-26a2-4e71-a4ac-54473786a0c9', 
    'type': 'manga', 
    'attributes': {
        'title': {'en': 'Migi tonari no Ukyo-san'}, 
        'altTitles': [{'ja': '右隣の右京さん'}, {'ja-ro': 'Migi tonari no Uyko-san'},{'ja-ro': 'Migidonari no Ukyou-san'}, {'ja-ro': 'Migidonari no Ukyō-san'}, {'en': 'Ukyou-san On My Right'}], 
        'description': {'en': "The story followlebrations.", 'fr': 'Une romance courte entre deux élèves qui peuvent être lu comme un livre ouvert.'}, 
        'isLocked': False, 
        'links': {'al': '108484', 'ap': 'migi-tonari-no-uyko-san', 'kt': 'migidonari-no-ukyou-san', 'mu': '183856', 'mal': '138965'}, 
        'originalLanguage': 'ja', 
        'lastVolume': '', 
        'lastChapter': '', 
        'publicationDemographic': None, 
        'status': 'completed', 
        'year': 2019, 
        'contentRating': 'safe', 
        'tags': [{'id': '0234a31e-a729-4e28-9d6a-3f87c4966b9e', 'type': 'tag', 'attributes': {'name': {'en': 'Oneshot'}, 'description': {}, 'group': 'format', 'version': 1}, 'relationships': []}, 
                {'id': '423e2eae-a7a2-4a8b-ac03-a8351462d71d', 'type': 'tag', 'attributes': {'name': {'en': 'Romance'}, 'description': {}, 'group': 'genre', 'version': 1}, 'relationships': []}, 
                {'id': '4d32cc48-9f00-4cca-9b5a-a839f0764984', 'type': 'tag', 'attributes': {'name': {'en': 'Comedy'}, 'description': {}, 'group': 'genre', 'version': 1}, 'relationships': []}, 
                {'id': 'caaa44eb-cd40-4177-b930-79d3ef2afe87', 'type': 'tag', 'attributes': {'name': {'en': 'School Life'}, 'description': {}, 'group': 'theme', 'version': 1}, 'relationships': []}], 
        'state': 'published', 
        'chapterNumbersResetOnNewVolume': False, 
        'createdAt': '2019-10-27T22:48:48+00:00', 
        'updatedAt': '2022-12-27T06:23:54+00:00', 
        'version': 8, 
        'availableTranslatedLanguages': ['en', 'id', 'vi', 'fr', 'pt-br', 'tr', 'it'], 
        'latestUploadedChapter': 'd0207281-4829-4e69-a0e6-aee7af206e24'},
        'relationships': [{'id': '74828944-5432-46fd-8859-cab89be785d6', 'type': 'author'}, 
                          {'id': '74828944-5432-46fd-8859-cab89be785d6', 'type': 'artist'}, 
                          {'id': 'f4ed7ee0-4551-4f9a-b811-440fde47cec8', 'type': 'cover_art'}]
    }
}
print(r.json()['data'][0]["relationships"][0]["id"])
exit()
print(r.json()['data'][0]["attributes"].keys())
exit()
tags = []
for i in r.json()["data"][0]["attributes"]["tags"]:
    tags.append(i["attributes"]["name"]["en"])
print(tags)

exit()
title = "Dachi no Imouto"
base_url = "https://api.mangadex.org"
title_url = "https://mangadex.org/title/"
r = requests.get(
    f"{base_url}/manga",
    params={"title": title}
)
print(r.json()["data"][0]['attributes']["tags"][0]['attributes']['name']['en'])
[{'id': '423e2eae-a7a2-4a8b-ac03-a8351462d71d', 'type': 'tag', 'attributes': {'name': {'en': 'Romance'}, 'description': {}, 'group': 'genre', 'version': 1}, 'relationships': []}, {'id': '4d32cc48-9f00-4cca-9b5a-a839f0764984', 'type': 'tag', 'attributes': {'name': {'en': 'Comedy'}, 'description': {}, 'group': 'genre', 'version': 1}, 'relationships': []}, {'id': 'caaa44eb-cd40-4177-b930-79d3ef2afe87', 'type': 'tag', 
'attributes': {'name': {'en': 'School Life'}, 'description': {}, 'group': 'theme', 'version': 1}, 'relationships': []}, {'id': 'e5301a23-ebd9-49dd-a0cb-2add944c7fe9', 'type': 'tag', 'attributes': {'name': {'en': 'Slice of Life'}, 'description': {}, 'group': 'genre', 'version': 1}, 'relationships': []}]
exit()
hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
author_url =  "https://api.mangadex.org/author/" + [manga["relationships"][0]["id"] for manga in r.json()["data"]][0]
n = requests.get(author_url, headers=hearders)
al = n.text
author_dict = (json.loads('{"' + al[al.find('<body>') + 7 : al.find('</body>')] + "}"))
print(author_dict['data']['attributes']['name'])
exit()

for i in r.json()["data"]:
    print("\n")
    print(i)
exit()
dir_title = "Sei-chan Capacity Over desu!"

try:
    os.remove(dir_title + "\\cover.jpg")
    os.remove(dir_title + "\\download.db")
except FileNotFoundError:
    print("file already cleaned")
list = os.listdir(dir_title)

for i in range (0, len(os.listdir(dir_title))):
    if not (dir_title in list[i]):
        os.replace(dir_title + "\\" + list[i], "{}\\{} {}".format(dir_title,  dir_title, list[i]))
    else:
        print("directory {} already named".format(list[i]))
exit()
url = "https://mangadex.org/title/f49def38-26a2-4e71-a4ac-54473786a0c9"
os.system('mangadex-dl {} --save-as "pdf-volume" --use-volume-cover -uvc' .format(url))



exit()
print("Kubo Won't Let Me Be Invisible_Vol.0".split("_Vol.")[0])
exit()

files = os.listdir(os.curdir)
print(files)
exit()
x = "Kubo Won't Let Me Be Invisible_Vol.0"
x.strip("_Vol.0")
print(x.strip("_Vol.0")
)


exit()
import shutil
import os
chap_pdf_location = "Ukyou-san_raws\\Migi tonari no Ukyo-san\\Ukyou-san_chapters"
folder_2_location = "Ukyou-san_raws\\Migi tonari no Ukyo-san"
vol_folder = os.getcwd()

print(chap_pdf_location.split("_raws")[0])
exit()
Title = "Migi tonari no Ukyo-san"
shutil.move(chap_pdf_location , vol_folder)
shutil.move(chap_pdf_location -  '{} Oneshot'.format(Title))

exit()
chapter_folders = ['[Fe Scans] Oneshot']
print(chapter_folders[0])
if chapter_folders[0].split(']')[0] + '] Oneshot' in chapter_folders:
    Oneshot_folder = chapter_folders[0].split(']')[0] + '] Oneshot'
    chapter_folders.remove(Oneshot_folder)
    chapter_folders.insert(0, Oneshot_folder)
else:
    chapter_folders.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))