$(document).ready(function(){
    var path = $(location).attr('href');
    var page = path.split('/').reverse()[0];
    if(page === "") {
        $("#home").css("color", "#68b1ac")
    } else {
        $("#" + page).css("color", "#68b1ac")  
    }
});