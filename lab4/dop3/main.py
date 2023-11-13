import re
import time

start_time = time.time()
fJSON = open('lab4JSON.json')
fYAML = open('lab4YAML.yaml', 'w')

lvlmas = [False] * 1000000
countBracket = [0] * 100000
countLine = [0] * 100000
index = -1
for line in fJSON:
    if re.match(r".*{", line) and lvlmas[index] == True and countBracket[index] == 0:
        countBracket[index] = 1
        continue
    if countLine[index] == 0 and countBracket[index] == 1:
        jndex = line.find('"')
        line = line[:jndex - 2] + '-' + line[jndex - 1:]
        countLine[index] = 1
    if lvlmas[index] == True and re.match(r".*{", line):
        countBracket[index] += 1
    if lvlmas[index] == True and re.match(r".*}", line):
        countBracket[index] -= 1
        if countBracket[index] == 0:
            countLine[index] = 0
    if re.match(r".*]", line):
        lvlmas[index] = False
        index -= 1
        continue
    if re.match(r".*\[", line):
        line = line.replace('[', '')
        index += 1
        lvlmas[index]=True
    if re.match(r".*},?", line) or re.match(r"\s*{", line):
        continue
    if re.match(r".*: {", line):
        line = line.replace('{', '')
    if re.match(r".*,$", line):
        line = line[:len(line) - 2] + line[-1:]
    line = line[2:]
    if not index == -1:
        if countBracket[index] == 0:
            if not index == 0:
                line = line[(2 * index):]
        if not countBracket[index] == 0:
            line = line[(2*(index+1)):]
    line = line.replace('"', '')
    fYAML.write(line)
fYAML.close()
end_time = time.time()
print(end_time - start_time)