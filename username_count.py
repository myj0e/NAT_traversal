

#统计filename中以空格为分割的第一列（用户名）出现的频率，返回为字典
def getData(filename:str)->dict:
    data = {}
    line_num = 1
    with open(filename,"r", encoding="utf-8") as fp:
        line = fp.readline()
        while line:
            if ("ssh:" not in line):
                line = fp.readline()
                continue
            username = line.split(' ')[0]
            if username not in data:
                data[username] = 1
            else:
                data[username] += 1
            print("processing:{}".format(line_num),end="\r")
            line = fp.readline()
            line_num += 1
        print("")
    return data

#统计结果写入文档
def writeResult(sort_data:list, filename:str):
    with open(filename,"w") as fp:
        for username, count in sort_data:
            fp.write("{0},{1}\n".format(username,count))


def main():
    data = getData("btmp.txt")
    sort_data = sorted(data.items(), key=lambda x: x[1], reverse = True)
    writeResult(sort_data,"result")
    print("OK")

import chardet

if "__main__" == __name__:
    main()
