/**
 * WIDE Range Logistics LLC - Payment Page JS
 */
document.addEventListener('DOMContentLoaded', function () {
    // Interactive hover or focus states for payment cards
    const payCards = document.querySelectorAll('.pay-grid');
    payCards.forEach(card => {
        card.addEventListener('mouseenter', () => card.classList.add('hovered'));
        card.addEventListener('mouseleave', () => card.classList.remove('hovered'));
    });
});
