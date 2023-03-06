from re import M
import mangadex
api = mangadex.Api()

title = "Dungeon Meshi"#input("title: ")
#gets the info for the manga chosen by title
manga_list = api.get_manga_list(title = title)
m_list = manga_list[0] # chooses the first version (english i think?)
print(m_list.title)

#gets all the chapter and volume information (we only need the chapter id's)
m_chapters = api.get_manga_volumes_and_chapters(manga_id = m_list.manga_id)
volumes = list(m_chapters.keys())
""" SOMEHOW TURN THIS MASIVE DICTIONARY INTO USABLE CHAPTER IDS"""
#print(volumes[1])
print(m_chapters["12"]["chapters"][0])

for i in range (0, len(volumes)):
    print(volumes[i])


#gets the cahpter information with the list of chapter id's
m_chapter = api.get_chapter(chapter_id = "015979c8-ffa4-4afa-b48e-3da6d10279b0")

#gets all the page images from the chosen chapter
m_pages = m_chapter.fetch_chapter_images()
