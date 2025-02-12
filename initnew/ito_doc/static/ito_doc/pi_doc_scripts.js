document.addEventListener('DOMContentLoaded', function() {
    console.log('Pi Doc script loaded');
    // Добавить обработчик события для кнопок с классом 'btn'
    document.querySelectorAll('.btn').forEach(function(button) {
        button.addEventListener('click', function() {
            alert('Button clicked!');
        });
    });
});
