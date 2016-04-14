
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
            newBook: '',
            books: bookdata
          },
          methods: {
            addToBooks: function () {
              var book = this.newBook.trim();
                that = this;
              if (book) {
                  this.newBook = '';
                  var flag = true;
                  if(this.books){
                   for (i = 0; i < this.books.length; i++) {
                        if (this.books[i].name == book) {
                            that = this;
                            $('.books').find('#'+i).find('.remainder').slideDown(200);
                            setTimeout(function(){that.books[i].count++;that.books[i].remainder++;
                                        $('.books').find('#'+i).find('.remainder').slideUp(200);
                                        addBook({name:book});
                            },200);
                            flag = false;
                            break;
                        }
                    }
                      if (flag){
                      this.books.push({ name: book ,count:1,remainder:1,reservation:0,borrow:0,borrow_datetime: null,reservation_datetime: null});
                         index =  this.books.length-1;
                          addBook({name:book});
                  }
                  }else {
                      this.books = [{ name: book ,count:1,remainder:1,reservation:0,borrow:0,borrow_datetime: null,reservation_datetime: null}];
                      index =  this.books.length-1;
                      addBook({name:book});
                  }
              }
            },



            removeBook: function (index) {
                for (var i = 0;i < this.books.length ; i++){
                    if(this.books[i].bid == index){
                        var n = i;
                        break;
                    }
                }

                var book = this.books[n];
                if (book) {
                     that = this;

                                        if(book.count > 1) {
                                            $('.books').find('#' + index).find('.remainder').slideUp(200, function () {
                                               book.count--;book.remainder--;
                                            $('.books').find('#' + index).find('.remainder').slideDown(200);
                                             deleteBook({name: book.name});
                                            });
                                        }else{

                                            $('.books').find('#'+index).slideUp(300, function () {
                                                that.books.splice(index, 1);
                                                deleteBook({name: book.name});
                                            });
                                    }

                }}
          }
        });
    }
});
function addBook(sentdata){
    $.ajax({
        url : "/admin/addbook",
        type : "POST",
        datatype:"json",
        data:JSON.stringify(sentdata),
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {
                //alert('add success!');
            }
        }
})};
function deleteBook(sentdata){
    $.ajax({
        url : "/admin/deletebook",
        type : "POST",
        datatype:"json",
        data:JSON.stringify(sentdata),
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {

            }
        }
})};


