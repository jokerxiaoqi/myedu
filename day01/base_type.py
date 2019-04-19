def text1():
    print('text1')

def text2():
    print('text2')

def text3():
    print('text3')

def aint_demo():
    aint=5
    # 变量aint赋值为5
    print(aint)
    # 打印aint
    print(type(aint))
    #打印aint的类型   （int类型）

def str_demo():
    astr='5'
    print(astr)
    print(type(astr))
   #打印astr的类型   （str类型）

def float_demo():
    afloat=0.123
    print(afloat)
    print(type(afloat))
    #打印afloat类型 （float）

def add_demo(a,b):
    # 增加语法
    print(a+b)

def type_zhuanhuan():
    # 类型转换
    aint=7
    print(aint)
    print(type (aint))
    # 转换类型为
    print(type (str(aint)))
    # 转换类型为
    print(type (int(aint)))
    # 转换类型为

def float_zhuanhuan():
    afloat=0.01
    print(afloat)
    print(type(afloat))
    print(type(str(afloat)))
    print(type(int(afloat)))

def str_join():
    a =123
    b ='是'
    c =0.123
    print(str(a) + b + str(c) )
    print('%s %s %s'%(a,b,c))

def jianfa_demo(a,b):
     # a - b
    return a - b


if __name__ == '__main__':#程序入口，放入可执行代码
    # text3()
    # text1()
    # text2()
    # aint_demo()
    # str_demo()
    # float_demo()
    # add_demo(999,999)
    # add_demo('你好','再见')
    # type_zhuanhuan()
    # float_zhuanhuan()
    # str_join()
    c = jianfa_demo(4,1)
    print(c)
    d = add_demo(6,3)
    print(d)
    print(type(d))