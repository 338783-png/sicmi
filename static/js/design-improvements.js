// ============================================
// SICMI SARL - Design Improvements JS
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // SCROLL TO TOP BUTTON
    // ============================================
    const scrollToTopBtn = document.getElementById('scrollToTop');
    
    if (scrollToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                scrollToTopBtn.classList.add('show');
            } else {
                scrollToTopBtn.classList.remove('show');
            }
        });
        
        scrollToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // ============================================
    // SCROLL PROGRESS BAR
    // ============================================
    const scrollProgress = document.getElementById('scrollProgress');
    
    if (scrollProgress) {
        window.addEventListener('scroll', function() {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            scrollProgress.style.width = scrolled + '%';
        });
    }
    
    // ============================================
    // ANIMATED COUNTERS
    // ============================================
    const counters = document.querySelectorAll('.counter');
    
    const animateCounter = (counter) => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000; // 2 seconds
        const increment = target / (duration / 16); // 60fps
        let current = 0;
        
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        updateCounter();
    };
    
    // Intersection Observer pour les compteurs
    if (counters.length > 0) {
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                    animateCounter(entry.target);
                    entry.target.classList.add('counted');
                }
            });
        }, { threshold: 0.5 });
        
        counters.forEach(counter => counterObserver.observe(counter));
    }
    
    // ============================================
    // LAZY LOADING IMAGES
    // ============================================
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    if (lazyImages.length > 0) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => imageObserver.observe(img));
    }
    
    // ============================================
    // ANIMATE ON SCROLL (AOS)
    // ============================================
    const aosElements = document.querySelectorAll('[data-aos]');
    
    if (aosElements.length > 0) {
        const aosObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('aos-animate');
                }
            });
        }, { 
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        });
        
        aosElements.forEach(element => {
            element.classList.add('aos-init');
            aosObserver.observe(element);
        });
    }
    
    // ============================================
    // ENHANCED CARD EFFECTS
    // ============================================
    const cards = document.querySelectorAll('.card-enhanced, .hover-lift');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.zIndex = '10';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.zIndex = '1';
        });
    });
    
    // ============================================
    // NAVBAR HIDE/SHOW ON SCROLL
    // ============================================
    let lastScrollTop = 0;
    const navbar = document.querySelector('.navbar');
    const scrollThreshold = 100;
    
    if (navbar) {
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            if (scrollTop > scrollThreshold) {
                if (scrollTop > lastScrollTop) {
                    // Scroll down
                    navbar.style.transform = 'translateY(-100%)';
                } else {
                    // Scroll up
                    navbar.style.transform = 'translateY(0)';
                }
            }
            
            lastScrollTop = scrollTop;
        }, { passive: true });
    }
    
    // ============================================
    // SMOOTH REVEAL ANIMATIONS
    // ============================================
    const revealElements = document.querySelectorAll('.reveal');
    
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                }
            });
        }, { threshold: 0.15 });
        
        revealElements.forEach(element => revealObserver.observe(element));
    }
    
    // ============================================
    // PARALLAX EFFECT
    // ============================================
    const parallaxElements = document.querySelectorAll('.parallax');
    
    if (parallaxElements.length > 0) {
        window.addEventListener('scroll', function() {
            parallaxElements.forEach(element => {
                const speed = element.dataset.speed || 0.5;
                const yPos = -(window.pageYOffset * speed);
                element.style.backgroundPositionY = yPos + 'px';
            });
        }, { passive: true });
    }
    
    // ============================================
    // ENHANCED FORM VALIDATION
    // ============================================
    const forms = document.querySelectorAll('.needs-validation');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
        
        // Real-time validation
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                if (this.checkValidity()) {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                } else {
                    this.classList.remove('is-valid');
                    this.classList.add('is-invalid');
                }
            });
        });
    });
    
    // ============================================
    // COPY TO CLIPBOARD
    // ============================================
    const copyButtons = document.querySelectorAll('[data-copy]');
    
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const text = this.dataset.copy;
            navigator.clipboard.writeText(text).then(() => {
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-check me-2"></i>Copié!';
                this.classList.add('btn-success');
                
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.classList.remove('btn-success');
                }, 2000);
            });
        });
    });
    
    // ============================================
    // LOADING SKELETON -> REAL CONTENT
    // ============================================
    window.addEventListener('load', function() {
        const skeletons = document.querySelectorAll('.skeleton');
        skeletons.forEach(skeleton => {
            skeleton.classList.remove('skeleton');
        });
    });
    
    // ============================================
    // PERFORMANCE: REDUCE MOTION FOR ACCESSIBILITY
    // ============================================
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    
    if (prefersReducedMotion.matches) {
        // Disable animations
        document.querySelectorAll('[data-aos]').forEach(el => {
            el.removeAttribute('data-aos');
        });
        
        // Remove transition classes
        document.querySelectorAll('.float, .pulse').forEach(el => {
            el.classList.remove('float', 'pulse');
        });
    }
    
    // ============================================
    // CONSOLE MESSAGE
    // ============================================
    console.log('%c🏭 SICMI SARL', 'color: #0056b3; font-size: 24px; font-weight: bold;');
    console.log('%cIngénierie & Construction Industrielle', 'color: #6c757d; font-size: 14px;');
    console.log('%cSite développé avec ❤️', 'color: #28a745; font-size: 12px;');
    
});

// ============================================
// GLOBAL UTILITIES
// ============================================

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function for scroll events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}
