# coding:utf-8
import requests
import re
from xml.dom import minidom

url = 'https://matterhorn.dce.harvard.edu/search/series.json?action=get&admin=false&episodes=true&id=20160114328&limit=400&offset=0&reFreshData=1496297'
content = requests.get(url)

# WHAT COMES BACK IS JSON FILE.WHAT WE WANT IS STORED IN VARIABLE "result"
contentjson = content.json()
result = contentjson['search-results']['result']


print len(result)
# HAVE A LOOK AT ONE OF THEM
result0 = result[6]

# THESE TWO VARAIBLES ARE USED TO FILTER THE URLS WHICH ARE CORRESPONDING TO EACH LECTRUE
preter = u'presenter_delivery.mp4'
pretion = u'presentation_delivery.mp4'


# FUNCTION TO TANSFORM EACH RESULT INTO A XML FILE 
def write_xml(x = rexml):
    f = file(r'media.xml', 'w')
    f.write(x)
    f.close()
# FUNCTION TO GET TITLE, URLS FROM EACH JSON RESULT
def get_data():
    urllist = []
    mp4list = []
    mp4Preter = []
    mp4Pretion = []
    headerlist = []
    # FILE TO BE PARSED
    dom = minidom.parse("media.xml")
    collection = dom.documentElement
    
    # GET TITLE ELEMENT AND DATA
    titleEle = collection.getElementsByTagName("title")[0]
    title = titleEle.childNodes[0].data

    # GET URL ELEMENT. ACTUALLY, URL ELEMENT CONTAINS A LOT OF URLS NEEDED TO BE ELIMINATED, LIKE ".xml"，".jpg" ——WHICH IS USELESS
    urlEle = collection.getElementsByTagName("url")

    # urllist = [url.childNodes[0].data for url in urllist]
    for url in urlEle:
        urldata = url.childNodes[0].data
        urllist.append(urldata)
    
    # ELIMINATE ALL THE USELESS URLS AND LEAVE ".MP4". mp4list CONTAINS ALL THE ".mp4" URLS.
    for i in urllist:
        boolmp4 = re.search('.mp4', i, re.IGNORECASE)
        if boolmp4:
            mp4list.append(i)
    
    # EXTRACT URLS WHICH ARE ENDED WITH "presenter_delivery.mp4" or "presentation_delivery.mp4". IN OTHER CASES, headerlist IS USED TO STORE A BASI URL FOR THE LECTURE
    for i in mp4list:
        boolTer = re.search(preter, i, re.IGNORECASE)
        boolTion = re.search(pretion, i, re.IGNORECASE)
        if boolTer:
            mp4Preter.append(i)
        elif boolTion:
            mp4Pretion.append(i)
        else:
            headerlist.append(i)

    # RETURN TITLE AND URLS 
    if len(headerlist) != 0:
        return title, headerlist[0]
    elif (len(mp4Pretion) != 0):
        return title, mp4Preter[0], mp4Pretion[0]
    else:
        return title, mp4Preter[0]

# FUNCTION TO WRITE TITLE,URLS TO TXT FILE
def data_to_doc(data):
    doc = file(r"data.txt", 'a')
    for i in range(0, len(data)):
        doc.write(str(data[i]))
        doc.write('\n')
    doc.write('\n')
    doc.close()

# MAIN FUNCTION
a = u'ocMediapackage'
for result0 in result:
    if a in result0.keys():
    	# TITLE AND URLS ARE STORED IN AN XML FILE
        rexml = result0['ocMediapackage']
        write_xml(rexml)
        data = get_data()
        data_to_doc(data)
    else:
        pass