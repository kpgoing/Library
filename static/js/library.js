
$(function () {
    $.ajax({
        url : "/allbooks",
        type : "POST",
        datatype:"json",
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {
                bookdata =  mydata.body;
                Go();
            }
        }
    });
    function Go() {
           new Vue({
          el: '#app2',
          data: {
            wantBook: '',
            books: bookdata
          },
          methods: {
            borrowBook: function () {
                book = arguments[0] ? arguments[0] : this.wantBook.trim();
                  if (book) {
                  var flag = true;
                   for (i = 0; i < this.books.length; i++) {
                        if (this.books[i].name == book) {
                            if (this.books[i].remainder > 0) {
                                that = this;
                                $('.books').find('#' + i).find('.borrow').slideToggle(200, function () {
                                    that.books[i].borrow++;
                                    that.books[i].remainder--;
                                    $('.books').find('#' + i).find('.borrow').slideToggle(200);
                                    flag = false;
                                borrowBook({bookname:book});
                                });
                                break;
                            }
                        }
                    }
                    setTimeout(function () {
                        if (flag){
                        alert('无此书籍!')
                  }
                    },500) ;
                this.newBook = ''
              }
            }
          }
        });
    }
  $("#topbutton1").click(function(){
   //$(".content").animate({
   //    left:'=+300'
   //},200,function(){
   // alert('11');
   //});
      $("#app2").fadeOut();
});
});
function borrowBook(sentdata){
    $.ajax({
        url : "/library/borrow",
        type : "POST",
        datatype:"json",
        data:JSON.stringify(sentdata),
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {
                //alert('借阅成功');
            }
        }
    })
}



