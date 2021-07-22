import sys

fname=sys.argv[1]

with open(fname) as f:
    content=f.readlines()
    content=[i.strip() for i in content]
    filtered_con=content[:-2]
    first="set "
    grep_system=filtered_con[0][:-1]
    res=[i[:-1] for i in filtered_con]
    res=[first+grep_system+i for i in res[1:]]
    for i in res:
        print(i)
    