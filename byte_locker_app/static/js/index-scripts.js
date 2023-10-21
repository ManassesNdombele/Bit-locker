var home_btn = document.getElementById('home-btn')
var option1 = document.getElementsByClassName('option')[0]
var option2 = document.getElementsByClassName('option')[1]
var option3 = document.getElementsByClassName('option')[2]
var option4 = document.getElementsByClassName('option')[3]
var option5 = document.getElementsByClassName('option')[4]
var option6 = document.getElementsByClassName('option')[5]

option1.addEventListener('click', () => {
    location.href = 'password-generator/form/'
})

option2.addEventListener('click', () => {
    location.href = 'saved-passwords/list/'
})

option3.addEventListener('click', () => {
    location.href = 'saved-accounts/'
})

option4.addEventListener('click', () => {
    location.href = 'authentication/'
})

option5.addEventListener('click', () => {
    location.href = 'account-configs/'
})

option6.addEventListener('click', () => {
    location.href = 'help-center/'
})

home_btn.addEventListener('click', () => {
    location.href = '/'
})
