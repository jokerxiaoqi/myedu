# 字典类型
# 字符类型
import  json
adind={'王也':'十七','道长':'小七'}
bdind='{"王也":"十七","道长":"小七"}'

# 字典转字符串
def adint_str():
    print(type(adind))
    cdint=json.dumps(adind)
    print(type(cdint))

# 字符串转字典
def bdind_dint():
    print(type(bdind))
    cdint=json.loads(bdind)
    print(type(cdint))


def adint_sel(c):
    c=[1,3,'dna','十七','胡来','很可怕呦']
    print(c[0])
    d=c[3:]
    a=c[0:4]
    d.append(a)
    print(d)


def adint_del():
    a=['任由','小七','胡来',
       '很','可怕','的哟']
    a.pop(-1)
    print(a)

def multi_table():
    result = ''
    for i in range(1, 10):
        for j in range(1, i + 1):
            separator = '\n' if j == i else '\t'
            result += '%d * %d = %-2d' % (j, i, i * j)
            result += separator
            i = 1
            i = i + 1
            i+=1
    return result



if __name__ == '__main__':
    # adint_str()
    # bdind_dint()
    # c = [1, '十七', 3, 'dna', '胡来', '很可怕呦']
    # adint_sel(c)
    adint_del()
    # multi_table()
    # r = multi_table()
    # print(r)
