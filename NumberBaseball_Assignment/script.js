let attempts = 9;
targetNumbers = generateUniqueNumbers();

function check_numbers() {
    const inputs = document.querySelectorAll('.input-field');
    const numbers = Array.from(inputs).map(input => parseInt(input.value, 10));

    if (numbers.some(isNaN)) {
        clearInput();
        return;
    }
    attempts--;

    const result = compareNumbers(numbers, targetNumbers);
    updateResultDisplay(numbers, result);

    if (result.strikes === 3 || attempts === 0) {
        endGame(result.strikes === 3) ;
    }
    clearInput();
}

function compareNumbers(input, targetNumbers) {
    let strikes = 0;
    let balls = 0;

    input.forEach((num, index) => {
        if (num === targetNumbers[index]) {
            strikes++;
        } else if (targetNumbers.includes(num)){
            balls++;
        }
    });
    return { strikes, balls};
}

function updateResultDisplay(numbers, result) {
    const resultDisplay = document.querySelector('.result-display');
    const resultHTML = `
        <div class="check-result">
        <div class="left">${numbers.join(' ')}</div>
        :
        <div class="right">
            ${result.strikes > 0 || result.balls > 0 ?
                `${result.strikes} <div class="strike num-result">S</div>
                ${result.balls} <div class="ball num-result">B</div>` :
                `<div class="out num-result">O</div>`
            }
        </div>
    </div>
    `;
    resultDisplay.insertAdjacentHTML('afterbegin', resultHTML);
    
}

function endGame(isWin) {
    const resultImg = document.getElementById('game-result-img');
    resultImg.src = isWin ? 'success.png':'fail.png';
    document.querySelector('.submit-buton').disabled = true;
}

function initializeGame() {
    attempts = 9;
    targetNumbers = generateUniqueNumbers();
    clearInput();
    clearResults();
}

function generateUniqueNumbers() {
    const numbers = new Set();
    while(numbers.size < 3) {
        numbers.add(Math.floor(Math.random()*10));
    }
    return Array.from(numbers)
}

function clearInput() {
    document.querySelectorAll('.input-field').forEach(input => input.value ='');
}

function clearResults() {
    document.querySelector('.result-display').innerHTML = '' ;
}






