document.addEventListener('DOMContentLoaded', function () {
    const favoriteLinks = document.querySelectorAll('.favorite-toggle');

    favoriteLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const url = this.href;
            const btn = this; // Reference to the button
    
            fetch(url, { method: 'GET' })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    if (data.action === 'added') {
                        btn.innerHTML = '★ Remove from Favorites';
                        btn.classList.remove('btn-outline-primary');
                        btn.classList.add('btn-outline-danger');
                        btn.href = btn.href.replace('add-to-favorites', 'remove-from-favorites');
                    } else {
                        btn.innerHTML = '☆ Add to Favorites';
                        btn.classList.remove('btn-outline-danger');
                        btn.classList.add('btn-outline-primary');
                        btn.href = btn.href.replace('remove-from-favorites', 'add-to-favorites');
                    }
                } else {
                    alert('Something went wrong. Please try again.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});
