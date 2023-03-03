const fNameField = document.getElementById('fname-field')
const lNameField = document.getElementById('lname-field')
const fNameError = document.getElementById('fname-error')
const lNameError = document.getElementById('lname-error')
const emailField = document.getElementById('email-field')
const emailError = document.getElementById('email-error')
// const usernameSuccess = document.getElementById('username-success')
const emailSuccess = document.getElementById('email-success')
const passwordField = document.getElementById('password-field')
const passwordError = document.getElementById('password-error')
const cpasswordField = document.getElementById('cpassword-field')
const cpasswordError = document.getElementById('cpassword-error')
const togglePassword = document.getElementById('toggle-password')
const submitBtn = document.getElementById('btn-submit')
let show = false


function ValidateEmail(input) {

    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  
    if (input.value.match(validRegex)) {
  
      return true;
  
    }
    return false;
}

togglePasswordVisibility = () => {
    show = !show
    if (show) {
        togglePassword.textContent = `HIDE`
        passwordField.setAttribute("type", "text")
    } else {
        togglePassword.textContent = `SHOW`
        passwordField.setAttribute("type", "password")
    }
}

togglePassword.addEventListener('click', togglePasswordVisibility)


cpasswordField.addEventListener('keyup', () => {
    if (cpasswordField.value === passwordField.value) {
        submitBtn.disabled = false
        cpasswordField.classList.remove('is-invalid')
        cpasswordField.classList.add('is-valid')
        if (cpasswordError.firstChild) {
            cpasswordError.removeChild(cpasswordError.firstChild)
        }
    } else {
        submitBtn.disabled = true
        cpasswordField.classList.add('is-invalid')
        cpasswordError.innerHTML = `<p>Passwords doesn't match</p>`
        cpasswordError.style.display = "block"
    }
})


passwordField.addEventListener('keyup', () => {
    if (passwordField.value.length > 6) {
        submitBtn.disabled = false
        passwordField.classList.remove('is-invalid')
        passwordField.classList.add('is-valid')
        if (passwordError.firstChild) {
            passwordError.removeChild(passwordError.firstChild)
        }
    } else {
        submitBtn.disabled = true
        passwordField.classList.add('is-invalid')
        passwordError.innerHTML = `<p>Password length must be at least 7</p>`
        passwordError.style.display = "block"
    }
})

emailField.addEventListener('keyup', () => {
    if (ValidateEmail(emailField)) {
        fetch('/validate_email', {
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({email: emailField.value}),
            method: "POST"
        }).then(res => res.json())
        .then((data) => {
            if (data.valid) {
            submitBtn.disabled = false
            emailField.classList.remove('is-invalid')
            emailField.classList.add('is-valid')
            if (emailError.firstChild) {
                emailError.removeChild(emailError.firstChild)
            }
        } else {
            submitBtn.disabled = true
            emailField.classList.add('is-invalid')
            emailError.innerHTML = `<p>Email already in use</p>`
            emailError.style.display = "block"
        }
        })

    } else {
        submitBtn.disabled = true
        emailField.classList.add('is-invalid')
        emailError.innerHTML = `<p>Invalid email format</p>`
        emailError.style.display = "block"
    }
})

fNameField.addEventListener("keyup", ()=>{

    if (fNameField.value.length > 2){
        submitBtn.disabled = false
        fNameField.classList.remove('is-invalid')
        fNameField.classList.add('is-valid')
        if (fNameError.firstChild){
            fNameError.removeChild(fNameError.firstChild)
        }
    } else {
        submitBtn.disabled = true
        fNameField.classList.add('is-invalid')
        fNameError.innerHTML = `<p>Length must greater than 2</p>`
        fNameError.style.display = "block"
    }
})

lNameField.addEventListener("keyup", ()=>{

    if (lNameField.value.length > 2){
        submitBtn.disabled = false
        lNameField.classList.remove('is-invalid')
        lNameField.classList.add('is-valid')
        if (lNameError.firstChild){
            lNameError.removeChild(lNameError.firstChild)
        }
    } else {
        submitBtn.disabled = true
        lNameField.classList.add('is-invalid')
        lNameError.innerHTML = `<p>Length must be greater than 2</p>`
        lNameError.style.display = "block"
    }
})
