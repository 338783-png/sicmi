// Animation au défilement avancée
document.addEventListener('DOMContentLoaded', function() {
    // Configuration de l'Intersection Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Animation séquentielle pour les éléments de liste
                if (entry.target.classList.contains('service-card') || 
                    entry.target.classList.contains('project-card')) {
                    const delay = Array.from(entry.target.parentNode.children).indexOf(entry.target) * 100;
                    entry.target.style.transitionDelay = `${delay}ms`;
                }
            }
        });
    }, observerOptions);

    // Observer tous les éléments avec la classe fade-in
    document.querySelectorAll('.fade-in').forEach(element => {
        element.classList.add('fade-in');
        observer.observe(element);
    });

    // Navigation active améliorée
    function updateActiveNav() {
        const currentPage = window.location.pathname;
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('active');
            }
        });
    }

    updateActiveNav();

    // Bouton retour en haut
    const backToTopButton = document.getElementById('backToTop');

    if (backToTopButton) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopButton.style.display = 'block';
                setTimeout(() => {
                    backToTopButton.style.opacity = '1';
                    backToTopButton.style.transform = 'scale(1)';
                }, 10);
            } else {
                backToTopButton.style.opacity = '0';
                backToTopButton.style.transform = 'scale(0.8)';
                setTimeout(() => {
                    backToTopButton.style.display = 'none';
                }, 300);
            }
        });

        backToTopButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Animation des dropdowns
    const dropdowns = document.querySelectorAll('.dropdown');
    
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('show.bs.dropdown', function() {
            const menu = this.querySelector('.dropdown-menu');
            menu.style.opacity = '0';
            menu.style.transform = 'translateY(-10px) scale(0.95)';
        });
        
        dropdown.addEventListener('shown.bs.dropdown', function() {
            const menu = this.querySelector('.dropdown-menu');
            menu.style.opacity = '1';
            menu.style.transform = 'translateY(0) scale(1)';
            menu.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        });
    });

    // Filtrage des projets avec animation
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            
            // Animation des boutons
            filterButtons.forEach(btn => {
                btn.classList.remove('active');
                btn.style.transform = 'scale(1)';
            });
            this.classList.add('active');
            this.style.transform = 'scale(1.05)';
            
            // Filtrage avec animation
            projectItems.forEach((item, index) => {
                const categories = item.getAttribute('data-categories').split(' ');
                
                if (filter === 'all' || categories.includes(filter)) {
                    item.style.display = 'block';
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0) scale(1)';
                    }, index * 100);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(20px) scale(0.95)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // Formulaire de contact avec validation
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Simulation de l'envoi
            submitBtn.innerHTML = '<span class="loading-spinner"></span> Envoi en cours...';
            submitBtn.disabled = true;
            
            setTimeout(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }, 2000);
        });
    }

    // Compteurs animés
    function animateCounters() {
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const duration = 2000;
            const step = target / (duration / 16);
            let current = 0;
            
            const timer = setInterval(() => {
                current += step;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                counter.textContent = Math.floor(current).toLocaleString();
            }, 16);
        });
    }

    // Observer pour les compteurs
    const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                counterObserver.unobserve(entry.target);
            }
        });
    });

    document.querySelectorAll('.counter-section').forEach(section => {
        counterObserver.observe(section);
    });

    // Gestion des images lazy loading
    const imageObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.getAttribute('data-src');
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img.lazy').forEach(img => {
        imageObserver.observe(img);
    });
});

// Gestion du responsive menu
function toggleMobileMenu() {
    const navbar = document.getElementById('navbarNav');
    navbar.classList.toggle('show');
}

