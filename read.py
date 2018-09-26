import pathlib
import sys
from xml.dom import minidom


def read_version(path):
    dp = pathlib.Path(path)
    container = {}
    for f in sorted(i for i in dp.iterdir() if i.match("*.kext") and i.is_dir()):
        # print(f.name)
        with minidom.parse(str(f) + "/Contents/Info.plist") as doc:
            items = doc.getElementsByTagName('dict')
            d = items[0]
            keys = [i.firstChild.data for i in d.getElementsByTagName("key")]
            vals = [i.firstChild.data for i in
                    d.getElementsByTagName("string")]
            pairs = dict(zip(keys, vals))
            # print(pairs["CFBundleShortVersionString"])
            container[f.name] = pairs["CFBundleShortVersionString"]
    return container


def pretty_print(container):
    max_key_number = len(max(container.keys(), key=lambda x: len(x))) + 2
    for k, v in container.items():
        k = k.ljust(max_key_number, ' ')
        print(k, end="")
        print(v)


if __name__ == "__main__":
    path = "."
    if len(sys.argv) > 1:
        path = sys.argv[1]
    container = read_version(path)
    pretty_print(container)
