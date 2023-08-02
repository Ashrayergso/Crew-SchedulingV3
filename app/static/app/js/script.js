// This script file is used for interactivity in the Django templates

document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
});

// Function to display success or failure messages
function displayMessage(messageType) {
    let message = '';
    switch(messageType) {
        case 'CREW_FETCH_SUCCESS':
            message = 'Crew members successfully fetched from the database.';
            break;
        case 'SHIP_FETCH_SUCCESS':
            message = 'Ships successfully fetched from the database.';
            break;
        case 'ASSIGNMENT_SUCCESS':
            message = 'New assignment successfully created.';
            break;
        case 'ASSIGNMENT_FAILURE':
            message = 'Error creating new assignment.';
            break;
        default:
            message = 'An unknown error occurred.';
    }
    alert(message);
}

// Function to handle form submission for creating/editing assignments
function handleFormSubmit(formId) {
    const form = document.getElementById(formId);
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        // Add your AJAX call here to submit the form data to the server
        // On success, call displayMessage('ASSIGNMENT_SUCCESS')
        // On failure, call displayMessage('ASSIGNMENT_FAILURE')
    });
}

// Function to handle sorting of ship and crew lists
function handleSort(sortType) {
    // Add your code here to sort the ship and crew lists based on the sortType
}

// Function to handle filtering of ship and crew lists
function handleFilter(filterType) {
    // Add your code here to filter the ship and crew lists based on the filterType
}