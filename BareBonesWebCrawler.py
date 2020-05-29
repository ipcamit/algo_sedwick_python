import re
from In import In

queue = []
marked = set([])

root='http://www.princeton.edu'
queue.append(root)
marked.add(root)

while len(queue) != 0:
    v = queue.pop(0)
    print("Current Domain {}".format(v))
    in_ = In(v)
    inputStr = in_.readAll()
    pattern = re.compile(r'http://(\w+\.)*(\w+)',re.I)
    matcher = pattern.finditer(inputStr)
    while True:
        try:
            match = next(matcher)
            w = match.group()
            if (not (w in marked)) and ("princeton" in w):
                # print(marked)
                # print(w)
                marked.add(w)
                queue.append(w)
        except:
            print("done")
            break   
print(marked)

