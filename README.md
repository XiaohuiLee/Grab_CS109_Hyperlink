# grab_CS109_hyperlink
Using python (requests\re\xml) to grab the download hyperlink for CS109 courses of Harvard

The main page for CS109 locates in http://cs109.github.io/2015/index.html.


The courses list is posted here: https://matterhorn.dce.harvard.edu/engage/ui/index.html#/2016/01/14328

This grabber is using Python, basically to extract the download link for the mp4s for each lesson. No offense.

By using Chrome's web development kit (Press button F12), file transfered from server is observed as a "GET" method. So using requests library to ask for sources and using innate json library to parse the package returned.
Information is stored in an wrapped xml piece which is laterly stored in an xml file. Then xml.dom is used to parse the xml file.



data.txt stores all the urls (Programme outputs) for CS109.
media.xml is a intermediate file to store informatin for each course.
