
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
              if (book) {
                  var flag = true;
                  if(this.books){
                   for (i = 0; i < this.books.length; i++) {
                        if (this.books[i].name == book) {
                            that = this;
                            $('.books').find('#'+i).find('.count').slideToggle(200);
                            setTimeout(function(){that.books[i].count++;
                                        $('.books').find('#'+i).find('.count').slideToggle(200);
                            },200);
                            flag = false;
                            break;
                        }
                    }
                      if (flag){
                      this.books.push({ name: book ,count:1});
                         index =  this.books.length-1;
                  }
                  }else {
                      this.books = [{ name: book ,count:1}];
                      index =  this.books.length-1;;
                  }
                  addBook({name:book});
                this.newBook = ''
              }
            },



            removeBook: function (index) {
                var book = this.books[index];
                if (book) {
                     that = this;
                            $('.books').find('#'+index).find('.count').slideUp(200);
                            setTimeout(function(){book.count--;
                                        $('.books').find('#'+index).find('.count').slideDown(200);
                                      if (book.count == 0){
                                        $('.books').find('#'+index).slideUp(300);
                                        setTimeout(function(){that.books.splice(index, 1);
                                        }, 300);
                                    }
                            },200);
                    deleteBook({name: book.name});
                }}
          }
        });
    }
});
function addBook(sentdata){
    $.ajax({
        url : "/book/addbook",
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
        url : "/book/deletebook",
        type : "POST",
        datatype:"json",
        data:JSON.stringify(sentdata),
        contentType: 'application/json',
        success : function(mydata){
            if (mydata.status ==  1) {

            }
        }
})};

