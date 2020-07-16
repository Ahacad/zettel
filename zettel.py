#! /usr/env/bin python3

import re
#import subprocess
import os
import json
# import argparse

class Zettel:

    def __init__(self):
        pass

    def cli(self):
        pass

    def getTagsFromAFile(self, File):
        pattern = r"\[\[[a-zA-Z0-9 ]+]]"
        with open(File, "r") as fil:
            line = "1"
            count = 0
            res = []
            while line:
                line = fil.readline()
                count += 1
                for tag in re.findall(pattern, line):
                    dic = {}
                    dic["fileName"] = File
                    dic["lineNumber"] = count
                    dic["tag"] = tag[2:-2]
                    res.append(dic)
        return res


    def getAllTags(self):
        dics = []
        for fil in os.listdir("."):
            if fil[-2:] == "md":
                dics += getTagsFromAFile(fil)
        return dics


    def safeToJson(self, storagePath, data):
        with open(storagePath, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return 0 


    def loadJson(self, storagePath):
        with open(storagePath) as json_file:
            res = json.load(json_file)
        return res


zet = Zettel()
res = zet.getAllTags()
print(res)

#res = getTagsFromAFile("text")
#subprocess.call(["vim", "+{}".format(res[0]["lineNumber"]), "text"])
