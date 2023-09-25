var option1 = document.getElementsByClassName('password-generator')[0]
var option2 = document.getElementsByClassName('saved-passwords')[0]
var option3 = document.getElementsByClassName('saved-accounts')[0]
var option4 = document.getElementsByClassName('authenticator')[0]
var option5 = document.getElementsByClassName('account-configs')[0]
var option6 = document.getElementsByClassName('help-center')[0]

option1.addEventListener('click', () => {
    location.href = 'password-generator/'
})

option2.addEventListener('click', () => {
    location.href = 'saved-passwords/'
})

option3.addEventListener('click', () => {
    location.href = 'saved-accounts/'
})

option4.addEventListener('click', () => {
    location.href = 'authenticator/'
})

option5.addEventListener('click', () => {
    location.href = 'account-configs/'
})

option6.addEventListener('click', () => {
    location.href = 'help-center/'
})
