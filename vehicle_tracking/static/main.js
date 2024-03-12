// document.addEventListener('DOMContentLoaded', function() {
//     loadContent('vehicles'); // Load dashboard content by default
//     const menuItems = document.querySelectorAll('.menu-item');
//     menuItems.forEach(item => {
//         item.addEventListener('click', function() {
//             const section = this.dataset.section;
//             loadContent(section);
//             // Remove active class from all menu items
//             menuItems.forEach(item => {
//                 item.classList.remove('active-menu-item');
//             });
//             // Add active class to the clicked menu item
//             this.classList.add('active-menu-item');
//         });
//     });
// });


// function loadContent(section) {
//     fetch(`/${section}/`)
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.text();
//         })
//         .then(data => {
//             document.getElementById('dashboard-content').innerHTML = data;
//         })
//         .catch(error => {
//             console.error('There was a problem with the fetch operation:', error);
//         });
// }


// document.addEventListener('DOMContentLoaded', function() {
//     loadContent('vehicles'); // Load dashboard content by default
//     const menuItems = document.querySelectorAll('.menu-item');
//     menuItems.forEach(item => {
//         item.addEventListener('click', function() {
//             const section = this.dataset.section;
//             loadContent(section);
//             // Remove active class from all menu items
//             menuItems.forEach(item => {
//                 item.classList.remove('active-menu-item');
//             });
//             // Add active class to the clicked menu item
//             this.classList.add('active-menu-item');
//         });
//     });

//     // Add event listener for form submission
//     const form = document.getElementById('sortForm');
//     if (sortForm) {
//         form.addEventListener('submit', function(event) {
//             event.preventDefault(); // Prevent default form submission behavior
//             const formData = new FormData(form);
//             const sort_by = formData.get('sort_by');
//             const section = window.location.pathname.split('/')[1]; // Get current section from URL
//             loadContent(section + '/?sort_by=' + sort_by);
//         });
//     }
// });

// function loadContent(section) {
//     fetch(`/${section}/`)
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.text();
//         })
//         .then(data => {
//             document.getElementById('dashboard-content').innerHTML = data;
//         })
//         .catch(error => {
//             console.error('There was a problem with the fetch operation:', error);
//         });
// }


document.addEventListener('DOMContentLoaded', function() {
    // Load dashboard content by default
    loadContent('vehicles');

    // Event listener for menu item clicks
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            const section = this.dataset.section;
            loadContent(section);
            // Remove active class from all menu items
            menuItems.forEach(item => {
                item.classList.remove('active-menu-item');
            });
            // Add active class to the clicked menu item
            this.classList.add('active-menu-item');
        });
    });

    // Event listener for form submission
    const form = document.getElementById('sortForm');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission behavior
            const formData = new FormData(form);
            const sort_by = formData.get('sort_by');
            const section = window.location.pathname.split('/')[1]; // Get current section from URL
            loadContent(section + '/?sort_by=' + sort_by);
        });
    }
});


function loadContent(section) {
    fetch(`/${section}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('dashboard-content').innerHTML = data;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}
