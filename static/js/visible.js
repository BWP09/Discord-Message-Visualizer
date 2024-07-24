document.getElementById('toggleContent').addEventListener('change', function() {
    var images = document.querySelectorAll('.message-body');

    images.forEach(function(image) {
        if (this.checked) {
            image.style.display = 'none';
        } else {
            image.style.display = 'block';
        }
    }, this);
});

document.getElementById('toggleImages').addEventListener('change', function() {
    var images = document.querySelectorAll('.message-image');

    images.forEach(function(image) {
        if (this.checked) {
            image.style.display = 'none';
        } else {
            image.style.display = 'block';
        }
    }, this);
});

document.getElementById('toggleReactions').addEventListener('change', function() {
    var images = document.querySelectorAll('.reaction');

    images.forEach(function(image) {
        if (this.checked) {
            image.style.display = 'none';
        } else {
            image.style.display = 'block';
        }
    }, this);
});

document.getElementById('toggleTimestamps').addEventListener('change', function() {
    var images = document.querySelectorAll('.timestamp');

    images.forEach(function(image) {
        if (this.checked) {
            image.style.display = 'none';
        } else {
            image.style.display = 'block';
        }
    }, this);
});

document.getElementById('toggleUsernames').addEventListener('change', function() {
    var images = document.querySelectorAll('.username');

    images.forEach(function(image) {
        if (this.checked) {
            image.style.display = 'none';
        } else {
            image.style.display = 'block';
        }
    }, this);
});

document.getElementById('toggleAvatars').addEventListener('change', function() {
    var images = document.querySelectorAll('.avatar');

    images.forEach(function(image) {
        if (this.checked) {
            image.style.display = 'none';
        } else {
            image.style.display = 'block';
        }
    }, this);
});

document.getElementById('toggleIDs').addEventListener('change', function() {
    var images = document.querySelectorAll('.message-footer');

    images.forEach(function(image) {
        if (this.checked) {
            image.style.display = 'none';
        } else {
            image.style.display = 'block';
        }
    }, this);
});