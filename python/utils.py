def parse_line(line):
    parts = line.split(",")

    uid = None
    status = None

    for part in parts:
        if part.startswith("UID:"):
            uid = part.replace("UID:", "").strip()
        elif part.startswith("STATUS:"):
            status = part.replace("STATUS:", "").strip()

    return uid, status