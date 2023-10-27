let delete_account_btn = document.getElementsByClassName('account-action')[0]
let logout_btn = document.getElementsByClassName('account-action')[1]
let update_info_btn = document.getElementsByClassName('account-action')[2]
let close_modal_del_account = document.getElementsByClassName('close-modal-btn')[0]
let close_modal_logout = document.getElementsByClassName('close-modal-btn')[2]
let close_modal_update_info = document.getElementsByClassName('close-modal-btn')[4]
let cancel_account_del = document.getElementsByClassName('close-modal-btn')[1]
let cancel_logout = document.getElementsByClassName('close-modal-btn')[3]

delete_account_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('delete-account').style.display = 'flex'
})

close_modal_del_account.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('delete-account').style.display = 'none'
})

cancel_account_del.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('delete-account').style.display = 'none'
})

logout_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('logout').style.display = 'flex'
})

close_modal_logout.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('logout').style.display = 'none'
})

cancel_logout.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('logout').style.display = 'none'
})

update_info_btn.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '0.1'
    document.getElementById('update-account-datas').style.display = 'flex'
})

close_modal_update_info.addEventListener('click', () => {
    document.getElementById('main-content').style.opacity = '1'
    document.getElementById('update-account-datas').style.display = 'none'
})
