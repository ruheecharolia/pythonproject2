with open("http_access_log.txt") as file_in:
    array = []
    for line in file_in:
        array.append(line)
comp = 0
dc = 0
wcomp = 0
wc = 0
mcomp = ""
mc = 0

for i in array:
    if i.find("[") != -1:
        dl = i.find("[")
        
