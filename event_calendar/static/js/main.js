function newEvent(event) {
    event.preventDefault()
    let name = document.getElementById('name').value
    let description = document.getElementById('description').value
    let startsAt = document.getElementById('starts-at').value
    let endsAt = document.getElementById('ends-at').value
    data = {
        'name': name,
        'description': description,
        'startsAt': startsAt,
        'endsAt': endsAt,
    }
    axios.post('new_event', data)
    .then((response) => {
    })
}

function updateEvent(event) {
    event.preventDefault()
    let name = document.getElementById('update-name').value
    let description = document.getElementById('update-description').value
    let startsAt = document.getElementById('update-starts-at').value
    let endsAt = document.getElementById('update-ends-at').value

    data = {
        'name': name,
        'description': description,
        'startsAt': startsAt,
        'endsAt': endsAt,
    }
    axios.post('', data)
    .then((response) => {
        console.log('>>>>>>>>>>>>>>>>>>>>>Response back from backend', response)
        alert(response['data']['Status'])
        window.location.href = '/events';
    })
}

function signUp(event) {
    event.preventDefault()
    firstName = document.getElementById('first-name').value
    lastName = document.getElementById('last-name').value
    email = document.getElementById('email').value
    password = document.getElementById('password').value

    data = {"firstName" : firstName,
        "lastName" : lastName,
        "email" : email,
        "password" : password
    }  
    axios.post('sign_up', data)
    .then((response) => {
        console.log(response['data']['Status'])
        alert(response['data']['Status'])
        window.location.href = '/events';
    })
}

function logIn(event) {
    event.preventDefault()
    email = document.getElementById('email').value
    password = document.getElementById('password').value    
    data = {
        'email': email,
        'password': password
    }
    axios.post('log_in', data)
    .then((response) => {
        alert(response['data']['Status'])
        window.location.href = '/events';
    })
}