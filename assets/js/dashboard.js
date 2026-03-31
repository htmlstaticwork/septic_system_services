document.addEventListener('DOMContentLoaded', () => {
    // Dashboard logout handling
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.location.href = 'index.html';
        });
    }
    
    // Panel switching logic
    const navLinks = {
        'nav-dashboard': 'dashboard-panel',
        'nav-schedule': 'schedule-panel',
        'nav-history': 'history-panel',
        'nav-reports': 'reports-panel',
        'nav-profile': 'profile-panel'
    };

    function switchPanel(panelId) {
        // Hide all panels
        document.querySelectorAll('.dashboard-panel').forEach(panel => {
            panel.style.display = 'none';
            panel.classList.remove('active');
        });

        // Show target panel
        const targetPanel = document.getElementById(panelId);
        if (targetPanel) {
            targetPanel.style.display = 'block';
            targetPanel.classList.add('active');
        }

        // Update active class in sidebar
        document.querySelectorAll('.sidebar-nav a').forEach(link => {
            link.classList.remove('active');
        });

        // Find the link that points to this panel
        for (const [linkId, pId] of Object.entries(navLinks)) {
            if (pId === panelId) {
                const activeLink = document.getElementById(linkId);
                if (activeLink) activeLink.classList.add('active');
                break;
            }
        }

        // Close sidebar on mobile
        if(window.innerWidth <= 991) {
            if(sidebar) sidebar.classList.remove('active');
            if(overlay) overlay.classList.remove('active');
        }

        // Scroll to top of main content
        window.scrollTo(0, 0);
    }

    // Add click listeners to sidebar links
    Object.keys(navLinks).forEach(linkId => {
        const link = document.getElementById(linkId);
        if (link) {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                switchPanel(navLinks[linkId]);
            });
        }
    });

    // Quick book button listener
    const quickBookBtn = document.getElementById('quick-book-btn');
    if (quickBookBtn) {
        quickBookBtn.addEventListener('click', (e) => {
            e.preventDefault();
            switchPanel('schedule-panel');
        });
    }

    // Sidebar user profile click listener
    const sidebarUser = document.querySelector('.sidebar-user');

    if (sidebarUser) {
        sidebarUser.addEventListener('click', () => {
            switchPanel('profile-panel');
        });
    }



    // Mobile Sidebar toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const closeSidebarBtn = document.getElementById('closeSidebar');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('dashboardOverlay');
    
    function checkWidth() {
        if(window.innerWidth <= 991) {
            if(mobileMenuBtn) mobileMenuBtn.style.display = 'block';
            if(closeSidebarBtn) closeSidebarBtn.style.display = 'block';
        } else {
            if(mobileMenuBtn) mobileMenuBtn.style.display = 'none';
            if(closeSidebarBtn) closeSidebarBtn.style.display = 'none';
            if(sidebar) sidebar.classList.remove('active');
            if(overlay) overlay.classList.remove('active');
        }
    }
    
    checkWidth();
    window.addEventListener('resize', checkWidth);

    function toggleSidebar() {
        if(sidebar) sidebar.classList.toggle('active');
        if(overlay) overlay.classList.toggle('active');
    }

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', toggleSidebar);
    if (closeSidebarBtn) closeSidebarBtn.addEventListener('click', toggleSidebar);
    if (overlay) overlay.addEventListener('click', toggleSidebar);
});
