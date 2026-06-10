// Fullscreen Menu Toggle
const menuOverlay = document.getElementById('menuOverlay');
const openBtn = document.getElementById('openBtn');
const closeBtn = document.getElementById('closeBtn');

openBtn.addEventListener('click', () => {
    menuOverlay.classList.add('active');
});

closeBtn.addEventListener('click', () => {
    menuOverlay.classList.remove('active');
});

// Dynamic 3D Tilt Card Interaction
const cards = document.querySelectorAll('.safari-card');

cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left; // Mouse position X relative to card
        const y = e.clientY - rect.top;  // Mouse position Y relative to card
        
        const xc = rect.width / 2;       // Card center X
        const yc = rect.height / 2;      // Card center Y
        
        // Calculate tilt angles based on cursor offset from center
        const angleX = (yc - y) / 15;
        const angleY = (x - xc) / 15;
        
        // Apply smooth 3D rotation matrix
        card.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg) scale(1.02)`;
    });
    
    // Smooth reset when user moves cursor away
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
    });
});

