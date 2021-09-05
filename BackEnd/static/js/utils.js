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

function sendDataPost(url, data) {
    fetch(url,
    {
        method: 'post',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(data),
    }
    ).then((response) => response.ok ? window.location.reload() : '');
}

function isAuthenticated() {
    if (!is_authenticated) {
        const curr_path = window.location.pathname;
        location.href = `/accounts/login/?next=${curr_path}`;
        return false;
    }
    return true;
}