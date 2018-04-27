/*global $, alert, console*/

$(function () {

    'use strict';

    var subnav = $(".subnav"),
        nav = $("nav"),
        catSection = $(".categories-links");

    $(window).on("scroll", function () {
        var sc = $(this).scrollTop();

        /*if (sc >= (catSection.innerHeight() - nav.innerHeight())) {
            subnav.addClass('fixed');
        } else {
            subnav.removeClass('fixed');
        }*/
        if (sc >= (catSection.innerHeight() - nav.innerHeight())) {
            subnav.find('p').fadeOut(400);
            subnav.find('i').addClass('fixed');
        } else {
            subnav.find('p').fadeIn(400);
            subnav.find('i').removeClass('fixed');
        }
    });
    
    /*$(".product-page .window .product .image img").resizable({
        containment: "#holder",
        aspectRatio: true
    });*/

});
