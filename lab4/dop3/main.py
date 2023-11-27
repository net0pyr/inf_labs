import re
import time

start_time = time.time()
fJSON = open('lab4JSON1.json')
fYAML = open('lab4YAML.yaml', 'w')

lvlmas = [False] * 1000000
countBracket = [0] * 100000
countLine = [0] * 100000
mas = []
index = 0
for line in fJSON:
    if re.match(r".*{", line) and lvlmas[index] == True and countBracket[index] == 0:
        countBracket[index] = 1
        mas.append(1)
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
        if re.match(r".*/S.*",line):
            fYAML.write(line)
        continue
    if lvlmas[index]==True and countBracket[index] == 0 and not re.match(r".*{", line):
        jndex = 0
        for x in line:
            if x!=' ':
                break
            jndex+=1
        line = line[:jndex - 2] + '  -' + line[jndex - 1:]
    if re.match(r".*},?", line) or re.match(r"\s*{", line):
        continue
    if re.match(r".*: {", line):
        line = line.replace('{', '')
    if re.match(r".*,$", line):
        line = line[:len(line) - 2] + line[-1:]
    line = line[2:]
    line = line.replace('"', '')
    fYAML.write(line)
fYAML.close()
end_time = time.time()
print(end_time - start_time)