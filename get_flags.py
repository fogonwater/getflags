from bs4 import BeautifulSoup
import urllib, urllib2

# terrible hacks because I am lazy and stretched for time
base_url = 'https://www.govt.nz/'
img_path = '/browse/engaging-with-government/the-nz-flag-your-chance-to-decide/gallery/?start='
NUM_FLAGS = 335

def main():
    start = 1
    img_num = 1
    while start < NUM_FLAGS:
        url = base_url + img_path + str(start)
        html = urllib2.urlopen(url)
        soup = BeautifulSoup(html)

        for img in soup.findAll('img'):
            img_url = img['src']
            if not 'flags-designs' in img_url:
                continue
            dst_name = 'img/' + str(img_num) + img_url[-4:]
            dst_name = dst_name.replace('jpeg', '.jpg')
            urllib.urlretrieve(base_url + img_url, dst_name)
            print dst_name, 'created.'
            img_num += 1
        
        # increment by number of imgs in visible gallery
        start += 9


if __name__ == '__main__':
    main()