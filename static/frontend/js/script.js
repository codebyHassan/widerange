/**
 * WIDE Range Logistics LLC - Main JavaScript
 */
document.addEventListener('DOMContentLoaded', function () {
    // 1. Mobile Menu Toggle
    const mobileToggle = document.getElementById('mobileToggle');
    const navContent = document.getElementById('navContent');

    if (mobileToggle && navContent) {
        mobileToggle.addEventListener('click', function (e) {
            e.stopPropagation();
            mobileToggle.classList.toggle('active');
            navContent.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', function (e) {
            if (!navContent.contains(e.target) && !mobileToggle.contains(e.target)) {
                mobileToggle.classList.remove('active');
                navContent.classList.remove('active');
            }
        });
    }

    // 2. Mobile Dropdown Toggle
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(function (dropdown) {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        if (toggle) {
            toggle.addEventListener('click', function (e) {
                if (window.innerWidth <= 992) {
                    e.preventDefault();
                    dropdown.classList.toggle('open');
                }
            });
        }
    });

    // 3. Testimonial Carousel (Home Page)
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const carouselContainer = document.querySelector('.testimonial-carousel');

    if (testimonialCards.length > 0) {
        let currentIndex = 0;

        function showTestimonial(index) {
            if (index < 0) {
                currentIndex = testimonialCards.length - 1;
            } else if (index >= testimonialCards.length) {
                currentIndex = 0;
            } else {
                currentIndex = index;
            }

            testimonialCards.forEach((card, idx) => {
                if (idx === currentIndex) {
                    card.classList.add('active');
                    card.style.display = 'grid';
                } else {
                    card.classList.remove('active');
                    card.style.display = 'none';
                }
            });
        }

        // Initialize first slide
        showTestimonial(0);

        if (prevBtn) {
            prevBtn.addEventListener('click', function () {
                showTestimonial(currentIndex - 1);
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', function () {
                showTestimonial(currentIndex + 1);
            });
        }

        // Auto-play every 6 seconds
        let autoPlay = setInterval(function () {
            showTestimonial(currentIndex + 1);
        }, 6000);

        if (carouselContainer) {
            carouselContainer.addEventListener('mouseenter', () => clearInterval(autoPlay));
            carouselContainer.addEventListener('mouseleave', () => {
                clearInterval(autoPlay);
                autoPlay = setInterval(function () {
                    showTestimonial(currentIndex + 1);
                }, 6000);
            });
        }
    }

    // 4. Scroll Reveal Animation for .reveal and .fade-on-view elements
    const revealElements = document.querySelectorAll('.reveal, .fade-on-view, .fade-in-start');
    if ('IntersectionObserver' in window && revealElements.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-visible', 'active');
                }
            });
        }, { threshold: 0.1 });

        revealElements.forEach(el => observer.observe(el));
    } else {
        revealElements.forEach(el => el.classList.add('fade-in-visible', 'active'));
    }

    // 5. Smooth scroll for in-page anchors
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId && targetId !== '#') {
                const target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });
                    // Close mobile nav if open
                    if (navContent && navContent.classList.contains('active')) {
                        navContent.classList.remove('active');
                        if (mobileToggle) mobileToggle.classList.remove('active');
                    }
                }
            }
        });
    });
});
