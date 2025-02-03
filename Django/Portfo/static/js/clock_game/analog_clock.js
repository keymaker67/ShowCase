document.addEventListener("DOMContentLoaded", () => {
    // Analog Clock
    function updateClock() {
        const hourHand = document.querySelector('.analog-hour');
        const minuteHand = document.querySelector('.analog-minute');
        const secondHand = document.querySelector('.analog-second');
        const analogDigitalClock = document.querySelector('.analog-digital-clock')

        const now = new Date();
        const hours = now.getHours();
        const minutes = now.getMinutes();
        const seconds = now.getSeconds();
        analogDigitalClock.textContent = `${hours}:${minutes}:${seconds}`;

        // Calculate the angles
        const hoursAngle = 90 + (hours % 12) * 30 + minutes * 0.5; // 360° / 12 = 30° per hour, +0.5° for each minute
        const minutesAngle = 90 + minutes * 6 + seconds * 0.1;    // 360° / 60 = 6° per minute
        const secondsAngle = 90 + seconds * 6;                   // 360° / 60 = 6° per second

        // Apply the transformations
        hourHand.style.transform = `rotate(${hoursAngle}deg)`;
        minuteHand.style.transform = `rotate(${minutesAngle}deg)`;
        secondHand.style.transform = `rotate(${secondsAngle}deg)`;
    }

    // Update the clock every second
    setInterval(updateClock, 1000);

    // Initialize the clock immediately
    updateClock();
});