from re import M
import mangadex
api = mangadex.Api()

title = "Dungeon Meshi"#input("title: ")
#gets the info for the manga chosen by title
manga_list = api.get_manga_list(title = title)
m_list = manga_list[0] # chooses the first version (english i think?)
print(m_list.title)

#gets all the chapter and volume information (we only need the chapter id's and names)
m_chapters_all = api.get_manga_volumes_and_chapters(manga_id = m_list.manga_id)

""" SOMEHOW TURN THIS MASIVE DICTIONARY INTO USABLE CHAPTER IDS WITH NAMES"""
#sets up the final dict with all the ids
chapt_names_ids = {}

vol_names_ids = {}
#finds the names for all the volumes
volume_names = list(m_chapters_all.keys())

for i in range (0, len(volume_names)):
    #gets all the information for chapters from the big list
    chapters_in_volume = m_chapters_all[volume_names[i]]["chapters"]
    #gets all the names for the volumes for the lists
    chapter_names = list(chapters_in_volume.keys())

    for i in range (0, len(chapter_names)):
        #gets the chapter name
        chap = chapter_names[i]
        #gets the chapter information to ids
        chapt_dict_ids = chapters_in_volume[str(chap)]
        #finds the ids from the dict using the key "id"
        chapt_ids = chapt_dict_ids["id"]
        #adds the names and ids to an easy to acess dictionary
        chapt_names_ids[chap] = chapt_ids


#gets the cahpter information with the list of chapter id's created previosly
m_chapter = api.get_chapter(chapter_id = chapt_names_ids["20"])

#gets all the page images from the chosen chapter
m_pages = m_chapter.fetch_chapter_images()
print(m_pages)
