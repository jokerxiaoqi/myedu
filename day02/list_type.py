def list_sel(a):

    #取第二个元素值
    print(a[1])

    # 取倒数第一个元素值
    print(a[-1])

    # 取第一个和第五个元素值（切片取值）
    print(a[0:6])

    # 取第三个和第六个元素值
    print(a[4:7])

    #取第三个元素到最后一个元素
    print(a[0:])

def list_del():
    # 删除语法

    alist = ['a', 4, 'nihao', '8', '就是', '哈']

    alist.pop()
    # 不加任何参数默认删除最后一个

    print(alist)
    # 打印alist

    alist.pop(0)
    # 删除第一个

    print(alist)
    # 讲切片获取的元素重新定义一个list保存起来

    blist=alist[:-2]
    # 删除倒数第一个和第二个
    print(blist)

def add_list():
    # 添加语法

    alist=['a','b','c','d','f','g']
    blist=[1,2,3]

    alist.append(blist)
    # 向alist添加blist

    print(alist)

def list_update():

    alist = ['我是谁', 4, '你是谁', '你叫啥名字', 'who im i', 'who are you', 'what`s name']

    alist[0]='步惊云'
    print(alist)


if __name__ == '__main__':
    alist=['我是谁',4,'你是谁','你叫啥名字','who im i','who are you','what`s name']
    # list_sel(alist)
    # list_del()
    # add_list()
    list_update()