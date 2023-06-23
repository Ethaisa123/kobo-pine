#py -3 -m pip install mangadex-downloader
import mangadex_downloader
import os
from PIL import Image
import shutil


#asks user for manga and creates first directory
print("welcome")
Title = input("     : What manga would you like to search for \n     : ")
folder = (Title + "_raws")
"""
Everything downloaded (manga images) and combined (manga images combined into pdfs) is done in the "folder" directory
this direcotry is created to make it easier to navigate, the directory is named the title that the user searches for + "_raws"
if the user missplells the name of the manga the directory will also be misspelled, this doesent really matter though because
the directory is deleted before the program finishes (although if there is an error and the program stops the folder will stick
around with the very useful "data.py" file)

"""
#checks wether the folder where the manga is going to be created exists 
#(this was more useful when the program didnt automaticaly delete the "folder" directory when the program finished)
try:
    os.mkdir(folder)
except:
    print("     : Manga already exists! [X]")
    if input("     : Overwrite? (y/n)\n     : ") == ("y" or "Y"):
        shutil.rmtree(folder)
        os.mkdir(folder)
    else:
        shutil.rmtree(folder)
        exit()
#this api made avalible by mansuf is a lifesaver please check his github it is amazing https://github.com/mansuf/mangadex-downloader
"""
when mangadex-dl downloads a manga it sorts each chapter into a file named "[TRANSLATOR] ch. vol."
in this file is a number of images from the chapter labled as the page_number.png/jpg

"""
os.system('mangadex-dl "{}" --search --folder "{}" ' .format(Title,folder))
#this locates the folder created by mangadex-dl
try:
    folder_2_location = (folder + "\\{}" .format(os.listdir(folder)[0]))
except IndexError:
    print("     : Manga does not exist")
    shutil.rmtree(folder)
    exit()
#creates a list of all the volumes (this could probably be a variable but keeping it a list is safer)
volumes = []
#this variable stores the names of all the folders that contain the chapter images
chapter_folders = os.listdir(folder_2_location)

#copies the cover into the first chapter (so that the thumbnail will look nicer) also removes the extra files
chapter_folders.remove("cover.jpg")
chapter_folders.remove("download.db")
print(chapter_folders)
chapter_folders.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
shutil.copyfile(folder_2_location + "\\cover.jpg", (folder_2_location + "\\{}\\cover.jpg".format(chapter_folders[0])))
print("file_system [/]")
#creates the chapters folder for all of the chapter pdfs to be stored (the next line stores where the folder is kept)
os.mkdir(folder_2_location + "\\{}_chapters" .format(Title))
chap_pdf_location = (folder_2_location + "\\{}_chapters" .format(Title))
"""
this massive for-loops job is to go through every chapter folder and combine all of the images
into a pdf, the pdfs are saved to the TITLE_chapters folder
"""
for i in range (0, (len(chapter_folders))):
    #stores the location of where the output file will be saved
    chap_folder_locaion = (folder_2_location + "\\{}".format(chapter_folders[i]))
    #the image_list variable is a replacement for os.listdir(chap_folderlocation) so that 
    # i can add or remove the cover image for a given chapter
    image_list = os.listdir(chap_folder_locaion)
    if "cover.jpg" in image_list:
        image_list.remove("cover.jpg")
    #if the volume and the chapter are both 1 it adds the cover to it (also if it is a oneshot)
    # this is just incase the first page is a translator page 
    if "Vol. 1 Ch. 1" in chapter_folders[i]:
        if (chapter_folders[i].split("Vol. 1 Ch. 1")[1] == "") == True:
            image_list.insert(0, "cover.jpg")
    elif "Oneshot" in chapter_folders[i]:
        image_list.insert(0, "cover.jpg")
    #this opens all of the images from the chapter folder into a list and then converts them 
    # into a format that can be saved be pillow
    images = [
    Image.open(chap_folder_locaion + "\\" + f).convert('RGB')
    for f in image_list]
    vol = ""
    str = chapter_folders[i]
    #saves the volumes to a list that can be used later by a dictionary to save the volumes properly
    if "Vol." in chapter_folders[i]:
        new_str = (str.split("Vol.",1)[1])
        volumes.append(int(new_str.split()[0]))
        vol = ( "vol.{}" .format(new_str.split()[0]))
    #sets the chapter to the actual chapter not the placement in the list
    if "Ch." in chapter_folders[i]:
        curr_chapter = (str.split("Ch.",1)[1])
        curr_chapter = curr_chapter.strip()
    #sets the destination and name of the output pdf file 
    if len(chapter_folders) < 2 and "Oneshot" in chapter_folders[i]:
        curr_chapter = "Oneshot"
        pdf_path = chap_pdf_location + ("\\{}_Oneshot.pdf" .format(Title))
    elif "Oneshot" in chapter_folders[i]:
        curr_chapter = "Oneshot"
        pdf_path = chap_pdf_location + ("\\{}_Oneshot__0.1__.pdf" .format(Title))
    else:
        pdf_path = chap_pdf_location + ("\\{}_Chapter__{}__{}.pdf" .format(Title, curr_chapter,vol))
    #saves the pdf file
    try:
        images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
    except:
        print("chapter {} failed to compile [X]".format(curr_chapter))
    print("chapter {} compiled [/]".format(curr_chapter))
#if the chapter has 1 oneshot chapter the IndexError is triggered and the volume is marked as a oneshot
oneshot_ = False
try:
    chap_premerge = os.listdir(chap_pdf_location)
    print("chapters found [/]")
    chap_premerge = sorted(chap_premerge, key = lambda x: float(x.split("__")[1]))
    print("chapters sorted [/]")
except IndexError:
    print("This either a oneshot or somthing has gone wrong [/]")
    oneshot_ = True
chap_dict = {}
#sets the chapt dict to help mark which chapters merge into what volume
for i in range (0, len(chap_premerge)):
    try:
        chap_dict[chap_premerge[i]] = (chap_premerge[i].split("vol.")[1].strip(".pdf"))
    except IndexError:
        print("volume not found when sorting [{}]".format(chap_premerge[i]))
        volumes.append(0)
        chap_dict[chap_premerge[i]] = "0"
#makes sure volumes list only has intagers
volumes = list(map(int, volumes))
print("chapters_sorted [/]")
#creates a data file incase of a crash (bug testing purposes)
with open(folder_2_location + "\\Data.py", 'w') as f:
    f.write('#Variables (if main crashes)\noneshot_ = {}\nvolumes = {}\nchaptdict = {}\nchap_pdf_location = "{}"\nTitle = "{}"\nchap_premerge = {}\nfolder = "{}"\nfolder_2_location = "{}"'.format(oneshot_,volumes, chap_dict, chap_pdf_location, Title, chap_premerge, folder, folder_2_location))



