// This code helps with being able to use the hamburger menu
$(document).on('click', '.headerburgerMenubutton, .header__layer', function() {
    $('header').toggleClass('menuOpen');
  });