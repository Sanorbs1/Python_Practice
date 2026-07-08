with open("list.py", "w", encoding="utf-8") as f:
    f.write("Hello, file!\n")
    f.writelines(["Line 1\n", "Line 2\n"])