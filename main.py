import os
import shutil
from secoundary import volumes, chap_dict, chap_pdf_location, Title, chap_premerge, folder, oneshot_
import fitz
#python -m pip install --upgrade pymupdf
vol_folder = Title + "_volumes"
try:
    os.mkdir(vol_folder)
except:
    FileExistsError
    shutil.rmtree(vol_folder)
    os.mkdir(vol_folder)

main_dirct = os.getcwd()

#condenses all chapters into a single file if no 
if oneshot_ == True:
    os.chdir(main_dirct)
    print(chap_pdf_location + ("\\{}_Oneshot.pdf" .format(Title)))
    shutil.move(chap_pdf_location + ("\\{}_Oneshot.pdf" .format(Title)), vol_folder)
    print("condensing chapters [/]")
    print("Oneshot detected, finished normaly [/]")
    os.chdir(main_dirct)
    shutil.rmtree(folder)
    exit()

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


#if there are volumes in this manga but some of the chapters arent in a volume this code condenses the chapters that arent in a volume into a single file
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

#this code condenses all the chapters from the same volume into a single file
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
os.chdir(main_dirct)
#deletes extra stuff
shutil.rmtree(folder)