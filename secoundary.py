#py -3 -m pip install mangadex-downloader
import mangadex_downloader
import os
from PIL import Image
import shutil
print("welcome")
Title = input("what manga would you like to search for \n   :  ")
folder = (Title + "_raws")
#_________________________________________________________
     
try:
    os.mkdir(folder)
except:
    print("manga already exists! [X]")
    if input("delete manga? (y/n)\n   :  ") == "y":
        shutil.rmtree(folder)
        os.mkdir(folder)
    else:
        exit()

os.system('mangadex-dl "{}" --search --folder "{}" ' .format(Title,folder))
print("---------------------------------------------------------------------")
folder_2_location = (folder + "\\{}" .format(os.listdir(folder)[0]))
volumes = []
chapter_folders = os.listdir(folder_2_location)

shutil.copyfile(folder_2_location + "\\cover.jpg", (folder_2_location + "\\{}\\cover.jpg".format(chapter_folders[-1])))
chapter_folders.remove("cover.jpg")
chapter_folders.remove("download.db")
print("file_system [/]")
#_________________________________________________________
os.mkdir(folder_2_location + "\\{}_chapters" .format(Title))
chap_pdf_location = (folder_2_location + "\\{}_chapters" .format(Title))
for i in range (0, (len(chapter_folders))  ):
    
    chap_folder_locaion = (folder_2_location + "\\{}".format(chapter_folders[i]))
    image_list = os.listdir(chap_folder_locaion)
    image_list.remove("cover.jpg")
    if "Vol." in chapter_folders[i]:
        if str.split("Vol.",1)[1] == 1:
            image_list.insert(0, "cover.jpg")
    elif "Oneshot" in chapter_folders[i]:
        image_list.insert(0, "cover.jpg")
    
    images = [
    Image.open(chap_folder_locaion + "\\" + f).convert('RGB')
    for f in image_list]
    print(images)
    vol = ""
    str = chapter_folders[i]
    if "Vol." in chapter_folders[i]:
        new_str = (str.split("Vol.",1)[1])
        volumes.append(int(new_str.split()[0]))
        vol = ( "_vol.{}" .format(new_str.split()[0]))
    if "Ch." in chapter_folders[i]:
        curr_chapter = (str.split("Ch.",1)[1])
        curr_chapter = curr_chapter.strip()
    if "Oneshot" in chapter_folders[i]:
        curr_chapter = "Oneshot"
        pdf_path = chap_pdf_location + ("\\{}_Oneshot.pdf" .format(Title))
    else:
        pdf_path = chap_pdf_location + ("\\{}_Chapter__{}__{}.pdf" .format(Title, curr_chapter,vol))
    try:
        images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
    except:
        print("chapter {} failed to compile [X]".format(curr_chapter))
    print("chapter {} compiled [/]".format(curr_chapter))
#_________________________________________________________


try:
    chap_premerge = os.listdir(chap_pdf_location)
    print("chapters found [/]")
    chap_premerge = sorted(chap_premerge, key = lambda x: float(x.split("__")[1]))
    print("chapters sorted [/]")
except IndexError:
    print("This either a oneshot or somthing has gone wrong [/]")
    oneshot_ = True
chap_dict = {}

for i in range (0, len(chap_premerge)):
    try:
        chap_dict[chap_premerge[i]] = chap_premerge[i].split("_vol.")[1]
    except IndexError:
        print("volume not found when sorting [-]")
        chap_dict[chap_premerge[i]] = 0
print("chapters_sorted [/]")



with open(folder_2_location + "\\Data.py", 'w') as f:
    f.write('#Variables (if main crashes)\nvolumes = {}\nchaptdict = {}\nchap_pdf_location = "{}"\nTitle = "{}"\nchap_premerge = {}\nfolder = "{}"\nfolder_2_location = "{}"'.format(volumes, chap_dict, chap_pdf_location, Title, chap_premerge, folder, folder_2_location))



