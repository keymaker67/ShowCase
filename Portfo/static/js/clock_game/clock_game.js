document.addEventListener("DOMContentLoaded", () => {
    const startButton = document.getElementById("startButton");
    const gameTypeSection = document.getElementById("gameTypeSection");
    const clockGameSpace = document.getElementById("clockGameSpace");
    const clockGameTitle = document.getElementById("clockGameTitle");
    const correctAnswer = document.getElementById("correctAnswer");
    const startGame = document.getElementById("startGame");
    const answer = document.getElementById("answer");
    const hourHand1 = document.querySelector('.analog-clock-1 .analog-hour ');
    const minuteHand1 = document.querySelector('.analog-clock-1 .analog-minute');
    const hourHand2 = document.querySelector('.analog-clock-2 .analog-hour');
    const minuteHand2 = document.querySelector('.analog-clock-2 .analog-minute');

    const gameType1 = document.getElementById("gameType1")
    const gameType2 = document.getElementById("gameType2")
    const gameType3 = document.getElementById("gameType3")
    const gameType4 = document.getElementById("gameType4")

    // let numPlayers;
    const gameType = [
        null,
        'Saat kaç',
        'Saat Kaçta gelir misin?',
        'Saat Kaçtan Kaça Kadar',
    ];

    // Start Button Click Event
    startButton.addEventListener("click", () => {
        shader(startButton, gameTypeSection)
    });

    // Game Type Event
    gameType1.addEventListener("click", () => {
        clockGameTitle.innerText = gameType[1]
        startGameEvent(1)
        shader(gameTypeSection, clockGameSpace);
    });

    gameType2.addEventListener("click", () => {
        clockGameTitle.innerText = gameType[2]
        startGameEvent(2)
        shader(gameTypeSection, clockGameSpace);
    });

    gameType3.addEventListener("click", () => {
        clockGameTitle.innerText = gameType[3]
        startGameEvent(3)
        shader(gameTypeSection, clockGameSpace);
    });

    function shader(element1, element2) {
        element1.style.transition = "opacity 0.5s ease-out";
        element1.style.opacity = "0";
        setTimeout(() => {
            element1.style.display = "none";
            element2.style.display = "block";
            element2.style.transition = "opacity 0.5s ease-in";
            element2.style.opacity = "1";
        }, 500)
    }

    let clockInTurkish;

    // Game type functions
    const gameTypeFunctions = [
        0,
        function clockGame1() {
            let [randomHour, randomMinute] = singleClock();

            if (randomMinute === 0 || randomMinute === 30) {
                clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + " " + minuteInTurkish;
            } else if (randomMinute < 30) {
                if (randomHour === 1 || randomHour === 5 || randomHour === 8 || randomHour === 11) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "i" + " " + minuteInTurkish(randomMinute) + " " + "geçiyor";
                } else if (randomHour === 2 || randomHour === 7 || randomHour === 12) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "yi" + " " + minuteInTurkish(randomMinute) + " " + "geçiyor";
                } else if (randomHour === 3) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "ü" + " " + minuteInTurkish(randomMinute) + " " + "geçiyor";
                } else if (randomHour === 4) {
                    clockInTurkish = "Saat" + " " + "dördü" + " " + minuteInTurkish(randomMinute) + " " + "geçiyor";
                } else if (randomHour === 6) {
                    clockInTurkish = "Saat" + " " + "altıyı" + " " + minuteInTurkish(randomMinute) + " " + "geçiyor";
                } else {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "u" + " " + minuteInTurkish(randomMinute) + " " + "geçiyor";
                }
            } else {
                if (randomHour === 4 || randomHour === 7 || randomHour === 10 || randomHour === 2) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour + 1] + "e" + " " + minuteInTurkish(randomMinute) + " " + "var";
                } else if (randomHour === 1 || randomHour === 6 || randomHour === 11) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour + 1] + "ye" + " " + minuteInTurkish(randomMinute) + " " + "var";
                } else if (randomHour === 3) {
                    clockInTurkish = "Saat" + " " + "dörde" + " " + minuteInTurkish(randomMinute) + " " + "var";
                } else if (randomHour === 5) {
                    clockInTurkish = "Saat" + " " + "altıya" + " " + minuteInTurkish(randomMinute) + " " + "var";
                } else if (randomHour === 12) {
                    clockInTurkish = "Saat" + " " + "bire" + " " + minuteInTurkish(randomMinute) + " " + "var";
                } else {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour + 1] + "a" + " " + minuteInTurkish(randomMinute) + " " + "var";
                }
            }
        },
        function clockGame2() {
            let [randomHour, randomMinute] = singleClock();

            if (randomMinute === 0) {
                if (hoursInTurkish[randomHour] === '1' || hoursInTurkish[randomHour] === '2' || hoursInTurkish[randomHour] === '7' || hoursInTurkish[randomHour] === '8' || hoursInTurkish[randomHour] === '11' || hoursInTurkish[randomHour] === '12') {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "de" + " " + 'gelirim';
                } else if (hoursInTurkish[randomHour] === '3' || hoursInTurkish[randomHour] === '3' || hoursInTurkish[randomHour] === '5') {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "te" + " " + 'gelirim';
                } else {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "da" + " " + 'gelirim';
                }
            } else if (randomMinute === 30) {
                clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "buçukta" + " " + 'gelirim';
            } else if (randomMinute < 30) {
                if (randomHour === 1 || randomHour === 5 || randomHour === 8 || randomHour === 11) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "i" + " " + minuteInTurkish(randomMinute) + " " + "geçe" + " " + 'gelirim';
                } else if (randomHour === 2 || randomHour === 7 || randomHour === 12) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "yi" + " " + minuteInTurkish(randomMinute) + " " + "geçe" + " " + 'gelirim';
                } else if (randomHour === 3) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "ü" + " " + minuteInTurkish(randomMinute) + " " + "geçe" + " " + 'gelirim';
                } else if (randomHour === 4) {
                    clockInTurkish = "Saat" + " " + "dördü" + " " + minuteInTurkish(randomMinute) + " " + "geçe" + " " + 'gelirim';
                } else if (randomHour === 6) {
                    clockInTurkish = "Saat" + " " + "altıyı" + " " + minuteInTurkish(randomMinute) + " " + "geçe" + " " + 'gelirim';
                } else {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour] + "u" + " " + minuteInTurkish(randomMinute) + " " + "geçe" + " " + 'gelirim';
                }
            } else {
                if (randomHour === 4 || randomHour === 7 || randomHour === 10 || randomHour === 2) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour + 1] + "e" + " " + minuteInTurkish(randomMinute) + " " + "kala" + " " + 'gelirim';
                } else if (randomHour === 1 || randomHour === 6 || randomHour === 11) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour + 1] + "ye" + " " + minuteInTurkish(randomMinute) + " " + "kala" + " " + 'gelirim';
                } else if (randomHour === 3) {
                    clockInTurkish = "Saat" + " " + "dörde" + " " + minuteInTurkish(randomMinute) + " " + "kala" + " " + 'gelirim';
                } else if (randomHour === 5) {
                    clockInTurkish = "Saat" + " " + "altıya" + " " + minuteInTurkish(randomMinute) + " " + "kala" + " " + 'gelirim';
                } else if (randomHour === 12) {
                    clockInTurkish = "Saat" + " " + "bire" + " " + minuteInTurkish(randomMinute) + " " + "kala" + " " + 'gelirim';
                } else {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour + 1] + "a" + " " + minuteInTurkish(randomMinute) + " " + "kala" + " " + 'gelirim';
                }
            }

        },
        function clockGame3() {
            let [randomHour1, randomMinute1, randomHour2, randomMinute2] = doubleClock();
            if (randomMinute1 === 0) {
                if (
                    randomHour1 === 1 ||
                    randomHour1 === 2 ||
                    randomHour1 === 7 ||
                    randomHour1 === 8 ||
                    randomHour1 === 11 ||
                    randomHour1 === 12) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1] + "’den" + " "
                } else if (
                    randomHour1 === 3 ||
                    randomHour1 === 4 ||
                    randomHour1 === 5) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1] + "’ten" + " "
                } else {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1] + "’dan" + " "
                }
            } else if (randomMinute1 === 30) {
                clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1] + " " + "buçuk’tan" + " ";
            } else if (randomMinute1 < 30) {
                if (randomHour1 === 1 || randomHour1 === 5 || randomHour1 === 8 || randomHour1 === 11) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1] + "i" + " " + minuteInTurkish(randomMinute1) + " " + "geçeden " + " ";
                } else if (randomHour1 === 2 || randomHour1 === 7 || randomHour1 === 12) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1] + "yi" + " " + minuteInTurkish(randomMinute1) + " " + "geçe’den" + " ";
                } else if (randomHour1 === 3) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1] + "ü" + " " + minuteInTurkish(randomMinute1) + " " + "geçe’den" + " ";
                } else if (randomHour1 === 4) {
                    clockInTurkish = "Saat" + " " + "dördü" + " " + minuteInTurkish(randomMinute1) + " " + "geçe’den" + " ";
                } else if (randomHour1 === 6) {
                    clockInTurkish = "Saat" + " " + "altıyı" + " " + minuteInTurkish(randomMinute1) + " " + "geçe’den" + " ";
                } else {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1] + "u" + " " + minuteInTurkish(randomMinute1) + " " + "geçe’den" + " ";
                }
            } else {
                if (randomHour1 === 4 || randomHour1 === 7 || randomHour1 === 10 || randomHour1 === 2) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1 + 1] + "e" + " " + minuteInTurkish(randomMinute1) + " " + "kaladan" + " ";
                } else if (randomHour1 === 1 || randomHour1 === 6 || randomHour1 === 11) {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1 + 1] + "ye" + " " + minuteInTurkish(randomMinute1) + " " + "kala’dan" + " ";
                } else if (randomHour1 === 3) {
                    clockInTurkish = "Saat" + " " + "dörde" + " " + minuteInTurkish(randomMinute1) + " " + "kala’dan" + " ";
                } else if (randomHour1 === 5) {
                    clockInTurkish = "Saat" + " " + "altıya" + " " + minuteInTurkish(randomMinute1) + " " + "kala’dan" + " ";
                } else if (randomHour1 === 12) {
                    clockInTurkish = "Saat" + " " + "bire" + " " + minuteInTurkish(randomMinute1) + " " + "kala’dan" + " ";
                } else {
                    clockInTurkish = "Saat" + " " + hoursInTurkish[randomHour1 + 1] + "a" + " " + minuteInTurkish(randomMinute1) + " " + "kala’dan" + " ";
                }
            }
            if (randomMinute2 === 0) {
                if (
                    randomHour2 === 1 ||
                    randomHour2 === 3 ||
                    randomHour2 === 5 ||
                    randomHour2 === 8 ||
                    randomHour2 === 11) {
                    clockInTurkish += hoursInTurkish[randomHour2] + "e" + " " + "kadar";
                } else if (
                    randomHour2 === 2 ||
                    randomHour2 === 12) {
                    clockInTurkish += hoursInTurkish[randomHour2] + "ye" + " " + "kadar";
                } else if (
                    randomHour2 === 4) {
                    clockInTurkish += "dörde" + " " + "kadar";
                } else if (
                    randomHour2 === 6) {
                    clockInTurkish += hoursInTurkish[randomHour2] + "yı" + " " + "kadar";
                } else {
                    clockInTurkish += hoursInTurkish[randomHour2] + "a" + " " + "kadar";
                }
            } else if (randomMinute2 === 30) {
                clockInTurkish += hoursInTurkish[randomHour2] + "buçuğa" + " " + "kadar";
            } else if (randomMinute2 < 30) {
                if (randomHour2 === 1 || randomHour2 === 5 || randomHour2 === 8 || randomHour2 === 11) {
                    clockInTurkish += hoursInTurkish[randomHour2] + "i" + " " + minuteInTurkish(randomMinute2) + " " + "geçe’ye " + " " + "kadar";
                } else if (randomHour2 === 2 || randomHour2 === 7 || randomHour2 === 12) {
                    clockInTurkish += hoursInTurkish[randomHour2] + "yi" + " " + minuteInTurkish(randomMinute2) + " " + "geçe’ye " + " " + "kadar";
                } else if (randomHour2 === 3) {
                    clockInTurkish += hoursInTurkish[randomHour2] + "ü" + " " + minuteInTurkish(randomMinute2) + " " + "geçe’ye " + " " + "kadar";
                } else if (randomHour2 === 4) {
                    clockInTurkish += "dördü" + " " + minuteInTurkish(randomMinute2) + " " + "geçe’ye " + " " + "kadar";
                } else if (randomHour2 === 6) {
                    clockInTurkish += "altıyı" + " " + minuteInTurkish(randomMinute2) + " " + "geçe’ye " + " " + "kadar";
                } else {
                    clockInTurkish += hoursInTurkish[randomHour2] + "u" + " " + minuteInTurkish(randomMinute2) + " " + "geçe’ye " + " " + "kadar";
                }
            } else {
                if (randomHour2 === 4 || randomHour2 === 7 || randomHour2 === 10 || randomHour2 === 2) {
                    clockInTurkish += hoursInTurkish[randomHour2 + 1] + "e" + " " + minuteInTurkish(randomMinute2) + " " + "kala’ya " + " " + "kadar";
                } else if (randomHour2 === 1 || randomHour2 === 6 || randomHour2 === 11) {
                    clockInTurkish += hoursInTurkish[randomHour2 + 1] + "ye" + " " + minuteInTurkish(randomMinute2) + " " + "kala’ya " + " " + "kadar";
                } else if (randomHour2 === 3) {
                    clockInTurkish += "dörde" + " " + minuteInTurkish(randomMinute2) + " " + "kala’ya " + " " + "kadar";
                } else if (randomHour2 === 5) {
                    clockInTurkish += "altıya" + " " + minuteInTurkish(randomMinute2) + " " + "kala’ya " + " " + "kadar";
                } else if (randomHour2 === 12) {
                    clockInTurkish += "bire" + " " + minuteInTurkish(randomMinute2) + " " + "kala’ya " + " " + "kadar";
                } else {
                    clockInTurkish += hoursInTurkish[randomHour2 + 1] + "a" + " " + minuteInTurkish(randomMinute2) + " " + "kala’ya " + " " + "kadar";
                }
            }
        },
    ]

    function startGameEvent(gameTypeNumber) {
        startGame.addEventListener("click", () => {
            gameTypeFunctions[gameTypeNumber]()
            startGame.style.transition = "opacity 0.5s ease-out";
            startGame.style.opacity = "0";
            answer.style.transition = "opacity 0.5s ease-out";
            answer.style.opacity = "0";
            setTimeout(() => {
                startGame.style.display = "none";
                correctAnswer.style.display = "block";
                correctAnswer.style.transition = "opacity 0.5s ease-in";
                correctAnswer.style.opacity = "1";
                answer.style.display = "none";
                answer.innerText = clockInTurkish;
            }, 500)
        })
    }

    correctAnswer.addEventListener("click", () => {
        correctAnswer.style.transition = "opacity 0.5s ease-out";
        correctAnswer.style.opacity = "0";
        setTimeout(() => {
            correctAnswer.style.display = "none";
            answer.style.display = "block";
            answer.style.transition = "opacity 0.5s ease-in";
            answer.style.opacity = "1";
            startGame.style.display = "block";
            startGame.style.transition = "opacity 0.5s ease-in";
            startGame.style.opacity = "1";
        }, 500)
    })

    function createRandomHour() {
        return Math.floor(Math.random() * 12) + 1;
    }

    function createRandomMinute() {
        return Math.floor(Math.random() * 12) * 5;
    }

    function createHoursAngle(hour, minute) {
        return (90 + (hour % 12) * 30 + minute * 0.5);
    }

    function createMinutesAngle(minute) {
        return (90 + minute * 6);
    }

    function createRotateStyle(angle) {
        return `rotate(${angle}deg)`;
    }

    function singleClock() {
        // Calculate the angles
        let randomHour = createRandomHour();
        let randomMinute = createRandomMinute();
        const hoursAngle = createHoursAngle(randomHour, randomMinute);
        const minutesAngle = createMinutesAngle(randomMinute);

        // Apply the transformations
        hourHand1.style.transform = createRotateStyle(hoursAngle);
        minuteHand1.style.transform = createRotateStyle(minutesAngle);
        hourHand2.style.transform = createRotateStyle(hoursAngle);
        minuteHand2.style.transform = createRotateStyle(minutesAngle);

        return [randomHour, randomMinute]
    }

    function doubleClock() {
        // Calculate the angles
        let randomHour1 = createRandomHour();
        let randomMinute1 = createRandomMinute();
        const hoursAngle1 = createHoursAngle(randomHour1, randomMinute1);
        const minutesAngle1 = createMinutesAngle(randomMinute1);
        let randomHour2 = createRandomHour();
        let randomMinute2 = createRandomMinute();
        const hoursAngle2 = createHoursAngle(randomHour2, randomMinute2);
        const minutesAngle2 = createMinutesAngle(randomMinute2);

        // Apply the transformations
        hourHand1.style.transform = createRotateStyle(hoursAngle1);
        minuteHand1.style.transform = createRotateStyle(minutesAngle1);
        hourHand2.style.transform = createRotateStyle(hoursAngle2);
        minuteHand2.style.transform = createRotateStyle(minutesAngle2);

        return [randomHour1, randomMinute1, randomHour2, randomMinute2];
    }

    const hoursInTurkish = [null, "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz", "on", "on bir", "on iki",];

    function minuteInTurkish(minute) {
        switch (minute) {
            case 5:
            case 55:
                minute = "beş";
                break;
            case 10:
            case 50:
                minute = "on";
                break;
            case 15:
            case 45:
                minute = "çeyrek";
                break;
            case 20:
            case 40:
                minute = "yirmi";
                break;
            case 25:
            case 35:
                minute = "yirmi beş";
                break;
            case 30:
                minute = "buçuk";
                break;
            case 0:
                minute = "";
                break;
        }
        return minute;
    }
});
