from django.shortcuts import render
from django.http import HttpResponse
from myweb.models import Goods,Types,Users
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myweb.models import Detail,Orders
import time


# 商城首页
def index(request):
    path = request.path
    request.session['path'] = path

    typelist = {}
    mytype = Types.objects.filter(pid = 0)
    for i in mytype:
        abc = i.id
        onetype = Types.objects.get(id = abc)
        typeset = onetype.info()
        typelist[str(abc)] = typeset
    request.session['typelist'] = typelist

    ob = Goods.objects.order_by('-clicknum')
    # ob = reversed(ob)
    context = {'hotgoods':ob}
    return render(request,"myweb/index.html",context)

# 商城商品列表页
def list(request):
	path = request.path
	request.session['path'] = path

	goodslist = Goods.objects.filter()
	if request.GET.get('tid','') != '':
		tid = str(request.GET.get('tid'))
		goodslist = goodslist.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+tid+','))
	context = {'goodslist':goodslist}
	return render(request,"myweb/list.html",context)

# 商城商品详情页
def detail(request,gid):
    path = request.path
    request.session['path'] = path

    goodob = Goods.objects.get(id = gid)
    goodob.clicknum += 1
    goodob.save()
    print(goodob.clicknum)
    context = {}
    context['goodob'] = goodob
    return render(request,"myweb/detail.html",context)


def cartshow(request):
	path = request.path
	request.session['path'] = path
	return render(request,'myweb/cart.html')

# 购物车
def cartadd(request):
	num = request.POST['num']
	gid = request.POST['gid']

	shop = Goods.objects.get(id = gid)
	shop = shop.info()
	shop['num'] = int(num)

	if 'shoplist' in request.session:
		shoplist = request.session['shoplist'] 
		total = request.session['num']
	else:
		shoplist = {}
		total = 0

	if gid in shoplist:
		shoplist[gid]['num'] += int(num)

	else:
		shoplist[gid] = shop
		request.session['num'] = total + 1
	request.session['shoplist'] = shoplist
	return redirect(reverse('cartshow'))


def cartchange(request):
	gid = request.GET['gid']
	num = request.GET['num']
	command = request.GET['command']
	print(num,command)

	shoplist = request.session['shoplist']
	if command == 'desc':
		if shoplist[gid]['num']>1:
			shoplist[gid]['num'] -= 1
		else:
			shoplist[gid]['num'] = 1
	else:
		shoplist[gid]['num'] += 1
	request.session['shoplist'] = shoplist

	return redirect(reverse('cartshow'))


def cartdel(request,gid):
	shoplist = request.session['shoplist']
	del shoplist[gid]
	request.session['shoplist'] = shoplist
	request.session['num'] -= 1
	return redirect(reverse('cartshow'))

def cartclear(request):
	try:
		del request.session['shoplist']
		del request.session['num']
		return redirect(reverse('cartshow'))
	except:
		return redirect(reverse('cartshow'))


# 订单页
def ordera(request):
	# if 'user' not in request.session:
	# 	return render(request,'myweb/login.html')

	ids = request.GET.get('gids','')
	gids = ids.split(',')
	if ids == '':
		context = {'info':'请选择要购买的商品'}
		return render(request,'myweb/ordera.html',context)

	shoplist = request.session['shoplist']
	orderlist = {}
	total = 0
	for sid in gids:
		orderlist[sid] = shoplist[sid]
		total += shoplist[sid]['price']*shoplist[sid]['num']

	request.session['orderlist'] = orderlist
	request.session['total'] = total
	print(total,orderlist)
	
	return render(request,'myweb/ordera.html')

def orderb(request):
	express={}
	express['name'] = request.POST['name']
	express['address'] = request.POST['address']
	express['code'] = request.POST['code']
	express['phone'] = request.POST['phone']
	request.session['express'] = express
	return render(request,'myweb/orderb.html')

def orderadd(request):
	# 订单表
	ob = Orders()

	ob.uid = request.session['user']['id']
	ob.linkman = request.session['user']['name']
	ob.address = request.session['express']['address']
	ob.code = request.session['express']['code']
	ob.phone = request.session['express']['phone']
	ob.addtime = time.time()
	ob.total = request.session['total']
	ob.status = 0
	ob.save()

	# 订单详情表
	orderlist = request.session['orderlist']
	print( orderlist )
	shoplist = request.session['shoplist']
	print(shoplist)

	for i in orderlist:
		dd = Detail()
		dd.orderid = str(int(time.time()))+str(request.session['express']['code'])+str(request.session['user']['id'])
		goodsid = orderlist[i]['id']
		dd.goodid = goodsid
		dd.name = orderlist[i]['goods']
		dd.price = orderlist[i]['price']
		dd.num = orderlist[i]['num']
		dd.save()
		shoplist = {}
		shoplist = request.session['shoplist']

		del shoplist[str(goodsid)]
		request.session['shoplist'] = shoplist

	# 加入到历史订单中

	history = {}
	for i in orderlist:
		history[str(orderlist[i]['id'])] = orderlist[i]

	try:
		nbb = request.session['history'] 
		for i in nbb:
			history[nbb[i]['id']] = nbb[i]
		request.session['history'] = history
	except:
		request.session['history'] = history
	return redirect(reverse('ordershow'))

def ordershow(request):
	return render(request,'myweb/myorder.html')


# 登录页
def login(request):


	return render(request,'myweb/login.html')

def dologin(request):
	
	# if request.session['verifycode'] != request.POST['verify']:
	# 	context['info'] = '验证码错误'
	# 	return render(request,'myweb/login.html',context)
	context = {}
	# try:
	ob = Users.objects.get(username = request.POST['account'])
	userinfo = ob.info()
	import hashlib
	m = hashlib.md5()
	m.update(bytes(request.POST['account'],encoding='utf8'))
	if ob.password != m.hexdigest():
		request.session['user'] = userinfo
		
		try:
			path = str(request.session['path'])
			path = path[1:]
			return redirect(reverse(path))
		except:
			return render(request,'myweb/index.html')
		# return render(request,path,context)
	else:
		context['info'] = '密码错误'
	# except:
	# 	context['info'] = '账号错误'

	return render(request,'myweb/login.html',context)

def logout(request):
	del request.session['user']	
	return render(request,'myweb/login.html')

