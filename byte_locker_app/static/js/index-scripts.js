function open_modal(modal) {
    function show_modal_details() {
        document.getElementById(`loader-${modal}-modal`).style.visibility = 'hidden'
    }

    var modal_finded = false
    for (let counter = 0; modal_finded === false; counter++) {
        var modal_element = document.getElementsByClassName('modal')[counter]
        if (modal_element.classList.contains(modal) === true) {
            document.getElementsByClassName('main-header')[0].style.opacity = '0.1'
            document.getElementsByTagName('main')[0].style.opacity = '0.1'
            if (modal_element.checkVisibility() === true) {
                modal_element.style.visibility = 'visible'
                modal_finded = true
            }
        }
    }
    setTimeout(show_modal_details, 4000)
}

function close_modal(modal) {
    var modal_finded = false
    for (let counter = 0; modal_finded === false; counter++) {
        var modal_element = document.getElementsByClassName('modal')[counter]
        if (modal_element.classList.contains(modal) === true) {
            document.getElementsByClassName('main-header')[0].style.opacity = '1'
            document.getElementsByTagName('main')[0].style.opacity = '1'
            modal_element.style.visibility = 'hidden'
            modal_finded = true
        }
    }
}

document.getElementsByClassName('password-generator')[0].addEventListener('click', () => {open_modal('password-generator')})
document.getElementById('close-modal-password-generator-btn').addEventListener('click', () => {close_modal('password-generator')})
document.getElementsByClassName('saved-passwords')[0].addEventListener('click', () => {open_modal('saved-passwords')})
document.getElementById('close-modal-saved-passwords-btn').addEventListener('click', () => {close_modal('saved-passwords')})
document.getElementsByClassName('saved-accounts')[0].addEventListener('click', () => {open_modal('saved-accounts')})
document.getElementById('close-modal-saved-accounts-btn').addEventListener('click', () => {close_modal('saved-accounts')})
document.getElementsByClassName('authenticator')[0].addEventListener('click', () => {open_modal('authenticator')})
document.getElementById('close-modal-authenticator-btn').addEventListener('click', () => {close_modal('authenticator')})
document.getElementsByClassName('account-configs')[0].addEventListener('click', () => {open_modal('account-configs')})
document.getElementById('close-modal-account-configs-btn').addEventListener('click', () => {close_modal('account-configs')})
document.getElementsByClassName('help-center')[0].addEventListener('click', () => {open_modal('help-center')})
document.getElementById('close-modal-help-center-btn').addEventListener('click', () => {close_modal('help-center')})
