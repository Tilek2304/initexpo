document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseover', function() {
            this.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
        });

        card.addEventListener('mouseout', function() {
            this.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
        });
    });
});
