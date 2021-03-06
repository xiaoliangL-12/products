#products = []
#while True:
#    name = input('请输入商品名称: ')                   
#    if name == 'e':                                   #请输入商品名字: 11
#        break                                         #请输入商品名字: 22
#    products.append(name)                             #请输入商品名字: e
#rint(products)                                       #[11, 22]

"*清单中还有清单/2 dimension"
"*split/切割, split()括号里面是你想要分开的那一个东西, split切完之后就是list"
"*continue/继续: 跳到下一回"
"*os/作业系统: operating system"
"*refactor/重新架构: 把憋的东西变成function形式"

#读取档案
import os
def read_file(filename):
    products = [] 
    with open(filename, 'r') as f:
        for line in f:
            if '商品, 价格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price]) 
    return products 

#输入部分
def user_input(products):
    while True:
        name = input('请输入商品名称: ')                     #大清单
        if name == 'e':                                   
            break      
        price = input('请输入商品价格: ')
        price = int(price)
        p = []                                              #小清单                              
        products.append([name, price])                      #小清单在大清单里面                    
    print(products)
    return products 

    #products[0][0]                                         #大清单里面第0格小清单的第0格                                     

#印出所有商品记录
def print_products(products):                                    
    for p in products:                             #让大清单中的每一个小清单/p一个一个的list出来
        print(p[0], '的价格是', p[1])               #把小清单里面的第一个一个一个的列出来
                                   
#'abc' + 123 = 'abc123'
#'abc' * 3 ='abcabcabc'

#写入档案
def write_file(filename, products):
    with open(filename, 'w') as f:                 #csv是来存储网站的能用excel/表格打开(,是区隔)
        f.write('商品, 价格\n')
        for p in  products:
            f.write(p[0] + ',' + str(p[1]) + '\n')  #f.write才是真正的开写, \是分行, str()把整数变成字串

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):   #检查档案在不在, 最好把csv写成参数, 这样可以不一直卡在一个档案上面
        print('yeah!')
        products = read_file(filename)
    else:
        print('No!')
    products = read_file('products.csv')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)
main()