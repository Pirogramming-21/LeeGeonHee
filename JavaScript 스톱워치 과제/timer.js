const time = document.querySelector('.moniter');
const startBtn = document.querySelector('.btn-start');
const stopBtn = document.querySelector('.btn-stop');
const resetBtn = document.querySelector('.btn-reset');
const recordList = document.getElementById('record-list');
const clearRecordsBtn = document.querySelector('.btn-clear-records');
const selectAllCheckbox = document.getElementById('select-all-checkbox');

let milliseconds = 0;
let timer;
let recordCount = 0;

function start(){
    if (!timer) {
        timer = setInterval(updateTimer, 10); // 10ms마다 업데이트 (100분의 1초)
    }
}

function stop(){
    clearInterval(timer);
    timer = null;
    addRecord();
}

function reset(){
    clearInterval(timer);
    timer = null;
    milliseconds = 0;
    updateDisplay();
    clearRecords();
}

function updateTimer(){
    milliseconds += 10;
    updateDisplay();
}

function updateDisplay() {
    const seconds = Math.floor(milliseconds / 1000);
    const centiseconds = Math.floor((milliseconds % 1000) / 10);
    const displaySeconds = seconds < 10 ? '0' + seconds : seconds;
    const displayCentiseconds = centiseconds < 10 ? '0' + centiseconds : centiseconds;
    time.textContent = `${displaySeconds}:${displayCentiseconds}`;
}

function addRecord(){
    recordCount++;
    const li = document.createElement('li');
    li.innerHTML = `<input type="checkbox" class='record-checkbox'> ${recordCount}. ${time.textContent}`;
    recordList.appendChild(li);
}

function clearRecords() {
    recordList.innerHTML = '';
    recordCount = 0;
}

function clearSelectedRecords() {
    const checkboxes = document.querySelectorAll('.record-checkbox');
    let removedCount = 0;
    checkboxes.forEach((checkbox, index) => {
        if (checkbox.checked) {
            checkbox.parentElement.remove();
            removedCount++;
        } else if (removedCount > 0) {
            const newNumber = index + 1 - removedCount;
            const textContent = checkbox.parentElement.textContent.split('. ')[1];
            checkbox.parentElement.innerHTML = `<input type="checkbox" class="record-checkbox"> ${newNumber}. ${textContent}`;
        }
    });
    recordCount -= removedCount;
    selectAllCheckbox.checked = false;
}

function toggleSelectAll() {
    const checkboxes = document.querySelectorAll('.record-checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.checked = selectAllCheckbox.checked;
    });
}



startBtn.addEventListener('click', start);
stopBtn.addEventListener('click', stop);
resetBtn.addEventListener('click', reset);
selectAllCheckbox.addEventListener('change', toggleSelectAll);
clearRecordsBtn.addEventListener('click', clearSelectedRecords);


updateDisplay();