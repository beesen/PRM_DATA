let spinner;
spinner = document.getElementById('my_spinner');

function showSpinner() {
    spinner.classList.remove('d-none');
    // console.log('showSpinner');
}

function hideSpinner() {
    spinner.classList.add('d-none');
    // console.log('hideSpinner');
}

document.addEventListener('click', function (event) {
        // If the clicked element doesn't have the right selector, bail
        if (!event.target.matches('.nav-link')) return;

        // Get previous active link and remove active
        // let prevLink = document.querySelector('.active');
        // prevLink.classList.remove('active');

        // Set clicked nav link to active
        // event.target.classList.add('active');

        // Don't follow the link
        // event.preventDefault();

        // Makes spinner visible
        showSpinner();
    }
);
