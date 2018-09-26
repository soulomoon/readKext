import pathlib
from xml.dom import minidom

dp = pathlib.Path()
for f in dp.iterdir():
    if f.match("*.kext"):
        print(f)
        for content in f.iterdir():
            for info in content.iterdir():
                if info.match("*.plist"):
                    with info.open() as fp:
                        doc = minidom.parse(fp)
                        items = doc.getElementsByTagName('dict')
                        d = items[0]
                        keys = [i.firstChild.data for i in d.getElementsByTagName("key")]
                        vals = [i.firstChild.data for i in
                                d.getElementsByTagName("string")]
                        pairs = dict(zip(keys, vals))
                        print(pairs["CFBundleShortVersionString"])
