import time

start_time = time.time()

fJSON = open('lab4JSON.json')
fYAML = open('lab4YAML.yaml', 'w')

lvlmas = False
countBracket = 0
countLine = 0
for line in fJSON:
    if line.find('[') != -1:
        line = line.replace('[', '')
        lvlmas = True
    if line.find('{') != -1 and lvlmas == True and countBracket == 0:
        countBracket = 1
        continue
    if countLine == 0 and countBracket == 1:
        index = line.find('"')
        line = line[:index - 2] + '-' + line[index - 1:]
        countLine = 1
    if lvlmas == True and line.find('{') != -1:
        countBracket += 1
    if lvlmas == True and line.find('}') != -1:
        countBracket -= 1
        if countBracket == 0:
            countLine = 0
    if line.find(']') != -1:
        lvlmas = False
        continue
    if line.find('}') != -1:
        continue
    if line.find('{') != -1:
        if line.find(':') != -1:
            line = line.replace('{', '')
        else:
            continue
    if line.rfind(',') == len(line) - 2:
        line = line[:len(line) - 2] + line[-1:]
    line = line[2:]
    if line[0] == line[1] == ' ':
        line = line[2:]
    line = line.replace('"', '')
    fYAML.write(line)
fYAML.close()
end_time = time.time()
print(end_time - start_time)