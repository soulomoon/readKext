import pathlib
import os
import sys
from xml.dom import minidom

if __name__ == "__main__":
    path = "."
    if len(sys.argv)>1: 
        path = sys.argv[1]

    dp = pathlib.Path(path)
    for f in sorted(list(dp.iterdir())):
        if f.match("*.kext"):
            if not f.is_dir():
                continue
            print(f.name)
            for content in f.iterdir():
                if not content.is_dir():
                    continue
                for info in content.iterdir():
                    if info.match("Info.plist"):
                        try:
                            with info.open() as fp:
                                doc = minidom.parse(fp)
                                items = doc.getElementsByTagName('dict')
                                d = items[0]
                                keys = [i.firstChild.data for i in d.getElementsByTagName("key")]
                                vals = [i.firstChild.data for i in
                                        d.getElementsByTagName("string")]
                                pairs = dict(zip(keys, vals))
                                print(pairs["CFBundleShortVersionString"])
                        except:
                            print("some error happen")
