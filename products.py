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
	p = []                                                    #小清单
	p.append(name)
	p.append(price) #//p = [name, price]                                
	products.append(p) #//products.append(name, price)        #小清单在大清单里面                    
print(products) 

#products[0][0]                                               #大清单里面第0格小清单的第0格                                     
                                     
	


