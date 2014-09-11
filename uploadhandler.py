__author__ = 'marcusfaust'


import csv, re


class uploadedCSV(file):

    def __init__(self, file):

        self.paths = []
        self.shares = []

        with open('tmp.csv', 'rU') as csvfile:
            sharescsv = csv.reader(csvfile, delimiter=',', escapechar="")
            for row in sharescsv:
                share = row[0]
                path = row[1]
                path = re.sub('^[a-zA-Z]:\\\\', '/', path)
                path = re.sub('\\\\', '/', path)
                self.shares.append(share)
                self.paths.append(path)

    def outputCmds(self, server, mountpoint):
        cmds = []
        index = 0
        currCmd = ""
        for path in self.paths:
            currCmd = "server_export server_2 -Protocol cifs -name \"" + self.shares[int(self.paths.index(path))] + "\" -option netbios=" + server + " \"" + mountpoint + path + "\""
            cmds.append(currCmd)
            index += 1
        return cmds


