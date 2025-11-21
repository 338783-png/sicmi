// ============================================
// SICMI SARL - Mobile Optimizations JS
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // DETECT MOBILE DEVICE
    // ============================================
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    const isIOS = /iPhone|iPad|iPod/i.test(navigator.userAgent);
    const isAndroid = /Android/i.test(navigator.userAgent);
    
    if (isMobile) {
        document.body.classList.add('is-mobile');
    }
    
    if (isIOS) {
        document.body.classList.add('is-ios');
    }
    
    if (isAndroid) {
        document.body.classList.add('is-android');
    }
    
    // ============================================
    // MOBILE MENU AUTO-CLOSE
    // ============================================
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link:not(.dropdown-toggle)');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth < 992 && navbarCollapse.classList.contains('show')) {
                const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                    toggle: true
                });
            }
        });
    });
    
    // ============================================
    // TOUCH FEEDBACK FOR BUTTONS
    // ============================================
    const touchButtons = document.querySelectorAll('.btn, .card, a');
    
    touchButtons.forEach(button => {
        button.addEventListener('touchstart', function() {
            this.style.opacity = '0.8';
        }, { passive: true });
        
        button.addEventListener('touchend', function() {
            this.style.opacity = '1';
        }, { passive: true });
    });
    
    // ============================================
    // PREVENT ZOOM ON INPUT FOCUS (iOS)
    // ============================================
    if (isIOS) {
        const inputs = document.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            if (input.style.fontSize < '16px') {
                input.style.fontSize = '16px';
            }
        });
    }
    
    // ============================================
    // SWIPE GESTURES FOR GALLERIES
    // ============================================
    const swipeableElements = document.querySelectorAll('.swipeable, .carousel');
    
    swipeableElements.forEach(element => {
        let touchStartX = 0;
        let touchEndX = 0;
        
        element.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });
        
        element.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe(element);
        }, { passive: true });
        
        function handleSwipe(el) {
            const swipeThreshold = 50;
            const diff = touchStartX - touchEndX;
            
            if (Math.abs(diff) > swipeThreshold) {
                if (diff > 0) {
                    // Swipe left
                    el.dispatchEvent(new CustomEvent('swipeleft'));
                } else {
                    // Swipe right
                    el.dispatchEvent(new CustomEvent('swiperight'));
                }
            }
        }
    });
    
    // ============================================
    // IMPROVE SCROLL PERFORMANCE ON MOBILE
    // ============================================
    let scrollTimeout;
    let isScrolling = false;
    
    window.addEventListener('scroll', () => {
        if (!isScrolling) {
            document.body.classList.add('is-scrolling');
            isScrolling = true;
        }
        
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
            document.body.classList.remove('is-scrolling');
            isScrolling = false;
        }, 150);
    }, { passive: true });
    
    // ============================================
    // OPTIMIZE IMAGES FOR MOBILE
    // ============================================
    if (isMobile && window.innerWidth < 768) {
        const images = document.querySelectorAll('img');
        images.forEach(img => {
            // Lazy load images
            if ('loading' in HTMLImageElement.prototype) {
                img.loading = 'lazy';
            }
            
            // Reduce quality for mobile
            if (img.src && !img.dataset.mobileOptimized) {
                img.dataset.mobileOptimized = 'true';
            }
        });
    }
    
    // ============================================
    // DOUBLE TAP TO ZOOM PREVENTION
    // ============================================
    let lastTouchEnd = 0;
    document.addEventListener('touchend', (e) => {
        const now = Date.now();
        if (now - lastTouchEnd <= 300) {
            e.preventDefault();
        }
        lastTouchEnd = now;
    }, { passive: false });
    
    // ============================================
    // ORIENTATION CHANGE HANDLER
    // ============================================
    window.addEventListener('orientationchange', () => {
        // Refresh layout after orientation change
        setTimeout(() => {
            window.scrollTo(0, window.scrollY + 1);
            window.scrollTo(0, window.scrollY - 1);
        }, 100);
    });
    
    // ============================================
    // MOBILE MENU ENHANCEMENTS
    // ============================================
    const navbarToggler = document.querySelector('.navbar-toggler');
    
    if (navbarToggler && isMobile) {
        navbarToggler.addEventListener('click', function() {
            // Add haptic feedback on supported devices
            if ('vibrate' in navigator) {
                navigator.vibrate(10);
            }
            
            this.classList.toggle('active');
        });
    }
    
    // ============================================
    // PULL TO REFRESH (disabled for web app)
    // ============================================
    if (isMobile) {
        document.body.style.overscrollBehavior = 'none';
    }
    
    // ============================================
    // OPTIMIZE ANIMATIONS ON MOBILE
    // ============================================
    if (isMobile && window.innerWidth < 768) {
        // Reduce animation complexity
        const animatedElements = document.querySelectorAll('[data-aos]');
        animatedElements.forEach(el => {
            const currentAnimation = el.getAttribute('data-aos');
            // Simplify to fade only
            if (currentAnimation && currentAnimation.includes('slide')) {
                el.setAttribute('data-aos', 'fade-up');
            }
            // Reduce duration
            if (!el.hasAttribute('data-aos-duration')) {
                el.setAttribute('data-aos-duration', '400');
            }
        });
    }
    
    // ============================================
    // MOBILE VIEWPORT HEIGHT FIX (iOS)
    // ============================================
    function setMobileViewportHeight() {
        const vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
    }
    
    if (isMobile) {
        setMobileViewportHeight();
        window.addEventListener('resize', setMobileViewportHeight);
        window.addEventListener('orientationchange', setMobileViewportHeight);
    }
    
    // ============================================
    // TELEPHONE LINKS AUTO-FORMATTING
    // ============================================
    if (isMobile) {
        const phoneNumbers = document.querySelectorAll('[href^="tel:"]');
        phoneNumbers.forEach(link => {
            link.addEventListener('click', function() {
                if ('vibrate' in navigator) {
                    navigator.vibrate(20);
                }
            });
        });
    }
    
    // ============================================
    // IMPROVE FORM USABILITY ON MOBILE
    // ============================================
    if (isMobile) {
        const forms = document.querySelectorAll('form');
        
        forms.forEach(form => {
            // Auto-scroll to active input
            const inputs = form.querySelectorAll('input, textarea, select');
            
            inputs.forEach(input => {
                input.addEventListener('focus', function() {
                    setTimeout(() => {
                        this.scrollIntoView({
                            behavior: 'smooth',
                            block: 'center'
                        });
                    }, 300);
                });
            });
        });
    }
    
    // ============================================
    // NETWORK DETECTION
    // ============================================
    if ('connection' in navigator) {
        const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
        
        function handleConnectionChange() {
            if (connection.effectiveType === 'slow-2g' || connection.effectiveType === '2g') {
                document.body.classList.add('slow-connection');
                // Disable heavy animations
                document.querySelectorAll('[data-aos]').forEach(el => {
                    el.removeAttribute('data-aos');
                });
            } else {
                document.body.classList.remove('slow-connection');
            }
        }
        
        connection.addEventListener('change', handleConnectionChange);
        handleConnectionChange();
    }
    
    // ============================================
    // MOBILE SHARE API
    // ============================================
    const shareButtons = document.querySelectorAll('[data-share]');
    
    if (navigator.share && shareButtons.length > 0) {
        shareButtons.forEach(button => {
            button.style.display = 'inline-block';
            
            button.addEventListener('click', async function() {
                try {
                    await navigator.share({
                        title: document.title,
                        text: 'Découvrez SICMI SARL',
                        url: window.location.href
                    });
                } catch (err) {
                    console.log('Erreur de partage:', err);
                }
            });
        });
    } else {
        shareButtons.forEach(button => {
            button.style.display = 'none';
        });
    }
    
    // ============================================
    // PREVENT BOUNCE SCROLL ON IOS
    // ============================================
    if (isIOS) {
        let startY = 0;
        
        document.addEventListener('touchstart', (e) => {
            startY = e.touches[0].pageY;
        }, { passive: true });
        
        document.addEventListener('touchmove', (e) => {
            const y = e.touches[0].pageY;
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const isAtTop = scrollTop <= 0;
            const isAtBottom = scrollTop + window.innerHeight >= document.body.scrollHeight;
            
            if ((isAtTop && y > startY) || (isAtBottom && y < startY)) {
                e.preventDefault();
            }
        }, { passive: false });
    }
    
    // ============================================
    // MOBILE PERFORMANCE MONITORING
    // ============================================
    if (isMobile && 'performance' in window) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                const perfData = performance.getEntriesByType('navigation')[0];
                const loadTime = perfData.loadEventEnd - perfData.loadEventStart;
                
                if (loadTime > 3000) {
                    console.warn('⚠️ Temps de chargement lent détecté:', loadTime + 'ms');
                    // Optimiser pour les prochaines visites
                    localStorage.setItem('slowLoad', 'true');
                }
            }, 0);
        });
    }
    
    // ============================================
    // CONSOLE LOG MOBILE INFO
    // ============================================
    console.log('📱 Mode Mobile:', isMobile);
    console.log('📱 iOS:', isIOS);
    console.log('📱 Android:', isAndroid);
    console.log('📱 Largeur écran:', window.innerWidth + 'px');
    console.log('📱 Hauteur écran:', window.innerHeight + 'px');
    console.log('📱 Ratio pixel:', window.devicePixelRatio);
    
});
