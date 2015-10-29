from warc_parser import process_warc

#Read in warc files for abcnews.go.com/us/weather/wirestory?id=7166541
warc_files = []
with open("test/1441_uri.csv", "r") as f:
    f.next()
    for line in f:
        warc_potential = line.split()[-1]
        if warc_potential[-7:] == "warc.gz":
            warc_files.append(warc_potential[:-3])

warc_directory = "C:/_Kayla/phd_research/data/unzipped/"
header_files = []
for warc_file in warc_files:
    warc_path = warc_directory + warc_file
    try:
        header_file = process_warc(warc_path)
        header_files.append(header_file)
    except:
        print "Could not process " + warc_file

records = []
for header_file in header_files:
    with open(header_file, "r") as f:
        record = {}
        for line in f:
            if line != "\n":
                if line[:len("WARC/")] == "WARC/":
                    record["WARC-Version"] = line[:-1]
                else:
                    record[line[:line.index(":")]] = line[line.index(":")+2:-1]
            else:
                records.append(record)
                record = {}

target_uri = "http://abcnews.go.com/us/weather/wirestory?id=7166541"
for record in records:
    try:
        uri = record["WARC-Target-URI"]
        print uri
        if record["WARC-Target-URI"][:len(target_uri)] == target_uri:
            print record
    except:
        pass
