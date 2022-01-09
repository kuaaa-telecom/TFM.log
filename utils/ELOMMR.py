import json
import sys, os


def convert(index, record):
    row = record.strip().split("\n")
    return json.dumps({
        "name": f"{base}.R{index}",
        # Ignore this timestamp paramteter
        "time_seconds": index,
        "standings": [[data.split(" ")[0], rank, rank] for rank, data in enumerate(row)]
    }, ensure_ascii = False, indent=4)

filename = sys.argv[1]
base = filename.split(".")[0]
raw = open(filename, 'r').read()
if not os.path.exists(base):
    os.mkdir(base)
records = raw.split("\n\n")

for index, record in enumerate(records):
    rec_json = convert(index, record)
    # I believe GC will do the job
    open(f'{base}/{index}.json', 'w').write(rec_json)

