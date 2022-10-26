var windowwidth = window.innerWidth || document.documentElement.clientWidth || 0;
    if (windowwidth > 768){
      var responsiveImage = [//PC用の画像
        { src: './static/img/jumon1.1.png'},
        { src: './static/img/jumon8.6.png'},
        { src: './static/img/jumon3.2.png'},
        { src: './static/img/jumon13.png'},
      ];
    } else {
    }

//Vegas全体の設定

$('#slider').vegas({
    overlay: false,//画像の上に網線やドットのオーバーレイパターン画像を指定。
    //transition: '',//切り替わりのアニメーション。http://vegas.jaysalvat.com/documentation/transitions/参照。fade、fade2、slideLeft、slideLeft2、slideRight、slideRight2、slideUp、slideUp2、slideDown、slideDown2、zoomIn、zoomIn2、zoomOut、zoomOut2、swirlLeft、swirlLeft2、swirlRight、swirlRight2、burnburn2、blurblur2、flash、flash2が設定可能。
    transitionDuration: 2000,//切り替わりのアニメーション時間をミリ秒単位で設定
    delay: 10000,//スライド間の遅延をミリ秒単位で。
    animationDuration: 20000,//スライドアニメーション時間をミリ秒単位で設定
    //animation: 'kenburns',//スライドアニメーションの種類。http://vegas.jaysalvat.com/documentation/transitions/参照。kenburns、kenburnsUp、kenburnsDown、kenburnsRight、kenburnsLeft、kenburnsUpLeft、kenburnsUpRight、kenburnsDownLeft、kenburnsDownRight、randomが設定可能。
    slides: responsiveImage,//画像設定を読む
  });

var slider;
var sliderFlag = false;
var breakpoint = 768;//768px以下の場合
  
function sliderSet() {
        var windowWidth = window.innerWidth;
        if (windowWidth >= breakpoint && !sliderFlag) {//768px以上は1行でスライダー表示
            slider = $('.slider').bxSlider({
            touchEnabled:false,//リンクを有効にするためスライドをマウスでドラッグした際にスライドの切り替えを可能にする機能を無効化
			      mode: 'vertical',//縦スライド指定
			      controls: false,//前後のコントロールを表示させない。
		      	  auto: 'true',//自動的にスライド
		      	  pager: false//ページ送り無効化
		});
            sliderFlag = true;
        } else if (windowWidth < breakpoint && sliderFlag) {
            slider.destroySlider();//bxSliderのOptionであるdestroySliderを使用してスライダーの動きを除去
            sliderFlag = false;
        }
    }

$(window).on('load resize', function() {
        sliderSet();
});