import re
import time

start_time = time.time()

fJSON = open('lab4JSON.json')
fYAML = open('lab4YAML.yaml', 'w')

lvlmas = False
countBracket = 0
countLine = 0
for line in fJSON:
    if re.match(r".*\[", line):
        line = line.replace('[', '')
        lvlmas = True
    if re.match(r".*{", line) and lvlmas == True and countBracket == 0:
        countBracket = 1
        continue
    if countLine == 0 and countBracket == 1:
        index = line.find('"')
        line = line[:index - 2] + '-' + line[index - 1:]
        countLine = 1
    if lvlmas == True and re.match(r".*{", line) :
        countBracket += 1
    if lvlmas == True and re.match(r".*}", line) :
        countBracket -= 1
        if countBracket == 0:
            countLine = 0
    if re.match(r".*]", line) :
        lvlmas = False
        continue
    if re.match(r".*},?", line) or re.match(r"\s*{", line):
        continue
    if re.match(r".*: {", line):
        line = line.replace('{', '')
    if re.match(r".*,$", line):
        line = line[:len(line) - 2] + line[-1:]
    line = line[2:]
    if line[0] == line[1] == ' ':
        line = line[2:]
    line = line.replace('"', '')
    fYAML.write(line)
fYAML.close()
end_time = time.time()
result = (end_time - start_time)
print(result)