import json
# 字典
# 全局变量
adict={"十七":"十七","77":"5"}
bdict={"5":"道长","道长":"77"}
cdict_dict='{"\u5341\u4e03": "\u5341\u4e03", "77": "5"}'
# adict = {"username":"yansl","password":"123456"}
# bdict = {5:"yansl","password":[2,5]}

def dict_sel():
    # 查询语法（查询变量）
    print(adict['十七'])
    print(bdict['5'])

def dict_del():
    # 删除语法（全局变量）
    adict.pop('77')
    print(adict)

def dict_add():
    # 合并语法（全局变量）K的字段不能重复，重复自动去重；相同K保留v时候保留括号中的v
    # 方式一
    adict.update(bdict)
    # 打印adict
    print(adict)

    # 方拾贰
    cdict = dict(adict,**bdict)
    # K的字段不能重复，重复自动去重；相同K保留v时候保留括号中的v
    # 打印cdict
    print(cdict)

def dict_add1():
    # 增加全局变量中的元素（默认添加到最后）
    adict['sex']='男'
    print(adict)

# 字典转字符串

def dict2str():
    print(type(adict))

    # 使用语法为json.dumps
    adict_str=json.dumps(adict)

    print(adict_str)
    print(type(adict_str))

# 字符串转化字典(首先转换的必须是字符串才能转化为字典)
def  str2_dint():
    print(type(cdict_dict))

    # 使用语法为json.loads
    cdict=json.loads(cdict_dict)

    print(cdict)
    print(type(cdict))


if __name__ == '__main__':
    # dict_sel()
    # dict_del()
    # dict_add()
    # dict_add1()
    # dict2str()
     str2_dint()