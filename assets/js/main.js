document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeBtns = document.querySelectorAll('#themeToggle');
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    const sunIcon = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;
    const moonIcon = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;

    themeBtns.forEach(btn => {
        btn.innerHTML = savedTheme === 'dark' ? sunIcon : moonIcon;
        btn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            themeBtns.forEach(b => b.innerHTML = newTheme === 'dark' ? sunIcon : moonIcon);
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

    // Back to Top functionality
    const backToTopBtn = document.querySelector('#backToTop');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Active Page Detection
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-menu a:not(.btn)').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});
