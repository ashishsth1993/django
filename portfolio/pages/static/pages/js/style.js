$(document).ready(function($){

    // Smooth Scrolling to particular Link
    const scrollLink = $('.scrollsmooth');
    scrollLink.click(function (e) {
        e.preventDefault();
        $('body,html').animate({
            scrollTop: $(this.hash).offset().top
        }, 600);
    });

    // Vertical Fixed Navigation Dotted Bar
    const contentSections = $('.cd-section');
    const navigationItems = $("#cd-vertical-nav ul li a");
    updateNavigation();
    $(window).on('scroll', function(){
        updateNavigation();
    });

    function updateNavigation() {
        contentSections.each(function(){
            const $this = $(this);
            const activeSection = $('#cd-vertical-nav ul li a[href="#'+$this.attr('id')+'"]').data('number') - 1;
            if ( ( $this.offset().top - $(window).height()/2 < $(window).scrollTop() ) && ( $this.offset().top + $this.height() - $(window).height()/2 > $(window).scrollTop() ) ) {
                navigationItems.eq(activeSection).addClass('is-selected');
            }else {
                navigationItems.eq(activeSection).removeClass('is-selected');
            }
        });
    }

    // Hamburger Menu Display
    const body = document.querySelector('body');
    const menu = document.querySelector('.menu-icon');

    function init() {
       applyListeners();
    }
    function applyListeners() {
        menu.addEventListener('click', function () {
            return toggleClass(body, 'nav-active');
        });
    }
    function toggleClass(element, stringClass) {
        if (element.classList.contains(stringClass))
            element.classList.remove(stringClass);
        else
            element.classList.add(stringClass);
    }
    init();

    const navLinks = document.querySelectorAll('#cd-ham-nav .nav__content ul li a');
    navLinks.forEach(navLink => {
        navLink.addEventListener('click', function () {
            return toggleClass(body, 'nav-active');
        })
    })

});

// Text Animation on Landing Page
class TypeWriter {
  constructor(txtElement, words, wait = 3000) {
    this.txtElement = txtElement;
    this.words = words;
    this.txt = '';
    this.wordIndex = 0;
    this.wait = parseInt(wait, 10);
    this.type();
    this.isDeleting = false;
  }
  type() {
    // Current index of word
    const current = this.wordIndex % this.words.length;
    // Get full text of current word
    const fullTxt = this.words[current];

    // Check if deleting
    if(this.isDeleting) {
      // Remove char
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      // Add char
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    // Insert txt into element
    this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

    // Initial Type Speed
    let typeSpeed = 100;

    if(this.isDeleting) {
      typeSpeed /= 2;
    }

    // If word is complete
    if(!this.isDeleting && this.txt === fullTxt) {
      // Make pause at end
      typeSpeed = this.wait;
      // Set delete to true
      this.isDeleting = true;
    } else if(this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      // Move to next word
      this.wordIndex++;
      // Pause before start typing
      typeSpeed = 500;
    }

    setTimeout(() => this.type(), typeSpeed);
  }
}
// Init On DOM Load
document.addEventListener('DOMContentLoaded', init);
// Init App
function init() {
    const txtElement = document.querySelector('.txt-type');
    const words = JSON.parse(txtElement.getAttribute('data-words'));
    const wait = txtElement.getAttribute('data-wait');
    // Init TypeWriter
    new TypeWriter(txtElement, words, wait);
}