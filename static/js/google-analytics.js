// ============================================
// SICMI SARL - Google Analytics Events
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // Vérifier si Google Analytics est chargé
    const isGALoaded = typeof gtag !== 'undefined';
    
    if (!isGALoaded) {
        console.log('📊 Google Analytics non chargé (mode développement ou bloqueur)');
        return;
    }
    
    // ============================================
    // TRACKING DES CLICS SUR BOUTONS CTA
    // ============================================
    const ctaButtons = document.querySelectorAll('a[href*="contact"], button[type="submit"], .btn-primary');
    
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const buttonText = this.textContent.trim() || 'Bouton CTA';
            const buttonHref = this.getAttribute('href') || 'submit';
            
            gtag('event', 'cta_click', {
                'event_category': 'Engagement',
                'event_label': buttonText,
                'value': buttonHref
            });
            
            console.log('📊 GA Event: CTA Click -', buttonText);
        });
    });
    
    // ============================================
    // TRACKING DES LIENS TÉLÉPHONE
    // ============================================
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');
    
    phoneLinks.forEach(link => {
        link.addEventListener('click', function() {
            const phoneNumber = this.getAttribute('href').replace('tel:', '');
            
            gtag('event', 'phone_click', {
                'event_category': 'Contact',
                'event_label': 'Appel téléphonique',
                'value': phoneNumber
            });
            
            console.log('📊 GA Event: Phone Click -', phoneNumber);
        });
    });
    
    // ============================================
    // TRACKING DES LIENS EMAIL
    // ============================================
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');
    
    emailLinks.forEach(link => {
        link.addEventListener('click', function() {
            const email = this.getAttribute('href').replace('mailto:', '');
            
            gtag('event', 'email_click', {
                'event_category': 'Contact',
                'event_label': 'Envoi email',
                'value': email
            });
            
            console.log('📊 GA Event: Email Click -', email);
        });
    });
    
    // ============================================
    // TRACKING DES SOUMISSIONS DE FORMULAIRE
    // ============================================
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const formName = this.getAttribute('name') || this.getAttribute('id') || 'Formulaire';
            const formAction = this.getAttribute('action') || window.location.pathname;
            
            gtag('event', 'form_submit', {
                'event_category': 'Lead Generation',
                'event_label': formName,
                'value': formAction
            });
            
            console.log('📊 GA Event: Form Submit -', formName);
        });
    });
    
    // ============================================
    // TRACKING DES CLICS SUR SERVICES
    // ============================================
    const serviceCards = document.querySelectorAll('.service-card, a[href*="/services/"]');
    
    serviceCards.forEach(card => {
        card.addEventListener('click', function() {
            const serviceName = this.querySelector('h3, h4, h5, .card-title')?.textContent.trim() || 'Service';
            
            gtag('event', 'service_view', {
                'event_category': 'Services',
                'event_label': serviceName
            });
            
            console.log('📊 GA Event: Service View -', serviceName);
        });
    });
    
    // ============================================
    // TRACKING DES CLICS SUR PROJETS/RÉALISATIONS
    // ============================================
    const projectCards = document.querySelectorAll('.project-card, a[href*="/projets/"]');
    
    projectCards.forEach(card => {
        card.addEventListener('click', function() {
            const projectName = this.querySelector('h3, h4, h5, .card-title')?.textContent.trim() || 'Projet';
            
            gtag('event', 'project_view', {
                'event_category': 'Réalisations',
                'event_label': projectName
            });
            
            console.log('📊 GA Event: Project View -', projectName);
        });
    });
    
    // ============================================
    // TRACKING DES CLICS SUR ATELIERS
    // ============================================
    const atelierCards = document.querySelectorAll('.atelier-card, a[href*="/ateliers/"]');
    
    atelierCards.forEach(card => {
        card.addEventListener('click', function() {
            const atelierName = this.querySelector('h3, h4, h5, .card-title')?.textContent.trim() || 'Atelier';
            
            gtag('event', 'atelier_view', {
                'event_category': 'Ateliers',
                'event_label': atelierName
            });
            
            console.log('📊 GA Event: Atelier View -', atelierName);
        });
    });
    
    // ============================================
    // TRACKING DU TEMPS PASSÉ SUR LA PAGE
    // ============================================
    let startTime = Date.now();
    let timeSpent = 0;
    let tracked30s = false;
    let tracked60s = false;
    let tracked120s = false;
    
    function trackTimeOnPage() {
        timeSpent = Math.floor((Date.now() - startTime) / 1000);
        
        if (timeSpent >= 30 && !tracked30s) {
            gtag('event', 'time_on_page', {
                'event_category': 'Engagement',
                'event_label': '30 secondes',
                'value': 30
            });
            tracked30s = true;
            console.log('📊 GA Event: 30s sur la page');
        }
        
        if (timeSpent >= 60 && !tracked60s) {
            gtag('event', 'time_on_page', {
                'event_category': 'Engagement',
                'event_label': '1 minute',
                'value': 60
            });
            tracked60s = true;
            console.log('📊 GA Event: 60s sur la page');
        }
        
        if (timeSpent >= 120 && !tracked120s) {
            gtag('event', 'time_on_page', {
                'event_category': 'Engagement',
                'event_label': '2 minutes',
                'value': 120
            });
            tracked120s = true;
            console.log('📊 GA Event: 120s sur la page');
        }
    }
    
    setInterval(trackTimeOnPage, 5000);
    
    // ============================================
    // TRACKING DE LA PROFONDEUR DE SCROLL
    // ============================================
    let scrollDepths = [25, 50, 75, 90, 100];
    let scrollTracked = [];
    
    function trackScrollDepth() {
        const scrollPercent = Math.round(
            ((window.scrollY + window.innerHeight) / document.documentElement.scrollHeight) * 100
        );
        
        scrollDepths.forEach(depth => {
            if (scrollPercent >= depth && !scrollTracked.includes(depth)) {
                gtag('event', 'scroll_depth', {
                    'event_category': 'Engagement',
                    'event_label': depth + '%',
                    'value': depth
                });
                scrollTracked.push(depth);
                console.log('📊 GA Event: Scroll', depth + '%');
            }
        });
    }
    
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(trackScrollDepth, 150);
    }, { passive: true });
    
    // ============================================
    // TRACKING DES LIENS EXTERNES
    // ============================================
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.hostname + '"])');
    
    externalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const url = this.getAttribute('href');
            
            gtag('event', 'outbound_link', {
                'event_category': 'Navigation',
                'event_label': url,
                'transport_type': 'beacon'
            });
            
            console.log('📊 GA Event: Lien externe -', url);
        });
    });
    
    // ============================================
    // TRACKING DES TÉLÉCHARGEMENTS
    // ============================================
    const downloadLinks = document.querySelectorAll('a[href$=".pdf"], a[href$=".doc"], a[href$=".docx"], a[href*="download"]');
    
    downloadLinks.forEach(link => {
        link.addEventListener('click', function() {
            const fileName = this.getAttribute('href').split('/').pop();
            
            gtag('event', 'file_download', {
                'event_category': 'Downloads',
                'event_label': fileName
            });
            
            console.log('📊 GA Event: Téléchargement -', fileName);
        });
    });
    
    // ============================================
    // TRACKING DES ERREURS 404
    // ============================================
    if (document.title.includes('404') || document.body.textContent.includes('Page non trouvée')) {
        gtag('event', 'page_not_found', {
            'event_category': 'Erreurs',
            'event_label': window.location.pathname
        });
        console.log('📊 GA Event: 404 -', window.location.pathname);
    }
    
    // ============================================
    // TRACKING DES INTERACTIONS CHATBOT
    // ============================================
    const chatToggle = document.querySelector('#chatToggle, .chat-toggle');
    
    if (chatToggle) {
        chatToggle.addEventListener('click', function() {
            gtag('event', 'chatbot_open', {
                'event_category': 'Engagement',
                'event_label': 'Ouverture chatbot'
            });
            console.log('📊 GA Event: Chatbot ouvert');
        });
    }
    
    // ============================================
    // TRACKING DE LA VITESSE DE CHARGEMENT
    // ============================================
    window.addEventListener('load', function() {
        setTimeout(function() {
            if ('performance' in window && 'getEntriesByType' in performance) {
                const perfData = performance.getEntriesByType('navigation')[0];
                const loadTime = Math.round(perfData.loadEventEnd - perfData.loadEventStart);
                
                gtag('event', 'page_load_time', {
                    'event_category': 'Performance',
                    'event_label': window.location.pathname,
                    'value': loadTime
                });
                
                console.log('📊 GA Event: Temps de chargement -', loadTime + 'ms');
            }
        }, 0);
    });
    
    // ============================================
    // TRACKING DES RECHERCHES
    // ============================================
    const searchForms = document.querySelectorAll('form[action*="search"], input[type="search"]');
    
    searchForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const searchInput = this.querySelector('input[type="search"], input[name="q"]');
            const searchTerm = searchInput ? searchInput.value : '';
            
            if (searchTerm) {
                gtag('event', 'search', {
                    'event_category': 'Recherche',
                    'search_term': searchTerm
                });
                
                console.log('📊 GA Event: Recherche -', searchTerm);
            }
        });
    });
    
    // ============================================
    // TRACKING DES CLICS SUR LIENS SOCIAUX
    // ============================================
    const socialLinks = document.querySelectorAll('a[href*="facebook.com"], a[href*="linkedin.com"], a[href*="twitter.com"], a[href*="instagram.com"]');
    
    socialLinks.forEach(link => {
        link.addEventListener('click', function() {
            const platform = this.getAttribute('href').match(/(facebook|linkedin|twitter|instagram)/)[0];
            
            gtag('event', 'social_click', {
                'event_category': 'Réseaux Sociaux',
                'event_label': platform
            });
            
            console.log('📊 GA Event: Réseau social -', platform);
        });
    });
    
    // ============================================
    // TRACKING DES VISIBILITÉS (IMPRESSION)
    // ============================================
    const impressionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.gaTracked) {
                const elementName = entry.target.dataset.gaName || entry.target.textContent.substring(0, 50);
                
                gtag('event', 'element_view', {
                    'event_category': 'Impressions',
                    'event_label': elementName
                });
                
                entry.target.dataset.gaTracked = 'true';
                console.log('📊 GA Event: Element visible -', elementName);
            }
        });
    }, { threshold: 0.5 });
    
    // Tracker les éléments importants
    document.querySelectorAll('[data-ga-track]').forEach(el => {
        impressionObserver.observe(el);
    });
    
    // ============================================
    // TRACKING AVANT QUITTER LA PAGE
    // ============================================
    window.addEventListener('beforeunload', function() {
        const finalTimeSpent = Math.floor((Date.now() - startTime) / 1000);
        
        gtag('event', 'session_duration', {
            'event_category': 'Engagement',
            'event_label': 'Durée totale',
            'value': finalTimeSpent,
            'transport_type': 'beacon'
        });
        
        console.log('📊 GA Event: Session terminée -', finalTimeSpent + 's');
    });
    
    console.log('✅ Google Analytics Events configurés');
});
