// Utility to retrieve CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.split("=")[1]);
                break;
            }
        }
    }
    return cookieValue;
}

// Like/unlike a post
function toggleLike(postId) {
    fetch(`/toggle_like/${postId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        }
    })
        .then(response => response.json())
        .then(data => {
            const btn = document.querySelector(`#like-btn-${postId}`);
            const icon = btn.querySelector(".icon");
            const count = document.querySelector(`#like-count-${postId}`);

            // Toggle class based on like status
            btn.classList.toggle("liked", data.liked);
            btn.classList.toggle("unliked", !data.liked);

            // Optional: update accessible label
            btn.setAttribute("aria-pressed", data.liked);

            // Update visible count
            if (count) {
                count.innerText = data.count;
            }
        })
        .catch(error => {
            console.error("Error toggling like:", error);
        });
}

// Show edit UI for a post
function editPost(postId) {
    document.querySelector(`#edit-area-${postId}`).style.display = "block";
    document.querySelector(`#post-content-${postId}`).style.display = "none";
}

// Save edited content of a post
function savePost(postId) {
    const textarea = document.querySelector(`#edit-textarea-${postId}`);
    fetch(`/edit_post/${postId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ content: textarea.value.trim() })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const content = document.querySelector(`#post-content-${postId}`);
                content.innerText = data.content;
                cancelEdit(postId);
            } else {
                alert("Failed to save post: " + data.error);
            }
        })
        .catch(error => {
            console.error("Error saving post:", error);
        });
}

// Cancel editing mode
function cancelEdit(postId) {
    document.querySelector(`#edit-area-${postId}`).style.display = "none";
    document.querySelector(`#post-content-${postId}`).style.display = "block";
    document.querySelector(`#like-btn-${postId}`)
    document.querySelector(`#like-count-${postId}`)
}