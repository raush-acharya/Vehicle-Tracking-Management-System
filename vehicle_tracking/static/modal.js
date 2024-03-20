document.addEventListener('DOMContentLoaded', function() {
    const openModalButtons = document.querySelectorAll('.vehicle-card');
    const closeModalButton = document.querySelector('[data-close-button]');
    const overlay = document.getElementById('overlay');
    const modalTitle = document.getElementById('popup-title');
    const modalDescription = document.getElementById('popup-description');
    const modalPrice = document.getElementById('popup-price');

    openModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            const modal = document.getElementById('modal');
            const vehicleName = button.querySelector('h2').textContent;
            const vehicleDescription = button.querySelector('p:first-of-type').textContent;
            const vehiclePrice = button.querySelector('p:last-of-type').textContent;
    
            modalTitle.textContent = vehicleName;
            modalDescription.textContent = vehicleDescription;
            modalPrice.textContent = vehiclePrice;
    
            openModal(modal);
        });
    });
    

    overlay.addEventListener('click', () => {
        const modals = document.querySelectorAll('.modal.active');
        modals.forEach(modal => {
            closeModal(modal);
        });
    });

    closeModalButton.addEventListener('click', () => {
        const modal = document.querySelector('.modal.active');
        closeModal(modal);
    });

    function openModal(modal) {
        if (modal == null) return;
        modal.classList.add('active');
        overlay.classList.add('active');
    }

    function closeModal(modal) {
        if (modal == null) return;
        modal.classList.remove('active');
        overlay.classList.remove('active');
    }
});
