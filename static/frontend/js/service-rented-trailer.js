/**
 * WIDE Range Logistics LLC - Services JS
 */
document.addEventListener('DOMContentLoaded', function () {
    // Highlight service block when hash matches
    if (window.location.hash) {
        const target = document.querySelector(window.location.hash);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
            target.classList.add('highlighted');
        }
    }
});
