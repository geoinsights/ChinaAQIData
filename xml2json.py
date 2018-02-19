# coding=utf-8
import json
import geojson
import time
import xml.dom.minidom


def data_from_xml_json(xmlfile):
    fp = open(xmlfile)
    data = fp.read()
    # this is for the air quality data, to split some charicters
    data = data.replace("a:", "")
    data = data.replace("b:", "")
    data = data.replace("c:", "")
    data = data.replace("&mdash", "-")
    return xmlparse(data)


def xmlparse(xmlstr):
    '''
       parse air quality xml data to dict list
    '''
    dom = xml.dom.minidom.parseString(xmlstr)
    root = dom.documentElement
    stats = dom.getElementsByTagName("AQIDataPublishLive")
    airdata = []
    for stat in stats:
        # print len(stat.childNodes)
        r = {}
        for node in stat.childNodes:
            if (node.nodeName == "#text" or
                    node.nodeName == "OpenAccessGenerated"):
                continue
            inx = node.nodeName
            inx = inx.lower()
            for n in node.childNodes:
                # print n.data
                r[inx] = n.data
        airdata.append(r)
    return airdata
    # return json.dumps(airdata, ensure_ascii=False)

if __name__ == "__main__":
    data = data_from_xml_json("data.xml")
    featList = []
    for recd in data:
        try:
            lon = float(recd["longitude"])
            lat = float(recd["latitude"])
        except:
            continue
        geom = geojson.Point((lon, lat))
        del recd["longitude"]
        del recd["latitude"]
        properties = recd
        feat = geojson.Feature(geometry=geom, properties=properties)
        featList.append(feat)
    fc = geojson.FeatureCollection(featList)
    fname = time.strftime("%Y-%m-%d-%H", time.localtime())
    fstr = geojson.dumps(fc, sort_keys=True)
    fp = open("archives/%s.json" % fname, "w")
    fp.write(fstr)
    fp.close()
    fp = open("airnow.json", "w")
    fp.write(fstr)
    fp.close()
