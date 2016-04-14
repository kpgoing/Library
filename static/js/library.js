
$(function () {
    var apporder = 2;
    $("#app1").hide();
    $("#app3").hide();
    $.ajax({
        url : "/allbooks",
        type : "POST",
        datatype:"json",
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {
                bookdata =  mydata.body;
                App2();
            }
        }
    });
    function App2() {
        var app2 = new Vue({
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
                                $('#app2').find('#app2' + i).find('.borrow').slideToggle(200, function () {
                                    that.books[i].borrow++;
                                    that.books[i].remainder--;
                                    $('#app2').find('#app2' + i).find('.borrow').slideToggle(200);
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
      if (apporder != 1) {
          $("#app" + apporder).fadeOut(200, function () {
              $("#app1").fadeIn();
              apporder = 1;
          });
           $.ajax({
        url : "/library/showborrowedbook",
        type : "POST",
        datatype:"json",
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {
                bookdata1 =  mydata.body;
                App1();
            }
        }
    });
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
function App1() {
          var app1 = new Vue({
          el: '#app1',
          data: {
            wantBook: '',
            books: bookdata1
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
                .$set('books',mydata.body);

            }
        }
    });
}


