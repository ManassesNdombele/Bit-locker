let regenerate_passwd_btn = document.getElementById('regenerate-passwd-btn')
let cancel_submit_btn = document.getElementById('cancel-submit-btn')

regenerate_passwd_btn.addEventListener('click', () => {
    location.href = 'password-generator/regenerate-password/'
})

cancel_submit_btn.addEventListener('click', () => {
    location.href = 'password-generator/cancel-generation/'
})
