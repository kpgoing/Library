
$(function () {
     getAllBooks();
    window.app2 = new Vue({
          el: '#app2',
          data: {
            wantBook: '',
            books: {}
          },
          methods: {
              borrowBook: function (name) {
                  book = arguments[0] ? arguments[0] : this.wantBook.trim();
                  if (book) {
                      var flag = true;
                      for (i = 0; i < this.books.length; i++) {
                          if (this.books[i].name == book) {
                              if (this.books[i].remainder > 0) {
                                  that = this;
                                  $('.books').find('#app2' + i).find('.borrow').slideToggle(200, function () {
                                      that.books[i].borrow++;
                                      that.books[i].remainder--;
                                      $('.books').find('#app2' + i).find('.borrow').slideToggle(200);
                                      flag = false;
                                      borrowBook({bookname: book});
                                  });
                                  break;
                              }
                          }
                      }
                      setTimeout(function () {
                          if (flag) {
                              alert('无此书籍!')
                          }
                      }, 500);
                      this.newBook = ''
                  }
              }
          }
        });
     window.app1 = new Vue({
          el: '#app1',
          data: {
            wantBook: '',
            books: {}
          },
          methods: {
            returnBook: function (index) {
                var book = this.books[index];
                  if (book) {
                                that = this;
                                 $('.books').find('#app1'+index).slideUp(300, function () {
                                                that.books.splice(index, 1);
                                                returnBook({blid: book.blid});
                                            });

                    }
              }
            }
          });
    var apporder = 2;
    $("#app1").hide();
    $("#app3").hide();
  $("#topbutton1").click(function(){
      if (apporder != 1) {
          $("#app" + apporder).fadeOut(200, function () {
              $("#app1").fadeIn();
              apporder = 1;
          });
           getBorrowBooks();
      }
});
    $("#topbutton2").click(function(){
      if (apporder != 2) {
          $("#app" + apporder).fadeOut(200, function () {
              $("#app2").fadeIn();
              apporder = 2;
              getAllBooks();
          });
      }
});
    $("#topbutton3").click(function(){
     if (apporder != 3) {
          $("#app" + apporder).fadeOut(200, function () {
              $("#app3").fadeIn();
              apporder = 3;
          });
      }
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
function returnBook(sentdata){
    $.ajax({
        url : "/library/return",
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

function getAllBooks(){
    $.ajax({
        url : "/allbooks",
        type : "POST",
        datatype:"json",
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {
                window.app2.$set('books',mydata.body);
            }
        }
    });
}
function getBorrowBooks(){
    $.ajax({
        url : "/library/showborrowedbook",
        type : "POST",
        datatype:"json",
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {
                window.app1.$set('books',mydata.body);
            }
        }
    });
}

function Cool(book){
      $('.books').find('app2#' + book.bid).find('.remainder').slideUp(200, function () {
                            $('.books').find('app2#' + book.bid).find('.borrow').slideUp(200, function () {
                                     book.remainder--;book.borrow++;
                                            $('.books').find('app2#' + book.bid).find('.remainder').slideDown(200, function () {
                                                $('.books').find('app2#' + book.bid).find('.borrow').slideDown(200);
                                            });
                                             borrowBook({bookname: book.bookname});
                                            });
                            });
}
function IsNum(s)
{
    if (s!=null && s!="")
    {
        return !isNaN(s);
    }
    return false;
}