import json

with (
    open("purchase_log.txt", "r", encoding="utf-8") as file_with_ID_and_category,
    open("visit_log (2).csv", "r", encoding="utf-8") as file_with_ID_and_source,
    open("funnel.csv", "w", encoding="utf-8") as result_file,
):
    purchases = dict()

    for line in file_with_ID_and_category:
        a = json.loads(line)
        purchases[a["user_id"]] = a["category"]

    for line in file_with_ID_and_source:
        user_id, source = line.strip().split(",")
        if user_id in purchases:
            result_file.write(f"{user_id},{source},{purchases[user_id]} \n")
