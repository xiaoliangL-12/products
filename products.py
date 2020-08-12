#products = []
#while True:
#	name = input('请输入商品名称: ')                   
#	if name == 'e':                                   #请输入商品名字: 11
#		break                                         #请输入商品名字: 22
#	products.append(name)                             #请输入商品名字: e
#rint(products)                                       #[11, 22]

"*清单中还有清单/2 dimension"
products = []                                         #大清单
while True:
	name = input('请输入商品名称: ')                   
	if name == 'e':                                   
		break      
	price = input('请输入商品价格: ')
	price = int(price)
	p = []                                                    #小清单
	p.append(name)
	p.append(price) #//p = [name, price]                                
	products.append(p) #//products.append(name, price)        #小清单在大清单里面                    
print(products) 

#products[0][0]                                               #大清单里面第0格小清单的第0格                                     
                                     
for p in products:                                        #让大清单中的每一个小清单/p一个一个的list出来
	print(p[0], '的价格是', p[1])                          #把小清单里面的第一个一个一个的列出来
                                   
#'abc' + 123 = 'abc123'
#'abc' * 3 ='abcabcabc'

with open('products.csv', 'w') as f:                      #csv是来存储网站的能用excel/表格打开(,是区隔)
	f.write('商品, 价格\n')
	for p in  products:
		f.write(p[0] + ',' + str(p[1]) + '\n')            #f.write才是真正的开写, \是分行, str()把整数变成字串







