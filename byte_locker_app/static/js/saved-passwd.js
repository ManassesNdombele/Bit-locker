let update_passwd_btn = document.getElementsByClassName('saved-passwd-action')[0]
let add_passwd_btn = document.getElementsByClassName('saved-passwd-action')[1]
let delete_passwd_btn = document.getElementsByClassName('saved-passwd-action')[2]
let close_modal_update_passwd = document.getElementsByClassName('close-modal-btn')[1]
let close_modal_add_passwd = document.getElementsByClassName('close-modal-btn')[0]
let close_modal_delete_passwd = document.getElementsByClassName('close-modal-btn')[2]
let cancel_delete_passwd = document.getElementsByClassName('close-modal-btn')[3]

add_passwd_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('new-passwd').style.display = 'flex'
})

close_modal_add_passwd.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('new-passwd').style.display = 'none'
})

update_passwd_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('password-update').style.display = 'flex'
})

close_modal_update_passwd.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('password-update').style.display = 'none'
})

delete_passwd_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('password-delete').style.display = 'flex'
})

close_modal_delete_passwd.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('password-delete').style.display = 'none'
})

cancel_delete_passwd.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('password-delete').style.display = 'none'
})
