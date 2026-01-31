/**
 * SICMI Chatbot with AI-powered responses
 * Base de connaissances intelligente pour répondre aux questions
 */

// Base de connaissances SICMI
const knowledgeBase = {
    services: {
        keywords: ['service', 'services', 'faire', 'proposer', 'offrir', 'activité', 'activités', 'domaine', 'spécialité', 'métier'],
        response: `🔧 **Nos Services Principaux :**

**1. Constructions Neuves**
• Chaudronnerie industrielle
• Structures métalliques
• Tuyauterie industrielle
• Installation d'équipements

**2. Maintenance Industrielle**
• Maintenance préventive
• Maintenance corrective
• Diagnostic et dépannage
• Modernisation d'équipements

**3. Accompagnement Technique**
• Études et conseils
• Supervision de projets
• Formation du personnel

**4. Travaux de Façade & Rénovation**

Voulez-vous en savoir plus sur un service en particulier ?`
    },
    
    contact: {
        keywords: ['contact', 'contacter', 'appeler', 'téléphone', 'email', 'mail', 'joindre', 'WhatsApp', 'numéro'],
        response: `📞 **Contactez-nous :**

**Téléphone :**
• +237 675 948 524
• +237 687 013 563

**Email :**
• sicmisarl@gmail.com

**WhatsApp :**
• +237 675 948 524

**Adresse :**
• Bonabéri, Douala - Cameroun

Nous sommes disponibles du Lundi au Vendredi, 8h-17h.
Souhaitez-vous remplir notre formulaire de contact ?`
    },
    
    localisation: {
        keywords: ['où', 'situé', 'situation', 'localisation', 'adresse', 'lieu', 'trouver', 'emplacement'],
        response: `📍 **Notre Localisation :**

**Siège Social :**
Bonabéri, Douala
Cameroun

Nous intervenons dans tout le Cameroun et la sous-région d'Afrique Centrale.

Souhaitez-vous obtenir un itinéraire ou programmer une visite ?`
    },
    
    chaudronnerie: {
        keywords: ['chaudronnerie', 'chaudronner', 'métallique', 'métal', 'soudure', 'souder', 'acier', 'inox'],
        response: `🔨 **Chaudronnerie Industrielle :**

Nous réalisons :
• Fabrication de cuves et réservoirs
• Structures métalliques sur-mesure
• Tuyauterie industrielle
• Assemblage et soudure TIG/MIG
• Pièces métalliques complexes

**Matériaux :** Acier, Inox, Aluminium

Notre atelier est équipé de machines modernes pour garantir la qualité. 
Besoin d'un devis pour votre projet ?`
    },
    
    maintenance: {
        keywords: ['maintenance', 'entretien', 'dépannage', 'réparation', 'réparer', 'panne', 'préventif', 'correctif'],
        response: `🔧 **Maintenance Industrielle :**

**Maintenance Préventive :**
• Inspection régulière
• Graissage et réglages
• Remplacement programmé
• Optimisation des équipements

**Maintenance Corrective :**
• Intervention rapide 24/7
• Diagnostic expert
• Réparation sur site
• Pièces de rechange

Nous assurons la continuité de votre production.
Voulez-vous un contrat de maintenance ?`
    },
    
    devis: {
        keywords: ['devis', 'prix', 'coût', 'tarif', 'budget', 'estimation', 'combien', 'gratuit'],
        response: `💰 **Demande de Devis :**

Nous établissons des devis **GRATUITS** et détaillés pour tous vos projets.

**Information nécessaire :**
• Type de projet
• Dimensions/Quantités
• Matériaux souhaités
• Délais attendus

**Délai de réponse :** 24-48h

Je peux vous rediriger vers notre formulaire de contact ou voulez-vous discuter directement avec un conseiller ?`
    },
    
    atelier: {
        keywords: ['atelier', 'équipement', 'machine', 'usine', 'production', 'fabrication', 'capacité'],
        response: `🏭 **Nos Ateliers & Équipements :**

**Atelier d'Usinage :**
• Tours et fraiseuses CNC
• Rectifieuses
• Perceuses

**Atelier d'Assemblage :**
• Postes de soudure TIG/MIG/Arc
• Tables de montage
• Ponts roulants

**Atelier de Production :**
• Presses hydrauliques
• Machines de découpe
• Équipements de finition

Capacité : Pièces de 10kg à 5 tonnes.
Souhaitez-vous visiter nos installations ?`
    },
    
    projet: {
        keywords: ['projet', 'réalisation', 'référence', 'travaux', 'exemple', 'portfolio'],
        response: `📂 **Nos Réalisations :**

Nous avons réalisé plus de **100 projets** pour des clients industriels au Cameroun :

• Installation de lignes de production
• Fabrication de structures métalliques
• Maintenance d'usines
• Rénovation d'équipements

**Secteurs :**
Agroalimentaire, Pétrole & Gaz, BTP, Mines, Énergie

Voulez-vous consulter notre portfolio détaillé ?`
    },
    
    urgence: {
        keywords: ['urgent', 'urgence', 'rapide', 'vite', 'immédiat', 'maintenant', 'dépannage'],
        response: `🚨 **Service d'Urgence 24/7 :**

Pour les urgences, contactez-nous immédiatement :

**Hotline Urgence :**
📞 +237 675 948 524

**Intervention :**
• Diagnostic rapide
• Équipe disponible 24/7
• Mobilisation sous 2h
• Expertise sur site

Décrivez votre problème pour une assistance immédiate !`
    },
    
    equipe: {
        keywords: ['équipe', 'personnel', 'technicien', 'ingénieur', 'soudeur', 'compétence', 'qualification'],
        response: `👥 **Notre Équipe :**

**Personnel qualifié :**
• Ingénieurs expérimentés
• Techniciens certifiés
• Soudeurs qualifiés
• Chefs de projet

**Formation continue :**
Nos équipes sont formées aux dernières normes et technologies.

**Expérience :**
Plus de 15 ans d'expertise cumulée dans l'industrie.

Souhaitez-vous en savoir plus sur nos qualifications ?`
    },
    
    certification: {
        keywords: ['certification', 'norme', 'qualité', 'ISO', 'sécurité', 'QHSE'],
        response: `✅ **Certifications & Normes :**

**Engagement Qualité :**
• Respect des normes internationales
• Politique QHSE stricte
• Contrôle qualité systématique
• Traçabilité complète

**Sécurité :**
• Formation HSE du personnel
• Équipements de protection
• Procédures de sécurité

**Environnement :**
• Gestion responsable des déchets
• Engagement RSE

Voulez-vous consulter notre politique QHSE complète ?`
    }
};

