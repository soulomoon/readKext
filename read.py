import pathlib
import sys
from xml.dom import minidom

if __name__ == "__main__":
    path = "."
    if len(sys.argv) > 1:
        path = sys.argv[1]

    dp = pathlib.Path(path)
    for f in sorted(i for i in dp.iterdir() if i.match("*.kext") and i.is_dir()):
        print(f.name)
        with minidom.parse(str(f) + "/Contents/Info.plist") as doc:
            items = doc.getElementsByTagName('dict')
            d = items[0]
            keys = [i.firstChild.data for i in d.getElementsByTagName("key")]
            vals = [i.firstChild.data for i in
                    d.getElementsByTagName("string")]
            pairs = dict(zip(keys, vals))
            print(pairs["CFBundleShortVersionString"])
