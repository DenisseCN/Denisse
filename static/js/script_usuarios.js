document.addEventListener('DOMContentLoaded', function () {
    const userForm = document.getElementById('userForm');
    const submitBtn = document.getElementById('submitBtn');

    userForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const userId = document.getElementById('userId').value;
        const url = userId ? `/api/usuarios/${userId}/` : '/api/usuarios/';
        const method = userId ? 'PUT' : 'POST';
        
        fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                username: document.getElementById('username').value,
                first_name: document.getElementById('first_name').value,
                last_name: document.getElementById('last_name').value,
                email: document.getElementById('email').value,
                is_superuser: document.getElementById('is_superuser').checked,
                is_active: document.getElementById('is_active').checked
            })
        })
        .then(response => {
            if (response.ok) {
                Swal.fire({
                    title: '¡Éxito!',
                    text: 'El usuario ha sido actualizado.',
                    icon: 'success',
                    confirmButtonText: 'Aceptar'
                });
                location.reload();
            } else {
                return response.json();
            }
        })
        .catch(error => {
            Swal.fire({
                title: 'Error',
                text: 'Ocurrió un error en la solicitud.',
                icon: 'error',
                confirmButtonText: 'Aceptar'
            });
            console.error('Error en la solicitud:', error);
        });
    });

    window.editUser = function (id) {
        fetch(`/api/usuarios/${id}/`)
            .then(response => response.json())
            .then(data => {
                console.log('Data:', data);
    
                const userIdElement = document.getElementById('userId');
                if (userIdElement) {
                    userIdElement.value = data.id;
                }
    
                const usernameElement = document.getElementById('username');
                if (usernameElement) {
                    usernameElement.value = data.username;
                }
    
                const firstNameElement = document.getElementById('first_name');
                if (firstNameElement) {
                    firstNameElement.value = data.first_name;
                }
    
                const lastNameElement = document.getElementById('last_name');
                if (lastNameElement) {
                    lastNameElement.value = data.last_name;
                }
    
                const emailElement = document.getElementById('email');
                if (emailElement) {
                    emailElement.value = data.email;
                }
    
                const isSuperUserElement = document.getElementById('is_superuser');
                if (isSuperUserElement !== null) {
                    isSuperUserElement.checked = data.is_superuser === true;
                }

                const isActiveElement = document.getElementById('is_active');
                if (isActiveElement !== null) {
                    isActiveElement.checked = data.is_active === true;
                }
    
                submitBtn.textContent = 'Actualizar';
    
                const formularioUsuario = document.getElementById('formularioUsuario');
                if (formularioUsuario) {
                    formularioUsuario.style.display = 'block';
                }
            });
    };

    window.deleteUser = function (id) {
        Swal.fire({
            title: '¿Estás seguro?',
            text: "¡No podrás revertir esto!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, eliminarlo!'
        }).then((result) => {
            if (result.isConfirmed) {
                fetch(`/api/usuarios/${id}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                }).then(response => {
                    if (response.ok) {
                        Swal.fire({
                            title: '¡Eliminado!',
                            text: 'El usuario ha sido eliminado.',
                            icon: 'success',
                            confirmButtonText: 'Aceptar'
                        });
                        document.getElementById(`user_${id}`).remove();
                    } else {
                        return response.json();
                    }
                })
                .catch(error => {
                    Swal.fire({
                        title: 'Error',
                        text: 'Ocurrió un error en la solicitud.',
                        icon: 'error',
                        confirmButtonText: 'Aceptar'
                    });
                    console.error('Error en la solicitud:', error);
                });
            }
        });
    };

    window.mostrarFormulario = function () {
        const formularioUsuario = document.getElementById('formularioUsuario');
        if (formularioUsuario) {
            formularioUsuario.style.display = 'block';
        }
        userForm.reset();
        const userIdElement = document.getElementById('userId');
        if (userIdElement) {
            userIdElement.value = '';
        }
        submitBtn.textContent = 'Guardar';
    };
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