// Réponses par défaut
const defaultResponses = [
    "Je ne suis pas sûr de comprendre votre question. Pouvez-vous la reformuler ?",
    "Désolé, je n'ai pas d'information précise sur ce sujet. Voulez-vous parler avec un conseiller ?",
    "Intéressant ! Pour une réponse précise, je vous recommande de contacter directement notre équipe au +237 675 948 524."
];

const greetings = {
    keywords: ['bonjour', 'salut', 'hello', 'bonsoir', 'hey', 'coucou', 'salutation'],
    responses: [
        "Bonjour ! 👋 Je suis l'assistant virtuel de SICMI SARL. Comment puis-je vous aider aujourd'hui ?",
        "Bonjour ! Ravi de vous accueillir. En quoi puis-je vous être utile ?",
        "Salut ! Je suis là pour répondre à vos questions sur nos services. Que souhaitez-vous savoir ?"
    ]
};

const thanks = {
    keywords: ['merci', 'thanks', 'thank', 'remercie', 'super', 'parfait', 'excellent'],
    responses: [
        "De rien ! 😊 N'hésitez pas si vous avez d'autres questions.",
        "Avec plaisir ! Je reste à votre disposition pour toute question.",
        "Content d'avoir pu vous aider ! Bonne journée ! 🌟"
    ]
};

/**
 * Analyse le message et trouve la meilleure réponse
 */
function analyzeMessage(message) {
    const lowerMessage = message.toLowerCase().trim();
    
    // Vérifier les salutations
    if (greetings.keywords.some(keyword => lowerMessage.includes(keyword))) {
        return greetings.responses[Math.floor(Math.random() * greetings.responses.length)];
    }
    
    // Vérifier les remerciements
    if (thanks.keywords.some(keyword => lowerMessage.includes(keyword))) {
        return thanks.responses[Math.floor(Math.random() * thanks.responses.length)];
    }
    
    // Chercher dans la base de connaissances
    let bestMatch = null;
    let maxScore = 0;
    
    for (const [topic, data] of Object.entries(knowledgeBase)) {
        const score = data.keywords.reduce((score, keyword) => {
            return score + (lowerMessage.includes(keyword) ? 1 : 0);
        }, 0);
        
        if (score > maxScore) {
            maxScore = score;
            bestMatch = data.response;
        }
    }
    
    // Si on a trouvé une correspondance
    if (maxScore > 0) {
        return bestMatch;
    }
    
    // Réponse par défaut
    return defaultResponses[Math.floor(Math.random() * defaultResponses.length)] +
           "\n\n**Questions fréquentes :**\n• Quels sont vos services ?\n• Comment vous contacter ?\n• Demander un devis";
}

/**
 * Suggestions intelligentes basées sur le contexte
 */
function getSmartSuggestions(lastResponse) {
    if (lastResponse.includes('Services')) {
        return ['Demander un devis', 'Voir les ateliers', 'Contact'];
    } else if (lastResponse.includes('Contact')) {
        return ['Formulaire contact', 'Services', 'Horaires'];
    } else if (lastResponse.includes('Devis')) {
        return ['Nos services', 'Contact direct', 'Délais'];
    } else {
        return ['Services', 'Contact', 'Localisation'];
    }
}

// Export pour utilisation
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { analyzeMessage, getSmartSuggestions };
}
