#! /usr/env/bin python3

import re
#import subprocess
import os
import json
import argparse

class Zettel:

    def __init__(self):
        self.cli()
        self.path = os.getcwd()
        self.tags = self.loadJson(self.path + "/.tags.json")

        if self.args.u:
            self.tags = self.getAllTags()
            self.saveToJson(self.path + "/.tags.json", self.tags)

        #self.tags = self.getAllTags()
        print(self.tags)

    def cli(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", action="store_true")
        self.args = parser.parse_args()

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
        for fil in os.listdir(self.path):
            if fil[-2:] == "md":
                dics += self.getTagsFromAFile(fil)
        return dics


    def saveToJson(self, storagePath, data):
        with open(storagePath, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return 0 


    def loadJson(self, storagePath):
        if not os.path.exists(storagePath):
            with open(storagePath, "w") as json_file:
                tmp = []
                json.dump(tmp, json_file, indent=4)
        with open(storagePath) as json_file:
            res = json.load(json_file)
        return res


zet = Zettel()

#res = getTagsFromAFile("text")
#subprocess.call(["vim", "+{}".format(res[0]["lineNumber"]), "text"])
