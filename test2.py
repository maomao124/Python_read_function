"""
 * Project name(项目名称)：Python_read函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 22:06
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    file1 = open("test2.py", "rb")
    # print(file1.read(10))
    # print(file1.read(10))
    # print(file1.read(10))
    b = file1.read()
    print(b)
    print()
    print("-------------------------------------------")
    print()
    print(b.decode("UTF-8"))
    print()
    print("-------------------------------------------")
    print()
    print(b.decode("utf-16le"))
    print()
    print("-------------------------------------------")
    print()
    print(b.decode("utf-16be", errors="?"))
    print()
    file1.close()

    input()