// Animation au défilement avancée
document.addEventListener('DOMContentLoaded', function() {
    // Configuration de l'Intersection Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Animation séquentielle pour les éléments de liste
                if (entry.target.classList.contains('service-card') || 
                    entry.target.classList.contains('project-card')) {
                    const delay = Array.from(entry.target.parentNode.children).indexOf(entry.target) * 100;
                    entry.target.style.transitionDelay = `${delay}ms`;
                }
            }
        });
    }, observerOptions);

    // Observer tous les éléments avec la classe fade-in
    document.querySelectorAll('.fade-in').forEach(element => {
        element.classList.add('fade-in');
        observer.observe(element);
    });

    // Navigation active améliorée
    function updateActiveNav() {
        const currentPage = window.location.pathname;
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('active');
            }
        });
    }

    updateActiveNav();

    // Bouton retour en haut
    const backToTopButton = document.getElementById('backToTop');

    if (backToTopButton) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopButton.style.display = 'block';
                setTimeout(() => {
                    backToTopButton.style.opacity = '1';
                    backToTopButton.style.transform = 'scale(1)';
                }, 10);
            } else {
                backToTopButton.style.opacity = '0';
                backToTopButton.style.transform = 'scale(0.8)';
                setTimeout(() => {
                    backToTopButton.style.display = 'none';
                }, 300);
            }
        });

        backToTopButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Animation des dropdowns
    const dropdowns = document.querySelectorAll('.dropdown');
    
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('show.bs.dropdown', function() {
            const menu = this.querySelector('.dropdown-menu');
            menu.style.opacity = '0';
            menu.style.transform = 'translateY(-10px) scale(0.95)';
        });
        
        dropdown.addEventListener('shown.bs.dropdown', function() {
            const menu = this.querySelector('.dropdown-menu');
            menu.style.opacity = '1';
            menu.style.transform = 'translateY(0) scale(1)';
            menu.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        });
    });

    // Filtrage des projets avec animation
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            
            // Animation des boutons
            filterButtons.forEach(btn => {
                btn.classList.remove('active');
                btn.style.transform = 'scale(1)';
            });
            this.classList.add('active');
            this.style.transform = 'scale(1.05)';
            
            // Filtrage avec animation
            projectItems.forEach((item, index) => {
                const categories = item.getAttribute('data-categories').split(' ');
                
                if (filter === 'all' || categories.includes(filter)) {
                    item.style.display = 'block';
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0) scale(1)';
                    }, index * 100);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(20px) scale(0.95)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // Formulaire de contact avec validation
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Simulation de l'envoi
            submitBtn.innerHTML = '<span class="loading-spinner"></span> Envoi en cours...';
            submitBtn.disabled = true;
            
            setTimeout(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }, 2000);
        });
    }

    // Compteurs animés
    function animateCounters() {
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const duration = 2000;
            const step = target / (duration / 16);
            let current = 0;
            
            const timer = setInterval(() => {
                current += step;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                counter.textContent = Math.floor(current).toLocaleString();
            }, 16);
        });
    }

    // Observer pour les compteurs
    const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                counterObserver.unobserve(entry.target);
            }
        });
    });

    document.querySelectorAll('.counter-section').forEach(section => {
        counterObserver.observe(section);
    });

    // Gestion des images lazy loading
    const imageObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.getAttribute('data-src');
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img.lazy').forEach(img => {
        imageObserver.observe(img);
    });

    // Gestion des backgrounds dynamiques
    initDynamicBackgrounds();
});

// Initialisation des backgrounds dynamiques
function initDynamicBackgrounds() {
    // Hero background slider
    const heroBackgrounds = document.querySelectorAll('.hero-slide');
    if (heroBackgrounds.length > 0) {
        let currentSlide = 0;
        
        function showNextSlide() {
            heroBackgrounds.forEach(slide => slide.classList.remove('active'));
            heroBackgrounds[currentSlide].classList.add('active');
            
            currentSlide = (currentSlide + 1) % heroBackgrounds.length;
        }
        
        // Changer de slide toutes les 5 secondes
        setInterval(showNextSlide, 5000);
        showNextSlide(); // Afficher le premier slide
    }

    // Service backgrounds
    const serviceBackgrounds = document.querySelectorAll('.service-background');
    serviceBackgrounds.forEach(background => {
        const imageUrl = background.getAttribute('data-background');
        if (imageUrl) {
            background.style.backgroundImage = `url('${imageUrl}')`;
        }
    });

    // Project backgrounds
    const projectBackgrounds = document.querySelectorAll('.project-background');
    projectBackgrounds.forEach(background => {
        const imageUrl = background.getAttribute('data-background');
        if (imageUrl) {
            background.style.backgroundImage = `url('${imageUrl}')`;
        }
    });
}

// Gestion du responsive menu
function toggleMobileMenu() {
    const navbar = document.getElementById('navbarNav');
    navbar.classList.toggle('show');
}

// Export des fonctions pour usage global
window.toggleMobileMenu = toggleMobileMenu;
window.initDynamicBackgrounds = initDynamicBackgrounds;

// Export des fonctions pour usage global
window.toggleMobileMenu = toggleMobileMenu;