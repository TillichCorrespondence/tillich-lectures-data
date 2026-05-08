import glob
import json
import os

from acdh_tei_pyutils.tei import TeiReader

files = sorted(glob.glob("./data/additional/*.xml"))

data = {}

for i, x in enumerate(files, start=1):
    doc = TeiReader(x)
    transkribus_id = doc.any_xpath(".//tei:idno[@type='transkribus_doc_id']/text()")[0]
    title = doc.any_xpath(".//tei:title")[0].text
    data[transkribus_id] = {
        "title": title,
        "order": i,
        "file_name": os.path.split(x)[-1],
    }

with open("title.json", "w", encoding="utf-8") as fp:
    json.dump(data, fp, indent=2, ensure_ascii=False)
