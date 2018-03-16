$(document).ready(function(){
    var path = $(location).attr('href');
    var page = path.split('/').reverse()[0];
    if(page === "") {
        $("#home").css("color", "#68b1ac")
    } else {
        $("#" + page).css("color", "#68b1ac")  
    }
});

$(document).ready(function(){
    $('#contact_container').show()
    $('.tab #contact').css("background", "#68b1ac").css("color", "white")
    $('.tab').on('click', '.tablinks', function() {
        $('.tablinks').css("background", "#f1f1f1").css("color", "black")
        $(this).css("background", "#68b1ac").css("color", "white")
        var active = $(this).attr('id')
        $('.tabcontent').hide()
        $('#' + active + '_container').show()
        console.log($('#' + active + '_container').siblings())
   })
});

$(document).ready(function(){
    if ($(window).width() < 640) {
        $('.nav_mobile').hide();
    }    
    $('nav').on('click', '#mobile_open', function() {
        $('#mobile_open').fadeOut()
        $('#mobile_close').show()
        $('.nav_mobile').slideDown();
   })
    $('nav').on('click', '#mobile_close', function() {
        $('#mobile_open').show()
        $('.logo').show()
        $('#mobile_close').hide()
        $('.nav_mobile').slideUp();
   })
});