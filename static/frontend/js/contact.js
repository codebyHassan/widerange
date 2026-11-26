/**
 * WIDE Range Logistics LLC - Contact Page JS
 */
document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            // Optional front-end check
            const inputs = contactForm.querySelectorAll('input[required], textarea[required]');
            let valid = true;
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    valid = false;
                    input.style.borderColor = '#ef4444';
                } else {
                    input.style.borderColor = '';
                }
            });
            if (!valid) {
                e.preventDefault();
                alert('Please fill out all required fields.');
            }
        });
    }
});
