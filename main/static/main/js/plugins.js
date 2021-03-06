/*global $, alert, console*/

$(function () {

    'use strict';

    var subnav      = $(".subnav"),
        nav         = $("nav"),
        navigation  = $(".navigation"),
        catSection  = $(".categories-links"),
        mainMenu    = $(".navigation ul .cat-link"),
        subMenu     = $(".sup-menu"),
        mobSearch   = $("nav i");

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
    
    navigation.css("top", nav.innerHeight());
    
    mainMenu.hover(function () {
        subMenu.fadeIn(300);
    }, function () {
        subMenu.fadeOut(300);
    });
    
    $(".contact-form form .form-group").each(function (i) {
        setTimeout(function () {
            $(".contact-form form .form-group").eq(i).css({
                opacity: 1,
                transform: "translateX(0)"
            });
        }, 150 * (i + 1));
    });
    
    // Shuffle
    $(".product-page .shuffle li").click(function () {
        $(this).addClass('active').siblings().removeClass('active');
        $(".product-page .image > div").hide();
        $($(this).data('class')).show();
        console.log($(this).data('class'));
    });
    
    
    /* Hamburger Active */
    $(".icon").click(function () {
        $(this).toggleClass('active');
        $(".nav-content .mlinks").slideToggle(300);
    });
    $(".cat-link").click(function () {
        $(".cat-link .sup-menu").slideToggle(300);
        console.log("YES");
    });
    $(".mobnav").css('top', nav.innerHeight());
    
    // Mob Search
    mobSearch.click(function () {
        $("nav .mob-search").fadeToggle(200);
    });
    /* Hamburger Active */
    /*$(".product-page .window .product .image img").resizable({
        containment: "#holder",
        aspectRatio: true
    });*/
    
    // Auto Slider
    
    (function selfCall() {
        
        $(".slider .active").each(function () {
        
            if (!$(this).is(":last-child")) {
           
                $(this).delay(3000).fadeOut(1000, function () {
                    
                    $(this).removeClass("active").next().addClass("active").fadeIn(1000);
                    
                    selfCall();
                });
                
            } else {
                
                $(this).delay(3000).fadeOut(1000, function () {
                    
                    $(this).removeClass("active");
                    
                    $(".slider div").eq(0).addClass("active").fadeIn(1000);
                    
                    selfCall();
                });
                
            }
        
        });
        
    }());

    /* Return Window width */
    function windowWidth() {
        return window.innerWidth;
    }

});
