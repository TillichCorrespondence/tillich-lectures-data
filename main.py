import glob

from acdh_tei_pyutils.tei import TeiReader

to_change = [
    "religion",
    "ultimate_concern",
    "unconscious",
    "biology",
    "monistic_theory",
    "genesis",
    "language",
    "community",
    "church",
    "nation",
    "individualism",
]


def main():
    print("Hello from tillich-lectures-data!")
    files = glob.glob("data/editions/*.xml")
    for x in sorted(files):
        doc = TeiReader(x)
        for y in to_change:
            rs_type = "_".join([y.capitalize() for y in y.split("_")])
            for el in doc.any_xpath(f"tei:{y}"):
                el.tag = "{http://www.tei-c.org/ns/1.0}rs"
                el.attrib["type"] = "keyword"
                el.attrib["type"] = f"#{rs_type}"


if __name__ == "__main__":
    main()
