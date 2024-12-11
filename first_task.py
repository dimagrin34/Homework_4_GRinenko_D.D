import json

purchases = {}

with open("purchase_log.txt", "r", encoding="utf-8") as file_with_ID_and_category:
    for line in file_with_ID_and_category:
        a = json.loads(line)
        purchases[a["user_id"]] = a["category"]

for user_id in purchases:
    if user_id == "user_id":
        continue
    print(user_id, purchases[user_id])
