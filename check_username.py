import readline
import csv

cmdhistfile = ""
cmdhist = []
localusers_file = "localusers.txt"

def getUsernames(filename:str)->list:
    with open(filename, "r") as fp:
        reader = csv.reader(fp)
        usernames = [i for i in reader]
    return usernames

def username_analyze(username:str)->list:
    if(username not in usernames_unsafe):
        return 0,0
    index = usernames_unsafe.index(username)
    return index+1, usernames_count[index]

def input_with_history(prompt:str)->str:
    line = input(prompt)
    cmdhist.append(line)
    return line

def cmdMod(string:str):
    args = string.split(" ")
    print(args)
    cmd = args[0]
    if(cmd == "help"):
        print("TODO:help messgae")
    elif(cmd == "hotlist"):
        if(len(args) < 2 or args[1] == ""):
            print("Need parameter after hotlist")
            return
        hotlist(int(args[1]))
    elif(cmd == "localusers"):
        localusers()
    else:
        print("Fail to parse command {}".format(cmd))
            
            
"""
cmdMod cmd_process
"""       
def hotlist(num:int):
    global usernames_unsafe
    global usernames_count
    print("username    :count")
    for i in range(num):
        try:
            print("{:<12}:{}".format(usernames_unsafe[i], usernames_count[i] ))
        except BaseException:
            break

def localusers():
    localusers = []
    with open(localusers_file, "r") as fp:
        for i in fp:
            if(i.strip() == ""):
                continue
            localusers.append(i.strip())
        for i in localusers:
            _, cnt = username_analyze(i)
            print("{:<12}:{}".format(i, cnt))

def main():
    global usernames_unsafe
    global usernames_count
    l = getUsernames("result")
    usernames_unsafe = [i[0] for i in l]
    usernames_count = [i[1] for i in l]

    try:
        readline.read_history_file(cmdhistfile)
        readline.set_history_length(1000)
    except FileNotFoundError:
        pass

    while True:
        username = input_with_history("Input you username:")
        if (username == ""):
            continue
        if(username[0] == '/'):
            # 命令模式
            cmdMod(username[1:])
            continue
        if(username in usernames_unsafe):
            hl, cnt = username_analyze(username)
            print("unsafe: toplist#{}, count#{}".format(hl, cnt))
        else:
            print("safe")

if "__main__" == __name__:
    main()

    
    
