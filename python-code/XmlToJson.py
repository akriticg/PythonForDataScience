import xml.etree.ElementTree as ET
import re
import json
import os

data = {}
fieldPostRegex = '\s+:([\S+\n\r\s]*?).*[A-Z].*[A-Z].*\s:'


def xmlToJson(fileName):
    # will convert the entire text into one field
    tree = ET.parse(fileName)
    root = tree.getroot()
    total = 0

    for record in root:

        recordId = record.attrib['ID']
        data[recordId] = {}
        total += 1
        children = record.getchildren()
        if len(children) == 2:
            data[recordId][children[0].tag] = children[0].attrib['STATUS']
        data[recordId][children[len(
            children) - 1].tag] = children[len(children) - 1].text.replace('\n', '')

    nameOfFileWithoutExt = os.path.splitext(fileName)[0]
    jsonFileName = nameOfFileWithoutExt + ".json"

    with open(jsonFileName, "w") as f:
        json.dump(dict(data), f)

    print('done: ' + jsonFileName)
    return jsonFileName