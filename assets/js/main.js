/**
* Template Name: Constructify
* Template URL: https://bootstrapmade.com/constructify-bootstrap-construction-website-template/
* Updated: Feb 11 2026 with Bootstrap v5.3.8
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    if (mobileNavToggleBtn) {
      mobileNavToggleBtn.classList.toggle('bi-list');
      mobileNavToggleBtn.classList.toggle('bi-x');
    }
  }
  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToogle);
  }

  /**
   * Close mobile nav on backdrop click
   */
  const navmenuOverlay = document.querySelector('#navmenu');
  if (navmenuOverlay) {
    navmenuOverlay.addEventListener('click', function(e) {
      if (document.querySelector('.mobile-nav-active') && e.target === this) {
        mobileNavToogle();
      }
    });
  }

  /**
   * Hide mobile nav on clicking navigation links (excluding dropdown toggles)
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        if (navmenu.getAttribute('href') === '#' || navmenu.parentElement.classList.contains('dropdown')) {
          return;
        }
        mobileNavToogle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns on clicking the parent link or icon
   */
  document.querySelectorAll('.navmenu .dropdown > a').forEach(dropdownLink => {
    dropdownLink.addEventListener('click', function(e) {
      if (document.querySelector('.mobile-nav-active')) {
        e.preventDefault();
        this.classList.toggle('active');
        const submenu = this.nextElementSibling;
        if (submenu) {
          submenu.classList.toggle('dropdown-active');
        }
        e.stopImmediatePropagation();
      }
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate Pure Counter
   */
  if (typeof PureCounter !== 'undefined') {
    new PureCounter();
  }

  /**
   * Init isotope layout and filters
   */
  if (typeof Isotope !== 'undefined' && typeof imagesLoaded !== 'undefined') {
    document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
      let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
      let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
      let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

      let container = isotopeItem.querySelector('.isotope-container');
      if (container) {
        imagesLoaded(container, function() {
          let initIsotope = new Isotope(container, {
            itemSelector: '.isotope-item',
            layoutMode: layout,
            filter: filter,
            sortBy: sort
          });

          isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
            filters.addEventListener('click', function() {
              isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
              this.classList.add('filter-active');
              initIsotope.arrange({
                filter: this.getAttribute('data-filter')
              });
              if (typeof aosInit === 'function') {
                aosInit();
              }
            }, false);
          });
        });
      }
    });
  }

  /**
   * Initiate glightbox
   */
  if (typeof GLightbox !== 'undefined') {
    const glightbox = GLightbox({
      selector: '.glightbox'
    });
  }

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      if (swiperElement.swiper) {
        return; // Already initialized
      }

      let configElement = swiperElement.querySelector(".swiper-config");
      if (!configElement) return;

      let config = {};
      try {
        config = JSON.parse(configElement.innerHTML.trim());
      } catch (err) {
        console.error("Swiper config parse error:", err);
        return;
      }

      // Auto-scope navigation buttons to this specific slider if present
      if (config.navigation) {
        const nextBtn = swiperElement.querySelector(".swiper-button-next") || (swiperElement.parentElement ? swiperElement.parentElement.querySelector(".swiper-button-next") : null);
        const prevBtn = swiperElement.querySelector(".swiper-button-prev") || (swiperElement.parentElement ? swiperElement.parentElement.querySelector(".swiper-button-prev") : null);
        if (nextBtn) config.navigation.nextEl = nextBtn;
        if (prevBtn) config.navigation.prevEl = prevBtn;
      }

      // Auto-scope pagination element
      if (config.pagination && typeof config.pagination.el === "string") {
        const pag = swiperElement.querySelector(config.pagination.el) || (swiperElement.parentElement ? swiperElement.parentElement.querySelector(config.pagination.el) : null);
        if (pag) config.pagination.el = pag;
      }

      let swiperInstance;
      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        swiperInstance = new Swiper(swiperElement, config);
      }

      // Direct click listeners to GUARANTEE previous and next buttons always work
      if (swiperInstance) {
        const next = swiperElement.querySelector(".swiper-button-next") || (swiperElement.parentElement ? swiperElement.parentElement.querySelector(".swiper-button-next") : null);
        const prev = swiperElement.querySelector(".swiper-button-prev") || (swiperElement.parentElement ? swiperElement.parentElement.querySelector(".swiper-button-prev") : null);

        if (next) {
          next.style.cursor = "pointer";
          next.addEventListener("click", function(e) {
            e.preventDefault();
            e.stopPropagation();
            swiperInstance.slideNext();
          });
        }
        if (prev) {
          prev.style.cursor = "pointer";
          prev.addEventListener("click", function(e) {
            e.preventDefault();
            e.stopPropagation();
            swiperInstance.slidePrev();
          });
        }
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initSwiper);
  } else {
    initSwiper();
  }
  window.addEventListener("load", initSwiper);

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle, .faq-item .faq-header').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

  /**
   * Contact Form Handler - WhatsApp & Instant Confirmation
   */
  document.querySelectorAll('.php-email-form').forEach(form => {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      e.stopImmediatePropagation();

      const loading = form.querySelector('.loading');
      const sentMessage = form.querySelector('.sent-message');
      const errorMessage = form.querySelector('.error-message');

      if (loading) loading.classList.add('d-block');
      if (errorMessage) errorMessage.classList.remove('d-block');
      if (sentMessage) sentMessage.classList.remove('d-block');

      const formData = new FormData(form);
      const name = formData.get('name') || '';
      const email = formData.get('email') || '';
      const phone = formData.get('phone') || '';
      const service = formData.get('service') || '';
      const subject = formData.get('subject') || '';
      const message = formData.get('message') || '';

      const waText = encodeURIComponent(
        `*Konsultasi Proyek Ducting HVAC*\n\n` +
        `• *Nama:* ${name}\n` +
        `• *Email:* ${email}\n` +
        `• *No. Telp:* ${phone}\n` +
        `• *Layanan:* ${service}\n` +
        `• *Subjek/Proyek:* ${subject}\n` +
        `• *Pesan:* ${message}`
      );

      setTimeout(function() {
        if (loading) loading.classList.remove('d-block');
        if (sentMessage) sentMessage.classList.add('d-block');
        form.reset();
        window.open('https://wa.me/6285210620252?text=' + waText, '_blank');
      }, 500);
    }, true);
  });

})();