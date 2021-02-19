import argparse
import re
from pathlib import Path
import json
import csv

parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=Path)
p = parser.parse_args()

file = open(p.file_path)
fileContent = file.readlines();
file.close()

fileContentAsStr = ""
fileContentAsStr = fileContentAsStr.join(fileContent)

paragraphsDictionary = {}
matches = re.findall("## Begin (Paragraph \w*)\s*(\w*) type=(\w*) format=(\w*)\s*## End Paragraph \w*\s*", fileContentAsStr)
for match in matches:
    paragraphsDictionary[match[0]] = {"name": match[1], "type": match[2], "format": match[3]}
    
jsonFile = open('json_output.json', "w")
json.dump(paragraphsDictionary, jsonFile, indent=4)