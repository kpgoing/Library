
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
          el: '#app',
          data: {
            wantBook: '',
            books: bookdata
          },
          methods: {
            borrowBook: function () {
              var book = this.wantBook.trim();
              if (book) {
                  var flag = true;
                   for (i = 0; i < this.books.length; i++) {
                        if (this.books[i].name == book) {
                            if (this.books[i].remainder > 0) {
                                that = this;
                                $('.books').find('#' + i).find('.borrow').slideToggle(200);
                                setTimeout(function () {
                                    that.books[i].borrow++;
                                    that.books[i].remainder--;
                                    $('.books').find('#' + i).find('.borrow').slideToggle(200);
                                }, 200);
                                flag = false;
                                borrowBook({name:book});
                                break;
                            }
                        }
                    }
                      if (flag){
                        alert('无此书籍!')
                  }
                this.newBook = ''
              }
            }
          }
        });
    }
});
function borrowBook(sentdata){
    $.ajax({
        url : "/book/borrowbook",
        type : "POST",
        datatype:"json",
        data:JSON.stringify(sentdata),
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {
                alert('借阅成功');
            }
        }
    })
}


