let show_details_btn = document.getElementsByClassName('saved-accounts-action')[0]
let update_btn = document.getElementsByClassName('saved-accounts-action')[1]
let delete_btn = document.getElementsByClassName('saved-accounts-action')[2]
let close_show_details = document.getElementsByClassName('close-modal-btn')[0]
let close_update = document.getElementsByClassName('close-modal-btn')[1]
let close_delete = document.getElementsByClassName('close-modal-btn')[2]
let cancel_delete = document.getElementsByClassName('close-modal-btn')[3]

show_details_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('user-account-datas-get').style.display = 'flex'
})

update_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('user-account-datas-up').style.display = 'flex'
})

delete_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('user-account-datas-del').style.display = 'flex'
})

close_show_details.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('user-account-datas-get').style.display = 'none'
})

close_update.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('user-account-datas-up').style.display = 'none'
})

close_delete.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('user-account-datas-del').style.display = 'none'
})

cancel_delete.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('user-account-datas-del').style.display = 'none'
})
