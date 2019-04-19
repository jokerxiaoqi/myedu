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
    
if __name__ == '__main__':
    alist=['我是谁',4,'你是谁','你叫啥名字','who im i','who are you','what`s name']
    list_sel(alist)