"""
 * Project name(项目名称)：Python_read函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 21:50
 * Version(版本): 1.0
 * Description(描述)：
 file.read([size])
其中，file 表示已打开的文件对象；size 作为一个可选参数，用于指定一次最多可读取的字符（字节）个数，如果省略，则默认一次性读取所有内容。
 """
import functools
import time


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print('函数"%s"执行时间：%.4f ms' % (func.__name__, (end - start) * 1000))
        return result

    return wrapper


@log_execution_time
def readpy(filename):
    """
    读源文件
    :param file:
    :return:
    """
    file = open(filename, "r", encoding="UTF-8")
    filestr = file.read()
    file.close()
    return filestr


if __name__ == '__main__':
    # file = open("test1.py", "r", encoding="UTF-8")
    print(readpy("test1.py"))
    file1 = open("test1.py", "r", encoding="UTF-8")
    print()
    print("---------------")
    print()
    print(file1.read(10))
    print(file1.read(10))
    print(file1.read(10))
    file1.close()

    input()
