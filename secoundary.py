#py -3 -m pip install mangadex-downloader
import mangadex_downloader
import os
from PIL import Image
import shutil

print("welcome")
Title = input("what manga would you like to search for \n   :  ")
folder = (Title + "_manga_raws")
#_________________________________________________________
     

os.mkdir(folder)
os.system('mangadex-dl "{}" --search --folder "{}" ' .format(Title,folder))
print("---------------------------------------------------------------------")
folder_2_location = (folder + "\\{}" .format(os.listdir(folder)[0]))

volumes = []
chapter_folders = os.listdir(folder_2_location)
chapter_folders.remove("cover.jpg")
chapter_folders.remove("download.db")
print("file_system [/]")
#_________________________________________________________
os.mkdir(folder_2_location + "\\{}_chapters" .format(Title))
chap_pdf_location = (folder_2_location + "\\{}_chapters" .format(Title))
for i in range (0, (len(chapter_folders))  ):
    chap_folder_locaion = (folder_2_location + "\\{}".format(chapter_folders[i]))
    (os.listdir(chap_folder_locaion))
    images = [
    Image.open(chap_folder_locaion + "\\" + f).convert('RGB')
    for f in os.listdir(chap_folder_locaion)]
    vol = ""
    str = chapter_folders[i]
    if "Vol." in chapter_folders[i]:
        new_str = (str.split("Vol.",1)[1])
        volumes.append(int(new_str.split()[0]))
        vol = ( "_vol.{}" .format(new_str.split()[0]))
    if "Ch." in chapter_folders[i]:
        curr_chapter = (str.split("Ch.",1)[1])
        curr_chapter = curr_chapter.strip()
    pdf_path = chap_pdf_location + ("\\{}_Chapter_{}{}.pdf" .format(Title, curr_chapter,vol))
    try:
        images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
    except:
        print("chapter {} failed to compile".format(i))
#_________________________________________________________



chap_premerge = os.listdir(chap_pdf_location)

chap_dict = {}

for i in range (0, len(chap_premerge)):
    chap_dict[chap_premerge[i]] = chap_premerge[i].split(".")[1]
print("chapters_sorted [/]")



with open(folder_2_location + "\\Data.txt", 'w') as f:
    f.write('Variables (if main crashes)\n volumes: {},\n chaptdict: {},\n chap_pdf_location: {},\n Title: {},\n chap_premerge {},\n folder: {},\n folder_2_location: {}'.format(volumes, chap_dict, chap_pdf_location, Title, chap_premerge, folder, folder_2_location))



"""
os.chdir(chap_pdf_location)
import fitz

for i in range (0,max(volumes)):
    result_1 = fitz.open()

    chap_merging = [k for k, v in chap_dict.items() if v == str(i + 1)]
    for pdf in chap_merging:
        with fitz.open(pdf) as mfile:
            result_1.insert_pdf(mfile)
        
    result_1.save("Volume_{}.pdf".format(i + 1))
"""

