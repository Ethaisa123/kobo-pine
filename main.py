import os
import shutil
from secoundary import volumes, chap_dict, chap_pdf_location, Title, chap_premerge, folder, oneshot_
import fitz
vol_folder = Title + "_volumes"
#creates a folder for the volumes in the main directory (if there alread is one it deletes it)
try:
    os.mkdir(vol_folder)
except:
    FileExistsError
    shutil.rmtree(vol_folder)
    os.mkdir(vol_folder)
#stores the main directory location (becuase we change directories a lot after this)
main_dirct = os.getcwd()
#if the manga itself is detected as a single oneshot, it doesnt merge anything and adds the oneshot chapter to the volumes folder
if oneshot_ == True:
    os.chdir(main_dirct)
    print(chap_pdf_location + ("\\{}_Oneshot.pdf" .format(Title)))
    shutil.move(chap_pdf_location + ("\\{}_Oneshot.pdf" .format(Title)), vol_folder)
    print("condensing chapters [/]")
    print("Oneshot detected, finished normaly [/]")
    os.chdir(main_dirct)
    shutil.rmtree(folder)
    exit()
#if no volumes are detected and its not a oneshot then the program asks if you want to merge the volumes 
# (you might not want to if its a webcomic for example)
if sum(volumes) == 0:
    if input("Do you want to add all chapters into a single file? (y/n) :  ") == "n":
        shutil.move(chap_pdf_location, main_dirct)
        shutil.rmtree(folder)
        shutil.rmtree(vol_folder)
        exit()
    print("condensing chapters [/]")
    os.chdir(main_dirct)
    os.chdir(chap_pdf_location)
    result_1 = fitz.open()
    for pdf in chap_premerge:
        with fitz.open(pdf) as mfile:
            result_1.insert_pdf(mfile)
    os.chdir(main_dirct)
    os.chdir(vol_folder)
    result_1.save("no_volume_{}.pdf".format(Title))
    print("Volumes not named, finished normaly [/]")
    os.chdir(main_dirct)
    shutil.rmtree(folder)
    exit()

#if volumes are detected but some of them arent assigned or they are assigned as 0 they are merged 
# (this is for if there are some chapters that arent assigned volumes yet)
# some issues that could arise are if there is a oneshot and some chapters that havent been assigned yet
# this could add the oneshot to the start of the chapter which could be a bit weird
if "" or "0" in volumes:
    os.chdir(main_dirct)
    os.chdir(chap_pdf_location)
    chap_merging = [k for k, v in chap_dict.items() if v == ("0") or ("")]
    for pdf in chap_merging:
        with fitz.open(pdf) as mfile:
            result_1.insert_pdf(mfile)
    os.chdir(main_dirct)
    os.chdir(vol_folder)
    print("condensing chapters without a volume [/]")
    result_1.save("Volume_{}.pdf".format("0"))
"""
 the way this works is the volumes are stored as a list of all the volumes from all the chapters eg: [0,0,0,1,1,1,1,2,2,2,2,3,3,3].
this means that we are able to find the total ammount of volumes even if they are out of order or some are weird.
after the ammount of volumes is found (using a max() funct) the directory is changed to the TITLE_volume 
folder (where the final volumes are stored).
then chapters are merged in "chap_merging" (in dict format eg: {"chapt_name: 0}) for loop goes through each volume and any chapters
with the same volume key are merged into a single list of all the chapter pdfs, then the pdfs with the same volume are each opened
one by one in the next for loop and then saved with the format TITLE_Vol.VOLUME.pdf
"""
for i in range (0,max(volumes)):
    os.chdir(main_dirct)
    os.chdir(chap_pdf_location)
    result_1 = fitz.open()
    chap_merging = [k for k, v in chap_dict.items() if v == str(i + 1)]
    for pdf in chap_merging:
        with fitz.open(pdf) as mfile:
            result_1.insert_pdf(mfile)
    os.chdir(main_dirct)
    os.chdir(vol_folder)
    print("condesning chapters in volume {} [/]".format(i + 1))
    result_1.save("{}_Vol.{}.pdf".format(Title, i + 1))
print("Volumes_condensed [/]")
print("finished normaly [/]")
#deletes unnessicary folders
os.chdir(main_dirct)
shutil.rmtree(folder)