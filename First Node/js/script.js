// Intersection Observer for triggering animations
document.addEventListener('DOMContentLoaded', () => {
    const faders = document.querySelectorAll('.fade-in, .slide-in');

    const options = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const appearOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('appear');
            observer.unobserve(entry.target);
        });
    }, options);

    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('video-modal');
    const videoFrame = document.getElementById('youtube-video');
    const closeButton = document.querySelector('.close-button');
    const videoLinks = document.querySelectorAll('.resource-link');

    // Function to open the modal
    const openModal = (youtubeId) => {
        const embedUrl = `https://www.youtube.com/embed/${youtubeId}?autoplay=1&rel=0`;
        videoFrame.setAttribute('src', embedUrl);
        modal.style.display = 'flex';
    };

    // Function to close the modal
    const closeModal = () => {
        modal.style.display = 'none';
        videoFrame.setAttribute('src', ''); // Stop the video
    };

    // Add click event listeners to all video links
    videoLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent default link behavior
            const youtubeId = link.getAttribute('data-youtube-id');
            if (youtubeId) {
                openModal(youtubeId);
            }
        });
    });

    // Close modal when the close button is clicked
    closeButton.addEventListener('click', closeModal);

    // Close modal when clicking on the background overlay
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            closeModal();
        }
    });
});