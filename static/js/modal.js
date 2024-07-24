// Get the modal
var modal = document.getElementById("image-modal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var modalImg = document.getElementById("modal-image");
var captionText = document.getElementById("caption");
var span = document.getElementsByClassName("close")[0];

function openModal(src, alt) {
    modalImg.style.display = "none";
    modal.style.display = "block";
    modalImg.src = src;
    modalImg.onload = function() {
        // Adjust modal image size based on its natural dimensions
        var naturalWidth = modalImg.naturalWidth;
        var naturalHeight = modalImg.naturalHeight;
        
        if (naturalWidth > window.innerWidth * 0.8 || naturalHeight > window.innerHeight * 0.8) {
            modalImg.style.width = '80%';
            modalImg.style.height = 'auto';
        } 
        else {
            modalImg.style.width = naturalWidth + 'px';
            modalImg.style.height = naturalHeight + 'px';
        }

        modalImg.style.display = "block";
    };
    
    captionText.innerHTML = alt;
}

var images = document.getElementsByClassName("message-image");

for (var i = 0; i < images.length; i++) {
    images[i].onclick = function() {
        openModal(this.src, this.alt);
    }
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal content, close the modal
modal.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}