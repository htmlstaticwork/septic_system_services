document.addEventListener('DOMContentLoaded', () => {
    // Dashboard logout handling
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.location.href = 'index.html';
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
