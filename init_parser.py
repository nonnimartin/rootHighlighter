import json

jsonList = open('./raw-wiktextract-data.json', 'r')
eng_only = open('./eng_only.json', 'a')
for line in jsonList:
    # extract only english language entries
    jsonDict = json.loads(line)
    if "lang_code" not in jsonDict.keys():
        continue
    elif jsonDict["lang_code"] == "en" and "etymology_text" in jsonDict.keys():
        eng_only.write(line)
eng_only.close()


