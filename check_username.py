import csv


def getUsernames(filename:str)->list:
    with open(filename, "r") as fp:
        reader = csv.reader(fp)
        usernames = [i for i in reader]
    return usernames


def cmdMod(string:str):
    args = string.split(" ")
    print(args)
    cmd = args[0]
    match cmd:
        case "help":
            print("TODO:help messgae")
        case "hotlist":
            if(len(args) < 2):
                print("Need parameter after hotlist")
                return
            hotlist(int(args[1]))
        case _:
            print("TODO:#{}#{}#".format(cmd,"hotlist"))
"""
cmdMod cmd_process
"""       
def hotlist(num:int):
    global usernames_unsafe
    global usernames_count
    print("username:count")
    for i in range(num):
        try:
            print("{:<8}:{}".format(usernames_unsafe[i], usernames_count[i] ))
        except BaseException:
            break



def main():
    global usernames_unsafe
    global usernames_count
    l = getUsernames("result")
    usernames_unsafe = [i[0] for i in l]
    usernames_count = [i[1] for i in l]
    while True:
        username = input("Input you username:")
        if (username == ""):
            continue
        if(username[0] == '/'):
            # 命令模式
            cmdMod(username[1:])
            continue
        if(username in usernames_unsafe):
            index = usernames_unsafe.index(username)
            print("unsafe: toplist#{}, count#{}".format(index+1, usernames_count[index]))
        else:
            print("safe")

if "__main__" == __name__:
    main()

    
    
