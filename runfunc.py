"""负责集成function.py文件,负责输入输出以及函数运行

"""
from function import *
def main():
    while 1:
        func = input(">>> ")
        out(func)
        s(func)
        inp(func)
        var(func)
if __name__ == "__main__":
    main()