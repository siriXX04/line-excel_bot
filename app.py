branch = ""
status = ""
detail = ""

for line in msg.split("\n"):

    if line.startswith("สาขา:"):
        branch = line.replace("สาขา:", "").strip()

    elif line.startswith("สถานะ:"):
        status = line.replace("สถานะ:", "").strip()

    elif line.startswith("รายละเอียด:"):
        detail = line.replace("รายละเอียด:", "").strip()

print("สาขา =", branch)
print("สถานะ =", status)
print("รายละเอียด =", detail)
