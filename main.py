import glob
from acdh_tei_pyutils.tei import TeiReader


def main():
    print("Hello from tillich-lectures-data!")
    files = glob.glob("data/editions/*.xml")
    for x in sorted(files):
        doc = TeiReader(x)
        print(doc.any_xpath(".//tei:title[@type='main']")[0].text)


if __name__ == "__main__":
    main()
