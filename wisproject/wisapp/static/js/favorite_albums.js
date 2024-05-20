document.addEventListener('DOMContentLoaded', function () {
    const favoriteButtons = document.querySelectorAll('.albums-favorite-toggle');

    favoriteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();

            const actionUrl = this.getAttribute('href');

            fetch(actionUrl, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), 
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const addUrl = this.getAttribute('data-add-url');
                    const removeUrl = this.getAttribute('data-remove-url');
                    updateButton(this, data.action, addUrl, removeUrl);
                } else {
                    console.error('Failed to update favorite status');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

    function updateButton(button, action, addUrl, removeUrl) {
        if (action === 'added') {
            button.classList.remove('btn-primary');
            button.classList.add('btn-danger');
            button.innerHTML = '★';
            button.setAttribute('href', removeUrl);
        } else if (action === 'removed') {
            button.classList.remove('btn-danger');
            button.classList.add('btn-primary');
            button.innerHTML = '☆';
            button.setAttribute('href', addUrl);
        }
    }

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
});
