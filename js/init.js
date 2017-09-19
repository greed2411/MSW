AOS.init();

(function ($) {
  $(function () {

    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('.scrollspy').scrollSpy();

    $('#introtext').typeIt({
      strings: ["Mechatronics.", "Machine Learning."],
      speed: 50,
      breakLines: false,
      autoStart: false,
      loop: true,
      deleteDelay: 2000,
      loopDelay: 2000,
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space

