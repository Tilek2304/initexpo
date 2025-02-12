// Устанавливаем дату для обратного отсчета (10 декабря 2024 года)
const countdownDate = new Date("Dec 10, 2024 00:00:00").getTime();

// Функция для обновления таймера каждую секунду
const timer = setInterval(function() {
  // Получаем текущую дату и время
  const now = new Date().getTime();

  // Вычисляем разницу между целевой датой и текущей
  const distance = countdownDate - now;

  // Если отсчет завершен
  if (distance < 0) {
    clearInterval(timer);
    document.querySelector('.timer__days .timer__value').textContent = "00";
    document.querySelector('.timer__hours .timer__value').textContent = "00";
    document.querySelector('.timer__minutes .timer__value').textContent = "00";
    document.querySelector('.timer__seconds .timer__value').textContent = "00";
    alert("Время истекло!");
    return;
  }

  // Вычисляем дни, часы, минуты и секунды
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Обновляем отображение на странице
  document.querySelector('.timer__days .timer__value').textContent = String(days).padStart(2, '0');
  document.querySelector('.timer__hours .timer__value').textContent = String(hours).padStart(2, '0');
  document.querySelector('.timer__minutes .timer__value').textContent = String(minutes).padStart(2, '0');
  document.querySelector('.timer__seconds .timer__value').textContent = String(seconds).padStart(2, '0');
}, 1000);
