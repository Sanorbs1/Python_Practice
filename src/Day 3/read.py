with open("list.py", "r", encoding="utf-8") as f:
    line1 = f.readline()        # one line
    lines = f.readlines()       # list of all remaining lines

    # or iterate directly
    for line in f:
        ...