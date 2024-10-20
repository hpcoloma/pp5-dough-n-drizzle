function toggleNavbar() {
    var nav = document.getElementById('mobile-nav');
    if (nav.classList.contains('show')) {
        nav.classList.remove('show');
    } else {
        nav.classList.add('show');
    }
}