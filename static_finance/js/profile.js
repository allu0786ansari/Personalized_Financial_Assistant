document.addEventListener('DOMContentLoaded', function() {
    // Debugging: Check if script is loaded
    console.log('JavaScript loaded');

    // Get references to the edit button and edit form
    const editButton = document.getElementById('editButton');
    const editForm = document.getElementById('editForm');

    if (!editButton || !editForm) {
        console.error('Edit button or edit form not found');
        return;
    }

    // Add click event listener to the edit button
    editButton.addEventListener('click', function() {
        // Toggle the visibility of the edit form
        if (editForm.style.display === 'none') {
            editForm.style.display = 'block';
            editButton.textContent = 'Cancel'; // Change button text to 'Cancel'
        } else {
            editForm.style.display = 'none';
            editButton.textContent = 'Edit Profile'; // Change button text back to 'Edit Profile'
        }
    });
});
