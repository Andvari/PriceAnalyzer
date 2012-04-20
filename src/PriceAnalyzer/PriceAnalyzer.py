'''
Created on 21.12.2011

@author: nemo
'''
import urllib2, re

def Ulmart():
    cookies = ""
    while(cookies == ""):
        req = urllib2.Request('http://www.ulmart.ru') 
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; windows NT 5.1; en-GB; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3)')
        response = urllib2.urlopen(req)
        headers  = response.info()
        try:
            cookies = headers["Set-Cookie"]
        except:
            pass

    log = open("C:\\User\\Shu\\tmp\\Ulmart.txt", "w")
    cookies = cookies + "; city=321"    
    req = urllib2.Request('http://www.ulmart.ru/tvs/?filter_active=1&r=1__75074%3B1__81419%3B5__1&nav_type=super&search_q=&highlight=&menu_type=&group_vend=&group_class=&orderby=retail_price&orderdir=asc&filter%5Bcurrency%5D=rur&filter%5Bconvert_currency%5D=0&filter%5Bscroll_count%5D=4&scroll_page=4&filter%5Bgroup%5D=-1&filter%5Bquery%5D=&go_search=1') 
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; windows NT 5.1; en-GB; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3)')
    req.add_header('Cookie', cookies)
    response = urllib2.urlopen(req)
    page = response.read()

    page = page.replace("\n", "")
    fragment = page[page.find("listed_from_to") : page.find("pages_nums")]
    fragment = fragment[fragment.rfind('bold;">')+7 : fragment.rfind("</span>")]
    num_pages = int(fragment)/15+1

    for i in xrange(num_pages):
        req = urllib2.Request('http://www.ulmart.ru/tvs/?filter_active=1&r=1__75074%3B1__81419%3B5__1&nav_type=super&search_q=&highlight=&menu_type=&group_vend=&group_class=&orderby=retail_price&orderdir=asc&filter%5Bcurrency%5D=rur&filter%5Bconvert_currency%5D=0&filter%5Bscroll_count%5D=4&scroll_page=' + str(i+1) + '&filter%5Bgroup%5D=-1&filter%5Bquery%5D=&go_search=1') 
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; windows NT 5.1; en-GB; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3)')
        req.add_header('Cookie', cookies)
        response = urllib2.urlopen(req)
        page = response.read()
        page = page.replace("\n", "")
        items = re.compile('catalogItem.+?} " >.*?(BBK|Cameron LVD|Cameron|Erisson|Hyundai|Izumi|LG|MYSTERY|Panasonic VIERA|Panasonic|Philips|Rolsen|Rubin|RUBIN|Samsung|Sharp AQUOS|Sharp|Sony BRAVIA|Sony|SOUNDMAX|SoundMAX|Supra|Thomson|Toshiba Regza|Toshiba|Varta) ([A-Z0-9-/ ]*?)(</a>| |,).+?ptHide\(\)"><span>(.+?)<span').findall(page)
        for item in items:
            vendor = str.upper(item[0])
            pos = vendor.find(" ")
            if(pos>=0): vendor = vendor[:pos]
            model = item[1]
            cost  = item[3]
            ulmart[vendor + " " + model] = cost
            
            log.write(vendor + "\t")
            if len(vendor)<8: log.write("\t")
            log.write(model + "\t")
            if len(model)<8:  log.write("\t")
            log.write(cost + "\n")
                                        
        print "Page " + str(i+1) + " of " + str(num_pages) + " processed"
    log.close()        
        
def Citilink():
    """
    req = urllib2.Request('http://www.citilink.ru/catalog/audio_and_digits/tv/?p=1') 
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; windows NT 5.1; en-GB; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3)')
    req.add_header('Cookie', 'citilink_space=nnov_cl')

    response = urllib2.urlopen(req)
    page = response.read()
    num_pages = int(page[page.rfind("?p=")+3 : page.rfind("?p=")+5 ])

"""
    num_pages=1
    for i in xrange(num_pages):
        """
        print i
        req = urllib2.Request('http://www.citilink.ru/catalog/audio_and_digits/tv/?p='+str(i+1+5)) 
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; windows NT 5.1; en-GB; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3)')
        req.add_header('Cookie', 'citilink_space=nnov_cl')
        response = urllib2.urlopen(req)
        page = response.read()
        """
        page = src.read()
        page = page.replace("\n","")
        page = page.replace("&nbsp;", " ")
        page = page.replace("&laquo;", "<")
        page = page.replace("&raquo;", ">")
        page = page.replace(" <R>", "")
        page = page.replace("<R>", "")

        #items = re.compile('class="photo".*?(BBK Ego|BBK Lumino|SUPRA.*?|ACER|GOLDSTAR|BBK|CAMERON LVD|CAMERON|ERISSON|HYUNDAI|IZUMI|LG|MYSTERY|PANASONIC VIERA|PANASONIC|PHILIPS|ROLSEN|RUBIN|SAMSUNG|SHARP AQUOS|SHARP|SONY BRAVIA|SONY|SOUNDMAX|SoundMAX|SUPRA Kobe|SUPRA Miyazaki|SUPRA Kyoto|SUPRA Yokohama|SUPRA|THOMSON|TOSHIBA Regza|TOSHIBA|VARTA) ([A-Z0-9-/ ]*?)(</a>| |,).+?price.txt.+?>(.+?)<span').findall(page)
        items = re.compile('class="photo".*?(BBK Ego|BBK Lumino|SUPRA|ACER|GOLDSTAR|BBK|CAMERON LVD|CAMERON|ERISSON|HYUNDAI|IZUMI|LG|MYSTERY|PANASONIC VIERA|PANASONIC|PHILIPS|ROLSEN|RUBIN|SAMSUNG|SHARP AQUOS|SHARP|SONY BRAVIA|SONY|SOUNDMAX|SoundMAX|THOMSON|TOSHIBA Regza|TOSHIBA|VARTA).*? ([A-Z0-9-/ ]*?)(</a>| |,).+?price.txt.+?>(.+?)<span').findall(page)

        for item in items:
            vendor = str.upper(item[0])
            pos = vendor.find(" ")
            if(pos>=0): vendor = vendor[:pos]
            model = item[1]
            cost  = item[3]
            citilink[vendor + " " + model] = cost
            
            print vendor + " " + model + " " + cost
            
            log.write(vendor + "\t")
            if len(vendor)<8: log.write("\t")
            log.write(model + "\t")
            if len(model)<8:  log.write("\t")
            log.write(cost + "\n")
                                        
        #print "Page " + str(i+1) + " of " + str(num_pages) + " processed"

log = open("C:\\User\\Shu\\tmp\\Citilink.txt", "w")
src = open("C:\\User\\Shu\\Citilink.htm", "r")

citilink = {}
ulmart = {}

Citilink()

