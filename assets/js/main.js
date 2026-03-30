document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeBtns = document.querySelectorAll('#themeToggle');
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    themeBtns.forEach(btn => {
        btn.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
        btn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            themeBtns.forEach(b => b.textContent = newTheme === 'dark' ? '☀️' : '🌙');
        });
    });

    // RTL Toggle
    const rtlBtns = document.querySelectorAll('#rtlToggle');
    const savedDir = localStorage.getItem('dir') || 'ltr';
    document.documentElement.setAttribute('dir', savedDir);
    
    rtlBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const currentDir = document.documentElement.getAttribute('dir');
            const newDir = currentDir === 'ltr' ? 'rtl' : 'ltr';
            document.documentElement.setAttribute('dir', newDir);
            localStorage.setItem('dir', newDir);
        });
    });

    // Mobile Menu
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            menuToggle.textContent = navMenu.classList.contains('active') ? '✕' : '☰';
        });
    }

    // Form submission mock
    const forms = document.querySelectorAll('form:not([id="loginForm"]):not([id="regForm"])');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            if(!form.action || form.action.includes(window.location.hostname)) {
                 e.preventDefault();
                 alert('Form submitted successfully!');
            }
        });
    });
});
