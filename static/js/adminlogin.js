$(function () {
    // init...
    var a = $('.login');
    var content = $('.content');
    content.hide();
    content.fadeIn(2000);
    // setTimeout(content.slideDown(1000),100000);

a.on('click', function  () {
	// body...
	$('body').css('-webkit-filter','blur(200px)');

});

	var img = new Image();
	img.src = "/static/img/test.png";
	img.onload = function(){
		$('.bac').attr('src','/static/img/test.png');
	};
	content.find('.panel').hover(
		function  () {
			$('.blur').css('-webkit-filter','blur(10px)');
		},
		function  () {
			$('.blur').css('-webkit-filter','blur(0px)');
		}
		);

	$('#submit').click(function () {
	$.ajax(
		{
			type: "POST",
			url:"./admin",
			datatype:"json",
			contentType: 'application/json',
                data: JSON.stringify({
                    adminname: $('#adminname').val(),
                    password: $('#password').val()
                }),
			success: function (data) {
					if (data.status == 1){
						location.href='/admin/book';
					}else {
                        location.reload();
                    }
				}

		}
	)
})
});
