import sys
import xml.etree.ElementTree as ET


MAL_EXPORT_FILE = 'mal_export.xml'
HUMMINGBIRD_EXPORT_FILE = 'hummingbird_export.xml'

def main():
    mal_tree = ET.parse(MAL_EXPORT_FILE)
    mal_root = mal_tree.getroot()
    
    hm_tree = ET.parse(HUMMINGBIRD_EXPORT_FILE)
    hm_root = hm_tree.getroot()
    
    mal_info = mal_root.find('myinfo')
    hm_info = hm_root.find('myinfo')
    
    for info in mal_info:
        hm_el = hm_info.find(info.tag)
        if hm_el is not None:
            print 'Updating {}: {} -> {}'.format(info.tag, hm_el.text, info.text)
            hm_info.find(info.tag).text = info.text
    
    
    mal_animes = mal_root.findall('anime')
    hm_animes = hm_root.findall('anime')
    
    for mal_anime in mal_animes:
        mal_id = mal_anime.find('series_animedb_id').text
        mal_score = mal_anime.find('my_score').text
        
        for hm_anime in hm_animes:
            hm_el = hm_anime.find('series_animedb_id')
            if hm_el is not None and hm_el.text == mal_id:
                hm_score = hm_anime.find('my_score').text = mal_score
    
    hm_tree.write(HUMMINGBIRD_EXPORT_FILE)

if __name__ == '__main__':
    sys.exit(main())