// 浮动小特效
$(window).scroll(scr)
scr();
function scr(){
	var gd = $(document).scrollTop();
	if(gd>500){
		$('#fd2').show()
	}else{
		$('#fd2').hide()
	}

	// 额外配件的图片固定头部特效
	if (gd>288){
		var cw = $(window).width();
		if (cw>640){
			var h = gd-290
			$('.fix_top').css("margin-top",h+"px")
		}
		
	}
}

// 因为执行顺序的原因要在特效外加一个function
$(function(){
	// 主页
	// 鼠标进入图片的特效
	$('.slat').hover(function(){
		$('.slap1').attr('src','public/img/sla3_2.jpg')
		$('.slap1').next('img').hide()
	},function(){
		$('.slap1').attr('src','public/img/sla3_1.jpg')
		$('.slap1').next('img').show()
	})




	// 详情页
	// 点击图片切图
	$('.spzs1').click(function(){
		var s = $(this).find('img').attr('src')
		$('.spzs2').attr('src',s)
	})


	// 产品说明点击特效
	$('.cpsm div').click(function(){
		$(this).addClass('cpsm1').siblings().removeClass('cpsm1')
		var id = $(this).index()
		$('.cpsms').eq(id).show().siblings().hide()
	})


	// 购买页
	// 下一步按钮
	var i=1
	var timebg=false
	var flag=[0,0,0,0]
	$('.btn_xyb').click(function(){
		i++
		var w = $('.buy div').eq(i-1).html()

		$('.buy div').eq(i).addClass('buy_border').siblings().removeClass('buy_border')
		$('.buy div').eq(i-1).addClass('buycol')
		flag[i-2] = 1
		switch(i){
			case 2:
				$('.buyinb').show();
				$('.buyinc').hide();
				$('.buyind').hide();
				$('.buyina').hide();
				break;
			case 3:
				$('.buyinc').show();
				$('.buyind').hide();
				$('.buyina').hide();
				$('.buyinb').hide();
				break;
			case 4:
				$('.buyind').show();
				$('.buyinc').hide();
				$('.buyinb').hide();
				$('.buyina').hide();
				$('.btn_fa').empty();
				var $span = $('<button class="btn btn-info btn_zd" data-toggle="modal" data-target="#myModal">加入购物车</button>')
				timebg = true
				$('.btn_fa').append($span);
				break;	
		}
	})


	// checkgoods
	$('.buy div').click(function(){
		var a = $(this).index()
		if(flag[a-1]==1){
			switch(a){
				case 1:
					$('.buyina').show();
					$('.buyinc').hide();
					$('.buyind').hide();
					$('.buyinb').hide();
					$('.buy div').eq(a).addClass('buy_border').siblings().removeClass('buy_border')
					i=a;
					break;
				case 2:
					$('.buyinb').show();
					$('.buyind').hide();
					$('.buyina').hide();
					$('.buyinc').hide();
					$('.buy div').eq(a).addClass('buy_border').siblings().removeClass('buy_border')
					i=a;
					break;
				case 3:
					$('.buyinc').show();
					$('.buyind').hide();
					$('.buyinb').hide();
					$('.buyina').hide();
					$('.buy div').eq(a).addClass('buy_border').siblings().removeClass('buy_border')
					i=a;
					break;
				case 4:
					$('.buyind').show();
					$('.buyinc').hide();
					$('.buyinb').hide();
					$('.buyina').hide();
					$('.buy div').eq(a).addClass('buy_border').siblings().removeClass('buy_border')
					i=a;
					break;
			}
		} 
	})

	// 选择偏好
	$('.select1a').click(function(){
		$(this).addClass('selected1').siblings().removeClass('selected1')
		var inde = $(this).find('#optionsRadios1').attr('value')
		$('.money').html(inde)
	})
	// 有bug
	$('.select1b').click(function(){
		$(this).addClass('selected2').siblings().removeClass('selected2')
	})



	// 选择套装

	var xztz = true
	$('.btn_select3').click(function(){
		// 对下一张页面的操作
		$('.ewtz1').show()
		$('.ewtz2').hide()

		// 对这张页面的操作
		$(this).addClass('selected3')
		$('.btn_select4').removeClass('selected3')
		if(!xztz){
			var xztzy = Number($('.money').html())
			var xztzx = 499
			var index = xztzy-xztzx
			$('.money').html(index)
			xztz = true
		}
	})
	$('.btn_select4').click(function(){
		// 对下一张页面的操作
		$('.ewtz1').hide()
		$('.ewtz2').show()
		// 对这张页面的操作
		$(this).addClass('selected3')
		$('.btn_select3').removeClass('selected3')
		if(xztz){
			var xztzy = Number($('.money').html())
			var xztzx = 499
			var index = xztzy+xztzx
			$('.money').html(index)
			xztz = false
		}
	})

	// 额外套装
	$('.btn_pj_up').click(function(){
		// 数量数值改变
		var a = $(this).next().html()
		a++
		$(this).next().html(a)
		// 加钱
		var b = Number($('.money').html())
		var c = $(this).parent().next().next().find('.price').html()
		var reg = /\w+/
		var rec = Number(reg.exec(c))
		var d = b+rec
		$('.money').html(d)

	})
		
	$('.btn_pj_down').click(function(){
		var a = $(this).prev().html()
		if(a>0){
			a--
			$(this).prev().html(a)
			// 减钱
			var b = Number($('.money').html())
			var c = $(this).parent().next().next().find('.price').html()
			var reg = /\w+/
			var rec = Number(reg.exec(c))
			var d = b-rec
			$('.money').html(d)
		}
	})

	// 模态框特效
	var time = 5
	$('.btn_zd').live('click',function(){
		alert(123)
		if(timebg){
			var init = setInterval(abc,1000)
			function abc(){
				if(time=0){
					window.location.href="index.html"
				}
				time = Number($('.set').html())
				time = time - 1
				$('.set').html(time)
			}
		}
	})

	// var time = 5
	// $('.btn_zd').live('click',function(){
	// 	alert(123)
	// 	if(timebg){
	// 		var init = setInterval(abc,1000)
	// 		function abc(){
	// 			if (time=0){
	// 				// 跳转页面
	// 			}
	// 			time = Number($('.set').html())
	// 			time = time - 1
	// 			$('.set').html(time)

	// 		}
	// 	}



	// 搜索区特效
	var cw = $(window).width()
	$(".a, .aj").mouseover(function(){
		if(cw>640){
			$('.aj').show()
		}
		
	})
	$('.a, .aj').mouseout(function(){
		if(cw>640){
			$('.aj').hide()
		}
    })

    $(".b, .bj").mouseover(function(){
		if(cw>640){
			$('.bj').show()
		}
		
	})
	$('.b, .bj').mouseout(function(){
		if(cw>640){
			$('.bj').hide()
		}
    })

    $(".c, .cj").mouseover(function(){
		if(cw>640){
			$('.cj').show()
		}
		
	})
	$('.c, .cj').mouseout(function(){
		if(cw>640){
			$('.cj').hide()
		}
    })

    $('.aj1').mouseover(function(){
    	$('.ajj1').show()
    	$('.ajj2').hide()
    	$('.ajj3').hide()
    })
    $('.aj2').mouseover(function(){
    	$('.ajj2').show()
    	$('.ajj1').hide()
    	$('.ajj3').hide()
    })
    $('.aj3').mouseover(function(){
    	$('.ajj3').show()
    	$('.ajj2').hide()
    	$('.ajj1').hide()
    })


    // 页面自动跳转函数
    $('.zdtz').click(function(){
    	// document.write("../index.html")
    	window.location.href="index.html"
    })






















})






			







