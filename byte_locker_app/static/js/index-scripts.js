function open_modal() {
    var modal_finded = false
    while (modal_finded == false) {
        var modal_element = document.getElementsByClassName('modal')[0]
        if (modal_element.classList.contains('password-generator') === true) {
            let main_element = document.getElementsByTagName('main')[0]
            main_element.style.opacity = '0.1'
            if (modal_element.checkVisibility() === true) {
                modal_element.setAttribute('style', 'visibility: visible;')
                modal_finded = true
            }
        }
    }
}

let passwd_generator_div = document.getElementsByClassName('password-generator')[0]
passwd_generator_div.addEventListener('click', open_modal)
