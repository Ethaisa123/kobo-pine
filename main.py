import os
import shutil
from secoundary import volumes, chap_dict, chap_pdf_location, Title, chap_premerge, folder
import fitz
#python -m pip install --upgrade pymupdf
vol_folder = Title + "_volumes"
os.chdir("../kobo-pine")
os.mkdir(vol_folder)

if sum(volumes) == 0:
    os.chdir(chap_pdf_location)
    result_1 = fitz.open()
    for pdf in chap_premerge:
        with fitz.open(pdf) as mfile:
            result_1.insert_pdf(mfile)
    os.chdir("../../..")
    os.chdir(vol_folder)
    result_1.save("no_volume_{}.pdf".format(Title))
    print("Volumes not named, finished normaly.")
    os.chdir("..")
    shutil.rmtree(folder)
    exit()

for i in range (0,max(volumes)):
    os.chdir(chap_pdf_location)
    result_1 = fitz.open()
    chap_merging = [k for k, v in chap_dict.items() if v == str(i + 1)]
    for pdf in chap_merging:
        with fitz.open(pdf) as mfile:
            result_1.insert_pdf(mfile)
    os.chdir("../../..")
    os.chdir(vol_folder)
    result_1.save("Volume_{}.pdf".format(i + 1))
print("Volumes_condensed [/]")
print("finished normaly")
os.chdir("..")
shutil.rmtree(folder)