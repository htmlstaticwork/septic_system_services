import os

base_dir = r"d:\March Websites\septic_system_services"

# Create directories
os.makedirs(os.path.join(base_dir, "assets", "css"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "assets", "js"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "assets", "images"), exist_ok=True)

head_template = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml"
        href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none'%3E%3Cpath d='M21 11C21 9.89543 20.1046 9 19 9H5C3.89543 9 3 9.89543 3 11V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V11Z' fill='%230f4c81'/%3E%3Cpath d='M6 7C6 6.44772 6.44772 6 7 6H10C10.5523 6 11 6.44772 11 7V9H6V7Z' fill='%230f4c81'/%3E%3Cpath d='M13 7C13 6.44772 13.4477 6 14 6H17C17.5523 6 18 6.44772 18 7V9H13V7Z' fill='%230f4c81'/%3E%3Cpath d='M1.5 13H4.5' stroke='%230f4c81' stroke-width='1.5' stroke-linecap='round'/%3E%3Cpath d='M19.5 13H22.5' stroke='%230f4c81' stroke-width='1.5' stroke-linecap='round'/%3E%3Cpath d='M10 13L11.5 14.5L15 11' stroke='white' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
    <link rel="stylesheet" href="assets/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>
<body>
"""

navbar = """
    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M21 11C21 9.89543 20.1046 9 19 9H5C3.89543 9 3 9.89543 3 11V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V11Z"
                        fill="var(--primary)" />
                    <path d="M6 7C6 6.44772 6.44772 6 7 6H10C10.5523 6 11 6.44772 11 7V9H6V7Z" fill="var(--primary)" />
                    <path d="M13 7C13 6.44772 13.4477 6 14 6H17C17.5523 6 18 6.44772 18 7V9H13V7Z" fill="var(--primary)" />
                    <path d="M1.5 13H4.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                    <path d="M19.5 13H22.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                    <path d="M10 13L11.5 14.5L15 11" stroke="white" stroke-width="1.5" stroke-linecap="round"
                        stroke-linejoin="round" />
                </svg>
                SepticCore
            </a>
            <div class="nav-menu">
                <a href="index.html">Home</a>
                <a href="home-2.html">Home 2</a>
                <a href="about.html">About</a>
                <a href="services.html">Services</a>
                <a href="blog.html">Blog</a>
                <a href="pricing.html">Pricing</a>
                <a href="contact.html">Contact</a>
                <div class="nav-actions">
                    <button id="themeToggle" class="icon-btn" aria-label="Toggle Dark Mode">🌙</button>
                    <button id="rtlToggle" class="icon-btn" aria-label="Toggle RTL">🌐</button>
                    <a href="login.html" class="btn btn-secondary">Login</a>
                    <a href="register.html" class="btn btn-secondary-outline">Signup</a>
                    <a href="dashboard.html" class="btn btn-primary">Dashboard</a>
                </div>
            </div>
            <button class="menu-toggle" aria-label="Toggle Menu">☰</button>
        </div>
    </nav>
"""

footer = """
    <footer class="footer">
        <div class="footer-container">
            <div class="footer-col">
                <h3 style="display: flex; align-items: center; gap: 8px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M21 11C21 9.89543 20.1046 9 19 9H5C3.89543 9 3 9.89543 3 11V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V11Z"
                            fill="var(--primary)" />
                        <path d="M6 7C6 6.44772 6.44772 6 7 6H10C10.5523 6 11 6.44772 11 7V9H6V7Z" fill="var(--primary)" />
                        <path d="M13 7C13 6.44772 13.4477 6 14 6H17C17.5523 6 18 6.44772 18 7V9H13V7Z"
                            fill="var(--primary)" />
                        <path d="M1.5 13H4.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M19.5 13H22.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M10 13L11.5 14.5L15 11" stroke="white" stroke-width="1.5" stroke-linecap="round"
                            stroke-linejoin="round" />
                    </svg>
                    SepticCore
                </h3>
                <p>Professional septic system pumping and installation services. 24/7 emergency support available.</p>
                <div class="social-icons">
                    <a href="#">FB</a> <a href="#">IG</a> <a href="#">X</a> <a href="#">YT</a>
                </div>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <a href="index.html">Home</a>
                <a href="about.html">About Us</a>
                <a href="blog.html">Blog</a>
                <a href="pricing.html">Pricing</a>
            </div>
            <div class="footer-col">
                <h4>Services</h4>
                <a href="services.html">Septic Pumping</a>
                <a href="services.html">System Installation</a>
                <a href="services.html">Maintenance</a>
                <a href="services.html">Inspections</a>
            </div>
            <div class="footer-col">
                <h4>Contact</h4>
                <p>📞 1-800-SEPTIC-9</p>
                <p>✉️ info@septiccore.com</p>
                <p>📍 123 Clean Water Rd, NY</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 SepticCore. All rights reserved.</p>
        </div>
    </footer>
    <script src="assets/js/main.js"></script>
</body>
</html>
"""

pages = {
    "index.html": {
        "title": "Home",
        "content": f"""
    <header class="hero">
        <div class="hero-content">
            <h1>Expert Septic Pumping & Installation</h1>
            <p>Reliable, professional, and fast septic services for residential and commercial properties.</p>
            <div class="hero-btns">
                <a href="services.html" class="btn btn-primary">Our Services</a>
                <a href="contact.html" class="btn btn-secondary">Get a Quote</a>
            </div>
        </div>
    </header>
    <section class="services-list section">
        <div class="container">
            <h2 class="section-title text-center mb-2">Our Services</h2>
            <div class="grid grid-2">
                <div class="card text-center"><h3>Septic Pumping</h3><p>Regular maintenance pumping to prevent system failures.</p></div>
                <div class="card text-center"><h3>New Installation</h3><p>Full system design and professional installation.</p></div>
                <div class="card text-center"><h3>Tank Repair</h3><p>Expert crack sealing and baffle replacements.</p></div>
                <div class="card text-center"><h3>System Inspection</h3><p>Comprehensive evaluations for real estate transactions.</p></div>
            </div>
        </div>
    </section>
    <section class="why-us section bg-alt">
        <div class="container">
            <h2 class="section-title text-center mb-2">Why Choose Us</h2>
            <div class="grid grid-3">
                <div class="feature card text-center"><h3>Licensed & Insured</h3><p>Full protection and compliance.</p></div>
                <div class="feature card text-center"><h3>Modern Equipment</h3><p>Efficient and clean operations.</p></div>
                <div class="feature card text-center"><h3>Transparent Pricing</h3><p>No hidden fees or surprises.</p></div>
            </div>
        </div>
    </section>
    <section class="emergency section">
        <div class="container text-center text-white p-4" style="background: var(--primary); border-radius: 12px; padding:40px;">
            <h2>24/7 Emergency Service</h2>
            <p>Septic backup? Don't wait. Call us immediately.</p>
            <a href="tel:18005550199" class="btn btn-secondary mt-2">Call Now: 1-800-555-0199</a>
        </div>
    </section>
    <section class="testimonials section">
        <div class="container">
            <h2 class="section-title text-center mb-2">What Our Clients Say</h2>
            <div class="grid grid-2">
                <div class="card"><p>"Fast response and absolute professionals. Highly recommend!"</p><h4 class="mt-1">- John D.</h4></div>
                <div class="card"><p>"They installed our new system perfectly and within budget."</p><h4 class="mt-1">- Sarah W.</h4></div>
            </div>
        </div>
    </section>
    <section class="cta-section section text-center">
        <div class="container">
            <h2>Ready for hassle-free septic service?</h2>
            <a href="contact.html" class="btn btn-primary mt-2">Contact Us Today</a>
        </div>
    </section>
"""
    },
    "home-2.html": {
        "title": "Home 2",
        "content": f"""
    <header class="hero hero-alt" style="align-items: center; text-align: center; background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('assets/images/hero2.jpg') center/cover;">
        <div class="hero-content">
            <h1 style="color:var(--primary);">Premium Septic Solutions</h1>
            <p>Advanced diagnostic and pumping services utilizing state-of-the-art technology.</p>
            <a href="services.html" class="btn btn-primary mt-1">Discover More</a>
        </div>
    </header>
    <section class="services-list section bg-alt">
        <div class="container">
            <h2 class="section-title text-center mb-2">Core Services</h2>
            <div class="grid grid-3">
                <div class="card text-center"><h3>Pumping</h3><p>Thorough cleaning and disposal.</p></div>
                <div class="card text-center"><h3>Installation</h3><p>Code-compliant setups.</p></div>
                <div class="card text-center"><h3>Maintenance</h3><p>Scheduled care plans.</p></div>
                <div class="card text-center"><h3>Repair</h3><p>Fast fixes for pipes and tanks.</p></div>
                <div class="card text-center"><h3>Inspection</h3><p>Camera and structural checks.</p></div>
                <div class="card text-center"><h3>Consultation</h3><p>Site planning and design.</p></div>
            </div>
        </div>
    </section>
    <section class="why-us section">
        <div class="container text-center">
            <h2 class="section-title mb-1">The SepticCore Advantage</h2>
            <p>Over 20 years of dedicated service in the region. We ensure your system running smoothly year round.</p>
        </div>
    </section>
    <section class="emergency section bg-alt">
        <div class="container text-center card">
            <h2>Need Immediate Help?</h2>
            <p>Our fleet is ready to deploy 24/7/365.</p>
            <a href="contact.html" class="btn btn-primary mt-2">Get Emergency Support</a>
        </div>
    </section>
    <section class="testimonials section">
        <div class="container">
            <h2 class="section-title text-center mb-2">Reviews</h2>
            <div class="grid grid-2">
                <div class="card" style="border-left: 4px solid var(--primary);">"Best in class service." <br><strong>- Mike T.</strong></div>
                <div class="card" style="border-left: 4px solid var(--primary);">"Very reliable and clean." <br><strong>- Anna L.</strong></div>
            </div>
        </div>
    </section>
    <section class="cta-section section text-center bg-alt">
        <div class="container">
            <h2>Join our maintenance program</h2>
            <p>Save money and prevent emergencies.</p>
            <a href="pricing.html" class="btn btn-primary mt-2">View Plans</a>
        </div>
    </section>
"""
    },
    "about.html": {
        "title": "About Us",
        "content": f"""
    <header class="page-header section text-center bg-alt">
        <div class="container">
            <h1 style="font-size:3rem; color:var(--primary);">About SepticCore</h1>
            <p>Leading the industry in waste management.</p>
        </div>
    </header>
    <section class="story section container">
        <div class="grid grid-2" style="align-items: center;">
            <div>
                <h2 class="mb-1">Our Story</h2>
                <p>Founded with a commitment to environmental safety and public health, SepticCore has grown into the leading provider of septic solutions. We utilize eco-friendly methods to ensure our community stays safe.</p>
            </div>
            <div style="height:250px; border-radius:12px; border:2px dashed var(--border); display:flex; align-items:center; justify-content:center; color:var(--text-muted);">[ Image placeholder ]</div>
        </div>
    </section>
    <section class="mission section container text-center card bg-alt">
        <h2 class="mb-1">Our Mission</h2>
        <p>To provide reliable, safe, and efficient septic services that protect our community's water supply and property values.</p>
    </section>
    <section class="team section container p-4">
        <h2 class="text-center mb-2">Meet The Team</h2>
        <div class="grid grid-3">
            <div class="card text-center"><div style="width:100px; height:100px; border-radius:50%; background:var(--bg-alt); margin:0 auto 15px auto;"></div><h3>David H.</h3><p class="text-muted">Master Installer</p></div>
            <div class="card text-center"><div style="width:100px; height:100px; border-radius:50%; background:var(--bg-alt); margin:0 auto 15px auto;"></div><h3>Mark T.</h3><p class="text-muted">Operations Mgr</p></div>
            <div class="card text-center"><div style="width:100px; height:100px; border-radius:50%; background:var(--bg-alt); margin:0 auto 15px auto;"></div><h3>Lisa G.</h3><p class="text-muted">Customer Support</p></div>
        </div>
    </section>
    <section class="cta-section section text-center bg-alt">
        <div class="container">
            <h2>Work with the best</h2>
            <a href="contact.html" class="btn btn-primary mt-2">Contact Us</a>
        </div>
    </section>
"""
    },
    "services.html": {
        "title": "Services",
        "content": f"""
    <header class="page-header section text-center bg-alt">
        <div class="container">
            <h1 style="font-size:3rem; color:var(--primary);">Our Services</h1>
            <p>Comprehensive care for your septic system</p>
        </div>
    </header>
    <section class="services section container">
        <div class="grid grid-2">
            <div class="card text-center">
                <h3>Residential Pumping</h3>
                <p>Keep your home's system healthy with routine pumping every 3-5 years.</p>
                <a href="service-details.html" class="btn btn-secondary mt-1 w-100">Learn More</a>
            </div>
            <div class="card text-center">
                <h3>Commercial Services</h3>
                <p>High-capacity solutions for businesses, restaurants, and facilities.</p>
                <a href="service-details.html" class="btn btn-secondary mt-1 w-100">Learn More</a>
            </div>
            <div class="card text-center">
                <h3>System Installation</h3>
                <p>From percolation tests to final landscaping, we handle it all.</p>
                <a href="service-details.html" class="btn btn-secondary mt-1 w-100">Learn More</a>
            </div>
            <div class="card text-center">
                <h3>Emergency Repairs</h3>
                <p>Fast response for backups, broken lines, and alarm activations.</p>
                <a href="service-details.html" class="btn btn-secondary mt-1 w-100">Learn More</a>
            </div>
            <div class="card text-center">
                <h3>Real Estate Inspections</h3>
                <p>Detailed reports and camera inspections for home buyers.</p>
                <a href="service-details.html" class="btn btn-secondary mt-1 w-100">Learn More</a>
            </div>
            <div class="card text-center">
                <h3>Drainfield Restoration</h3>
                <p>Advanced techniques to rejuvenate failing drainfields.</p>
                <a href="service-details.html" class="btn btn-secondary mt-1 w-100">Learn More</a>
            </div>
        </div>
    </section>
"""
    },
    "service-details.html": {
        "title": "Service Details",
        "content": f"""
    <header class="page-header section text-center bg-alt">
        <div class="container">
            <h1 style="font-size:3rem; color:var(--primary);">Residential Pumping</h1>
            <p>Routine care to maximize system lifespan.</p>
        </div>
    </header>
    <section class="desc section container">
        <div class="card">
            <h2 class="mb-1">Service Overview</h2>
            <p>Our residential pumping service removes all sludge and scum from your tank, ensuring optimal flow and preventing catastrophic drainfield failure. We don't just pump; we inspect every component to catch small issues before they become expensive problems.</p>
        </div>
    </section>
    <section class="steps section container p-4">
        <h2 class="text-center mb-2">How It Works</h2>
        <div class="grid grid-2">
            <div class="card">
                <h3>1. Preparation</h3>
                <p>Locate and carefully expose the tank lids without damaging landscaping.</p>
            </div>
            <div class="card">
                <h3>2. Extraction</h3>
                <p>Thoroughly agitate and pump contents using high-powered vac trucks.</p>
            </div>
            <div class="card">
                <h3>3. Inspection</h3>
                <p>Inspect inlet/outlet baffles, tank walls, and overall structural integrity.</p>
            </div>
            <div class="card">
                <h3>4. Reporting</h3>
                <p>Provide a detailed condition report and next-service timeline.</p>
            </div>
        </div>
    </section>
    <section class="benefits section bg-alt">
        <div class="container card">
            <h2 class="mb-1">Benefits</h2>
            <ul style="padding-left: 20px; line-height: 1.8;">
                <li>Prevents costly drainfield replacements.</li>
                <li>Eliminates foul odors inside and outside.</li>
                <li>Ensures smooth plumbing operations.</li>
                <li>Complies with local health department regulations.</li>
            </ul>
        </div>
    </section>
    <section class="cta-section section text-center">
        <div class="container">
            <h2>Schedule your pump out today</h2>
            <a href="contact.html" class="btn btn-primary mt-2">Book Now</a>
        </div>
    </section>
"""
    },
    "blog.html": {
        "title": "Blog",
        "content": f"""
    <header class="page-header section text-center bg-alt">
        <div class="container">
            <h1 style="font-size:3rem; color:var(--primary);">Septic Knowledge Base</h1>
            <p>Tips, guides, and news.</p>
        </div>
    </header>
    <section class="blog-grid section container">
        <div class="grid grid-2">
            <div class="card">
                <div style="height:200px; background:var(--bg-alt); margin:-30px -30px 20px -30px; border-radius: 12px 12px 0 0; display:flex; align-items:center; justify-content:center; border-bottom:1px solid var(--border);">[ Image placeholder ]</div>
                <h3>How Often Should You Pump?</h3>
                <p>A guide to maintenance schedules based on family size.</p>
                <a href="blog-details.html" class="btn btn-secondary mt-1">Read More</a>
            </div>
            <div class="card">
                <div style="height:200px; background:var(--bg-alt); margin:-30px -30px 20px -30px; border-radius: 12px 12px 0 0; display:flex; align-items:center; justify-content:center; border-bottom:1px solid var(--border);">[ Image placeholder ]</div>
                <h3>Signs of a Failing Drainfield</h3>
                <p>Watch out for these 5 common indicators.</p>
                <a href="blog-details.html" class="btn btn-secondary mt-1">Read More</a>
            </div>
            <div class="card">
                <div style="height:200px; background:var(--bg-alt); margin:-30px -30px 20px -30px; border-radius: 12px 12px 0 0; display:flex; align-items:center; justify-content:center; border-bottom:1px solid var(--border);">[ Image placeholder ]</div>
                <h3>What NOT to Flush</h3>
                <p>Protect your system by keeping these items out of the drain.</p>
                <a href="blog-details.html" class="btn btn-secondary mt-1">Read More</a>
            </div>
            <div class="card">
                <div style="height:200px; background:var(--bg-alt); margin:-30px -30px 20px -30px; border-radius: 12px 12px 0 0; display:flex; align-items:center; justify-content:center; border-bottom:1px solid var(--border);">[ Image placeholder ]</div>
                <h3>New Installation Guide</h3>
                <p>What to expect when replacing your septic tank.</p>
                <a href="blog-details.html" class="btn btn-secondary mt-1">Read More</a>
            </div>
        </div>
    </section>
"""
    },
    "blog-details.html": {
        "title": "Blog Details",
        "content": f"""
    <div class="container section">
        <header class="blog-header" style="max-width: 800px; margin: 0 auto; text-align:center;">
            <h1 style="font-size:2.5rem; color:var(--primary);">How Often Should You Pump?</h1>
            <p style="color:var(--text-muted); margin-top:10px;">Published on Oct 12, 2026 | By SepticCore Team</p>
        </header>
        <div class="blog-content" style="max-width: 800px; margin: 2rem auto; line-height: 1.8;">
            <div style="height:400px; background:var(--bg-alt); border-radius:12px; margin-bottom: 2rem; border:1px solid var(--border);"></div>
            <p>One of the most common questions we receive is about pumping frequency. The truth is, there is no one-size-fits-all answer, but there are clear guidelines.</p>
            <h2 class="mt-2 mb-1">Factors to Consider</h2>
            <ul>
                <li><strong>Household Size:</strong> More people means more water and waste.</li>
                <li><strong>Tank Size:</strong> Smaller tanks fill up faster.</li>
                <li><strong>Garbage Disposal Usage:</strong> Increases solid waste significantly.</li>
            </ul>
            <p class="mt-1">We generally recommend pumping every 3-5 years for a typical residential system. Commercial systems may require annual or even quarterly service.</p>
            <div class="card mt-2 text-center bg-alt">
                <h3>Need a professional assessment?</h3>
                <a href="contact.html" class="btn btn-primary mt-1">Contact Us</a>
            </div>
        </div>
    </div>
"""
    },
    "pricing.html": {
        "title": "Pricing",
        "content": f"""
    <header class="page-header section text-center bg-alt">
        <div class="container">
            <h1 style="font-size:3rem; color:var(--primary);">Transparent Pricing</h1>
            <p>No hidden fees.</p>
        </div>
    </header>
    <section class="pricing-cards section container">
        <div class="grid grid-3" style="align-items: center;">
            <div class="card text-center">
                <h3>Basic Pump</h3>
                <h2 style="font-size: 2.5rem; margin:1rem 0; color:var(--text)">$299</h2>
                <ul style="list-style:none; padding:0; line-height:2.5; border-top:1px solid var(--border); padding-top:1rem; margin-bottom:1rem;">
                    <li>1000 Gal Tank</li>
                    <li>Visual Inspection</li>
                    <li>Basic Report</li>
                </ul>
                <a href="contact.html" class="btn btn-secondary w-100">Choose Plan</a>
            </div>
            <div class="card text-center" style="transform: scale(1.05); border: 2px solid var(--primary); z-index:2; position:relative; padding:40px 30px;">
                <div style="background:var(--primary); color:#fff; position:absolute; top:0; left:0; right:0; padding: 0.5rem; border-radius: 8px 8px 0 0; font-weight:bold;">Popular Plan</div>
                <h3 style="margin-top:10px;">Standard Care</h3>
                <h2 style="font-size: 3rem; margin:1rem 0; color:var(--primary)">$399</h2>
                <ul style="list-style:none; padding:0; line-height:2.5; border-top:1px solid var(--border); padding-top:1rem; margin-bottom:1rem;">
                    <li>Up to 1500 Gal Tank</li>
                    <li>Baffle Inspection</li>
                    <li>Filter Cleaning</li>
                </ul>
                <a href="contact.html" class="btn btn-primary w-100">Choose Plan</a>
            </div>
            <div class="card text-center">
                <h3>Full Maintenance</h3>
                <h2 style="font-size: 2.5rem; margin:1rem 0; color:var(--text)">$599</h2>
                <ul style="list-style:none; padding:0; line-height:2.5; border-top:1px solid var(--border); padding-top:1rem; margin-bottom:1rem;">
                    <li>Any Size Residential</li>
                    <li>Camera Inspection</li>
                    <li>Bacterial Additive</li>
                </ul>
                <a href="contact.html" class="btn btn-secondary w-100">Choose Plan</a>
            </div>
        </div>
    </section>
"""
    },
    "contact.html": {
        "title": "Contact Us",
        "content": f"""
    <header class="page-header section text-center bg-alt">
        <div class="container">
            <h1 style="font-size:3rem; color:var(--primary);">Contact Us</h1>
            <p>We're here to help, 24/7.</p>
        </div>
    </header>
    <section class="contact-section section container">
        <div class="grid grid-2">
            <div class="contact-info card">
                <h2 class="mb-1">Get in touch</h2>
                <p><strong>Phone:</strong> <br><a href="tel:1800SEPTIC9" style="color:var(--primary);">1-800-SEPTIC-9</a></p>
                <p class="mt-1"><strong>Email:</strong> <br><a href="mailto:info@septiccore.com" style="color:var(--primary);">info@septiccore.com</a></p>
                <p class="mt-1"><strong>Address:</strong> <br>123 Clean Water Rd, NY 10001</p>
                <div class="map mt-2" style="height:250px; background:var(--bg-alt); border-radius:8px; display:flex; align-items:center; justify-content:center; border:1px solid var(--border);">
                    [ Map Placeholder ]
                </div>
            </div>
            <div class="card">
                <h2 class="mb-1">Send a Message</h2>
                <form id="contactForm" onsubmit="event.preventDefault(); alert('Message sent!');">
                    <div class="form-group mb-1">
                        <label style="font-weight:bold; display:block; margin-bottom:5px;">Name</label>
                        <input type="text" class="form-control" required style="width:100%">
                    </div>
                    <div class="form-group mb-1">
                        <label style="font-weight:bold; display:block; margin-bottom:5px;">Email</label>
                        <input type="email" class="form-control" required style="width:100%">
                    </div>
                    <div class="form-group mb-1">
                        <label style="font-weight:bold; display:block; margin-bottom:5px;">Message</label>
                        <textarea class="form-control" rows="5" required style="width:100%"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary w-100 mt-1">Send Message</button>
                </form>
            </div>
        </div>
    </section>
"""
    },
    "404.html": {
        "title": "Page Not Found",
        "content": f"""
    <section class="section container text-center" style="padding: 100px 20px; min-height:60vh; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="font-size: 8rem; color: var(--primary); font-weight:bold; line-height:1;">404</h1>
        <h2 style="font-size: 2rem; margin-bottom:10px;">Oops! Page Not Found</h2>
        <p class="mb-2 text-muted">The page you are looking for does not exist or has been moved.</p>
        <a href="index.html" class="btn btn-primary">Back to Home</a>
    </section>
"""
    },
    "coming-soon.html": {
        "title": "Coming Soon",
        "content": f"""
    <section class="section container text-center" style="padding: 100px 20px; min-height:60vh; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="font-size: 4rem; color: var(--primary); margin-bottom:10px;">Coming Soon</h1>
        <p class="mb-2 text-muted" style="font-size:1.2rem;">We are working on something awesome. Stay tuned!</p>
        <div style="font-size: 2rem; font-weight:bold; margin-bottom:2rem; background:var(--bg-alt); padding:20px; border-radius:12px; border:1px solid var(--border);">
            <span style="color:var(--primary);">12</span> D : <span style="color:var(--primary);">05</span> H : <span style="color:var(--primary);">45</span> M
        </div>
        <form style="width:100%; max-width:400px; display:flex; gap:10px;">
            <input type="email" class="form-control" placeholder="Enter email" required style="flex:1;">
            <button class="btn btn-primary">Notify Me</button>
        </form>
    </section>
"""
    }
}

for filename, info in pages.items():
    html = head_template.format(title=info["title"]) + navbar + info["content"] + footer
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)
        
auth_head = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - SepticCore</title>
    <link rel="icon" type="image/svg+xml"
        href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none'%3E%3Cpath d='M21 11C21 9.89543 20.1046 9 19 9H5C3.89543 9 3 9.89543 3 11V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V11Z' fill='%230f4c81'/%3E%3Cpath d='M6 7C6 6.44772 6.44772 6 7 6H10C10.5523 6 11 6.44772 11 7V9H6V7Z' fill='%230f4c81'/%3E%3Cpath d='M13 7C13 6.44772 13.4477 6 14 6H17C17.5523 6 18 6.44772 18 7V9H13V7Z' fill='%230f4c81'/%3E%3Cpath d='M1.5 13H4.5' stroke='%230f4c81' stroke-width='1.5' stroke-linecap='round'/%3E%3Cpath d='M19.5 13H22.5' stroke='%230f4c81' stroke-width='1.5' stroke-linecap='round'/%3E%3Cpath d='M10 13L11.5 14.5L15 11' stroke='white' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
    <link rel="stylesheet" href="assets/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>
<body class="auth-body" style="display:flex; align-items:center; justify-content:center; min-height:100vh; background:var(--bg-alt); padding:20px;">
"""

auth_pages = {
    "login.html": {
        "title": "Login",
        "content": """
    <div class="card auth-card" style="width:100%; max-width:400px; text-align:center;">
        <div style="display:flex; justify-content:flex-end; gap:10px; margin-bottom:1rem;">
            <button id="themeToggle" class="icon-btn" aria-label="Toggle Dark Mode">🌙</button>
            <button id="rtlToggle" class="icon-btn" aria-label="Toggle RTL">🌐</button>
        </div>
        <a href="index.html" class="logo" style="justify-content:center; margin-bottom:20px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M21 11C21 9.89543 20.1046 9 19 9H5C3.89543 9 3 9.89543 3 11V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V11Z"
                    fill="var(--primary)" />
                <path d="M6 7C6 6.44772 6.44772 6 7 6H10C10.5523 6 11 6.44772 11 7V9H6V7Z" fill="var(--primary)" />
                <path d="M13 7C13 6.44772 13.4477 6 14 6H17C17.5523 6 18 6.44772 18 7V9H13V7Z" fill="var(--primary)" />
                <path d="M1.5 13H4.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                <path d="M19.5 13H22.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                <path d="M10 13L11.5 14.5L15 11" stroke="white" stroke-width="1.5" stroke-linecap="round"
                    stroke-linejoin="round" />
            </svg>
            <span style="font-size: 2rem; font-weight: bold; margin-left: 10px;">SepticCore</span>
        </a>
        <h2 class="mb-2">Login to Account</h2>
        <form onsubmit="event.preventDefault(); window.location.href='dashboard.html';">
            <div class="form-group mb-1 text-left">
                <input type="email" class="form-control" placeholder="Email Address" required>
            </div>
            <div class="form-group mb-1 text-left" style="position:relative;">
                <input type="password" class="form-control" placeholder="Password" id="password" required>
                <button type="button" onclick="document.getElementById('password').type = document.getElementById('password').type === 'password' ? 'text' : 'password'" style="position:absolute; right:15px; top:50%; transform:translateY(-50%); background:none; border:none; cursor:pointer;">👁️</button>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; font-size:0.9rem;">
                <label style="display:flex; align-items:center; gap:5px;"><input type="checkbox"> Remember Me</label>
                <a href="#" style="color:var(--primary); font-weight:600;">Forgot Password?</a>
            </div>
            <button type="submit" class="btn btn-primary w-100 mb-1">Login</button>
            <div style="margin:1rem 0; color:var(--text-muted); position:relative;">
                <hr style="border-top:1px solid var(--border); border-bottom:none;">
                <span style="position:absolute; top:-10px; left:50%; transform:translateX(-50%); background:var(--card-bg); padding:0 10px;">or continue with</span>
            </div>
            <div style="display:flex; gap:10px;">
                <button type="button" class="btn btn-secondary" style="flex:1;">Google</button>
                <button type="button" class="btn btn-secondary" style="flex:1;">Apple</button>
            </div>
            <p class="mt-2 text-center text-muted">Don't have an account? <a href="register.html" style="color:var(--primary); font-weight:600;">Register</a></p>
        </form>
    </div>
"""
    },
    "register.html": {
        "title": "Register",
        "content": """
    <div class="card auth-card" style="width:100%; max-width:400px; text-align:center;">
        <div style="display:flex; justify-content:flex-end; gap:10px; margin-bottom:1rem;">
            <button id="themeToggle" class="icon-btn" aria-label="Toggle Dark Mode">🌙</button>
            <button id="rtlToggle" class="icon-btn" aria-label="Toggle RTL">🌐</button>
        </div>
        <a href="index.html" class="logo" style="justify-content:center; margin-bottom:20px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M21 11C21 9.89543 20.1046 9 19 9H5C3.89543 9 3 9.89543 3 11V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V11Z"
                    fill="var(--primary)" />
                <path d="M6 7C6 6.44772 6.44772 6 7 6H10C10.5523 6 11 6.44772 11 7V9H6V7Z" fill="var(--primary)" />
                <path d="M13 7C13 6.44772 13.4477 6 14 6H17C17.5523 6 18 6.44772 18 7V9H13V7Z" fill="var(--primary)" />
                <path d="M1.5 13H4.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                <path d="M19.5 13H22.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                <path d="M10 13L11.5 14.5L15 11" stroke="white" stroke-width="1.5" stroke-linecap="round"
                    stroke-linejoin="round" />
            </svg>
            <span style="font-size: 2rem; font-weight: bold; margin-left: 10px;">SepticCore</span>
        </a>
        <h2 class="mb-2">Create Account</h2>
        <form onsubmit="event.preventDefault(); window.location.href='login.html';">
            <div class="form-group mb-1">
                <input type="text" class="form-control" placeholder="Full Name" required>
            </div>
            <div class="form-group mb-1">
                <input type="email" class="form-control" placeholder="Email Address" required>
            </div>
            <div class="form-group mb-1">
                <input type="tel" class="form-control" placeholder="Phone Number" required>
            </div>
            <div class="form-group mb-1" style="position:relative;">
                <input type="password" class="form-control" placeholder="Password" id="reg-password" required>
            </div>
            <button type="submit" class="btn btn-primary w-100 mt-1 mb-1">Sign Up</button>
            <div style="margin:1rem 0; color:var(--text-muted); position:relative;">
                <hr style="border-top:1px solid var(--border); border-bottom:none;">
                <span style="position:absolute; top:-10px; left:50%; transform:translateX(-50%); background:var(--card-bg); padding:0 10px;">or continue with</span>
            </div>
            <div style="display:flex; gap:10px;">
                <button type="button" class="btn btn-secondary" style="flex:1;">Google</button>
                <button type="button" class="btn btn-secondary" style="flex:1;">Apple</button>
            </div>
            <p class="mt-2 text-center text-muted">Already have an account? <a href="login.html" style="color:var(--primary); font-weight:600;">Login</a></p>
        </form>
    </div>
"""
    }
}

for filename, info in auth_pages.items():
    html = auth_head.format(title=info["title"]) + info["content"] + '<script src="assets/js/main.js"></script></body></html>'
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)

dashboard_html = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - SepticCore</title>
    <link rel="icon" type="image/svg+xml"
        href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none'%3E%3Cpath d='M21 11C21 9.89543 20.1046 9 19 9H5C3.89543 9 3 9.89543 3 11V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V11Z' fill='%230f4c81'/%3E%3Cpath d='M6 7C6 6.44772 6.44772 6 7 6H10C10.5523 6 11 6.44772 11 7V9H6V7Z' fill='%230f4c81'/%3E%3Cpath d='M13 7C13 6.44772 13.4477 6 14 6H17C17.5523 6 18 6.44772 18 7V9H13V7Z' fill='%230f4c81'/%3E%3Cpath d='M1.5 13H4.5' stroke='%230f4c81' stroke-width='1.5' stroke-linecap='round'/%3E%3Cpath d='M19.5 13H22.5' stroke='%230f4c81' stroke-width='1.5' stroke-linecap='round'/%3E%3Cpath d='M10 13L11.5 14.5L15 11' stroke='white' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
    <link rel="stylesheet" href="assets/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        .dashboard-container { display: flex; min-height: 100vh; background:var(--bg-alt); }
        .sidebar { width: 260px; background: var(--card-bg); border-right: 1px solid var(--border); display: flex; flex-direction: column; position: fixed; left:0; top:0; height: 100vh; transition: 0.3s; z-index: 1000; }
        .sidebar-header { padding: 20px; font-size: 1.5rem; font-weight: bold; border-bottom: 1px solid var(--border); display:flex; justify-content:space-between; align-items:center; }
        .sidebar-nav { flex: 1; padding: 20px 0; overflow-y: auto; display:flex; flex-direction:column; gap:5px; }
        .sidebar-nav a { display: block; padding: 12px 20px; color: var(--text-muted); text-decoration: none; transition: 0.3s; font-weight:500; border-left: 4px solid transparent; }
        .sidebar-nav a:hover, .sidebar-nav a.active { background: var(--bg-alt); color: var(--primary); border-left: 4px solid var(--primary); }
        .sidebar-footer { padding: 20px; border-top: 1px solid var(--border); display: flex; flex-direction:column; gap:15px; }
        .main-content { flex: 1; padding: 30px; margin-left: 260px; transition: 0.3s; }
        html[dir="rtl"] .sidebar { left:auto; right:0; border-right: none; border-left: 1px solid var(--border); }
        html[dir="rtl"] .sidebar-nav a { border-left: none; border-right: 4px solid transparent; }
        html[dir="rtl"] .sidebar-nav a:hover, html[dir="rtl"] .sidebar-nav a.active { border-right: 4px solid var(--primary); }
        html[dir="rtl"] .main-content { margin-left: 0; margin-right: 260px; }
        .dashboard-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; background:var(--card-bg); padding:15px 20px; border-radius:12px; box-shadow:0 2px 10px var(--shadow); }
        .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .metric-card { background: var(--card-bg); padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px var(--shadow); }
        .metric-card h3 { font-size: 1rem; color: var(--text-muted); margin-bottom: 10px; font-weight:500; }
        .metric-card div { font-size: 2rem; font-weight: bold; color: var(--primary); }
        
        .overlay { display:none; position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(0,0,0,0.5); z-index:999; }
        
        @media (max-width: 991px) {
            .sidebar { transform: translateX(-100%); }
            html[dir="rtl"] .sidebar { transform: translateX(100%); }
            .sidebar.active { transform: translateX(0); }
            .main-content { margin-left: 0; }
            html[dir="rtl"] .main-content { margin-right: 0; }
            .overlay.active { display:block; }
        }
    </style>
</head>
<body>
    <div class="overlay" id="dashboardOverlay"></div>
    <div class="dashboard-container">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <a href="index.html" class="logo" style="text-decoration:none;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M21 11C21 9.89543 20.1046 9 19 9H5C3.89543 9 3 9.89543 3 11V17C3 18.1046 3.89543 19 5 19H19C20.1046 19 21 18.1046 21 17V11Z"
                            fill="var(--primary)" />
                        <path d="M6 7C6 6.44772 6.44772 6 7 6H10C10.5523 6 11 6.44772 11 7V9H6V7Z" fill="var(--primary)" />
                        <path d="M13 7C13 6.44772 13.4477 6 14 6H17C17.5523 6 18 6.44772 18 7V9H13V7Z"
                            fill="var(--primary)" />
                        <path d="M1.5 13H4.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M19.5 13H22.5" stroke="var(--primary)" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M10 13L11.5 14.5L15 11" stroke="white" stroke-width="1.5" stroke-linecap="round"
                            stroke-linejoin="round" />
                    </svg>
                    SepticCore
                </a>
                <button id="closeSidebar" class="icon-btn" style="display:none;">✕</button>
            </div>
            <nav class="sidebar-nav">
                <a href="#" class="active">Dashboard</a>
                <a href="#">Schedule Service</a>
                <a href="#">Maintenance History</a>
                <a href="#">Reports</a>
                <a href="#">Profile</a>
            </nav>
            <div class="sidebar-footer">
                <div style="display:flex; justify-content:space-around;">
                    <button id="themeToggle" class="icon-btn" aria-label="Toggle Dark Mode">🌙</button>
                    <button id="rtlToggle" class="icon-btn" aria-label="Toggle RTL">🌐</button>
                </div>
                <button id="logoutBtn" class="btn btn-secondary w-100">Logout</button>
            </div>
        </aside>
        
        <main class="main-content">
            <header class="dashboard-header">
                <div style="display:flex; align-items:center; gap:15px;">
                    <button id="mobileMenuBtn" class="icon-btn" style="display:none; font-size:1.5rem;">☰</button>
                    <h2 style="font-size:1.5rem;">Welcome Back, User!</h2>
                </div>
                <div class="user-profile" style="display:flex; align-items:center; gap:10px;">
                    <span style="font-weight:600; display:none;">John Doe</span>
                    <div style="width:45px; height:45px; background:var(--primary); border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold;">JD</div>
                </div>
            </header>
            
            <section class="metrics-grid">
                <div class="metric-card">
                    <h3>Next Service</h3>
                    <div style="font-size:1.5rem">Oct 24, 2026</div>
                </div>
                <div class="metric-card">
                    <h3>System Health</h3>
                    <div style="color:#28a745;">Good</div>
                </div>
                <div class="metric-card">
                    <h3>Past Services</h3>
                    <div>3</div>
                </div>
                <div class="metric-card">
                    <h3>Active Alerts</h3>
                    <div style="color:#dc3545;">0</div>
                </div>
            </section>
            
            <section class="notifications-section">
                <h3 class="mb-2">Recent Notifications</h3>
                <div class="card mb-1" style="border-left:4px solid var(--primary); padding:20px;">
                    <p><strong>Reminder:</strong> Your bio-additive supply is running low.</p>
                </div>
                <div class="card mb-1" style="border-left:4px solid #28a745; padding:20px;">
                    <p><strong>System:</strong> Maintenance record updated attached to oct 15 service.</p>
                </div>
            </section>
        </main>
    </div>
    <script src="assets/js/main.js"></script>
    <script src="assets/js/dashboard.js"></script>
</body>
</html>
"""

with open(os.path.join(base_dir, "dashboard.html"), "w", encoding="utf-8") as f:
    f.write(dashboard_html)

css = """
:root {
    --primary: #0056b3;
    --primary-hover: #004494;
    --secondary: #f8f9fa;
    --text: #333333;
    --text-muted: #666666;
    --bg: #ffffff;
    --bg-alt: #f4f7f6;
    --card-bg: #ffffff;
    --border: #e0e0e0;
    --shadow: rgba(0,0,0,0.1);
}

[data-theme="dark"] {
    --primary: #3399ff;
    --primary-hover: #66b2ff;
    --secondary: #2c2c2c;
    --text: #f0f0f0;
    --text-muted: #aaaaaa;
    --bg: #121212;
    --bg-alt: #1e1e1e;
    --card-bg: #242424;
    --border: #333333;
    --shadow: rgba(0,0,0,0.5);
}

* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; transition: background 0.3s, color 0.3s; }
a { text-decoration: none; color: inherit; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.section { padding: 80px 0; }
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-muted { color: var(--text-muted); }
.bg-alt { background: var(--bg-alt); }
.mt-1 { margin-top: 1rem; } .mt-2 { margin-top: 2rem; }
.mb-1 { margin-bottom: 1rem; } .mb-2 { margin-bottom: 2rem; }
.w-100 { width: 100%; }

/* Buttons */
.btn { display: inline-block; padding: 12px 28px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: 0.3s; border: none; text-align:center; font-size:1rem; }
.btn-primary { background: var(--primary); color: #fff; }
.btn-primary:hover { background: var(--primary-hover); }
.btn-secondary { background: var(--secondary); color: var(--text); border: 1px solid var(--border); }
.btn-secondary:hover { background: var(--border); }
.icon-btn { background: none; border: none; font-size: 1.2rem; cursor: pointer; padding: 5px; color: var(--text); border-radius:50%; width:40px; height:40px; display:inline-flex; align-items:center; justify-content:center; }
.icon-btn:hover { background: var(--bg-alt); }

/* Forms */
.form-group { margin-bottom: 15px; }
.form-control { width: 100%; padding: 14px; border: 1px solid var(--border); border-radius: 8px; background: var(--card-bg); color: var(--text); outline: none; transition: border-color 0.3s, box-shadow 0.3s; font-family: inherit; }
.form-control:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(0,86,179,0.1); }

/* Grid */
.grid { display: grid; gap: 30px; }
.grid-2 { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.grid-3 { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }

/* Cards */
.card { background: var(--card-bg); padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px var(--shadow); transition: transform 0.3s, box-shadow 0.3s; }
.card:hover { transform: translateY(-5px); box-shadow: 0 8px 30px var(--shadow); }

/* Navbar */
.navbar { position: sticky; top: 0; background: var(--card-bg); box-shadow: 0 2px 10px var(--shadow); z-index: 1000; }
.nav-container { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 15px 20px; }
.logo { font-size: 1.5rem; font-weight: 700; color: var(--primary); display: flex; align-items: center; gap: 5px; }
.nav-menu { display: flex; align-items: center; gap: 20px; }
.nav-menu a:not(.btn) { font-weight: 600; font-size: 0.95rem; color:var(--text); transition:0.3s; }
.nav-menu a:hover:not(.btn) { color: var(--primary); }
.nav-actions { display: flex; align-items: center; gap: 15px; }
.menu-toggle { display: none; background:none; border:none; font-size:1.8rem; color:var(--text); cursor:pointer;}

/* Hero */
.hero { padding: 100px 20px; background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('assets/images/hero.jpg') center/cover; color: #fff; display:flex; align-items:center; justify-content:center; text-align:center; min-height:60vh; }
.hero-content { max-width: 800px; }
.hero h1 { font-size: 3.5rem; margin-bottom: 20px; line-height:1.2; font-weight:700; }
.hero p { font-size: 1.25rem; margin-bottom: 30px; color:#e0e0e0; }
.hero-btns { display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; }

/* Dashboard Card */
.auth-card { padding: 40px; box-shadow: 0 10px 30px var(--shadow); border-radius: 16px; }

/* Footer */
.footer { background: var(--card-bg); padding: 60px 20px 20px; border-top: 1px solid var(--border); }
.footer-container { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; }
.footer-col h3, .footer-col h4 { margin-bottom: 20px; font-weight:700; }
.footer-col h3 { color: var(--primary); font-size:1.5rem; }
.footer-col a { display: block; margin-bottom: 12px; color: var(--text-muted); font-weight:500; transition:0.3s; }
.footer-col a:hover { color: var(--primary); transform:translateX(5px); }
.footer-bottom { text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid var(--border); color: var(--text-muted); font-weight:500; }
.social-icons { display:flex; gap:10px; margin-top:15px; }
.social-icons a { width:40px; height:40px; background:var(--bg-alt); display:flex; align-items:center; justify-content:center; border-radius:50%; margin-bottom:0; color:var(--text); transition:0.3s;}
.social-icons a:hover { background:var(--primary); color:#fff; transform:translateY(-3px);}

/* RTL Support */
html[dir="rtl"] { direction: rtl; }
html[dir="rtl"] .nav-actions { margin-left: auto; margin-right: 0; }
html[dir="rtl"] .form-group.text-left { text-align: right; }
html[dir="rtl"] .logo-icon { margin-left: 5px; margin-right: 0;}
html[dir="rtl"] .footer-col a:hover { transform:translateX(-5px); }

@media (max-width: 1024px) {
    .nav-menu { position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); background: var(--card-bg); flex-direction: column; padding: 40px 20px; transition: 0.3s; overflow-y: auto; align-items: flex-start; z-index:999; }
    html[dir="rtl"] .nav-menu { left: auto; right: -100%; }
    .nav-menu.active { left: 0; }
    html[dir="rtl"] .nav-menu.active { right: 0; }
    .menu-toggle { display: block; }
    .nav-actions { flex-direction: column; width: 100%; align-items: stretch; margin-top: 30px; border-top:1px solid var(--border); padding-top:20px; }
    .nav-actions .btn { text-align:center; }
    .hero h1 { font-size: 2.8rem; }
}

@media (max-width: 768px) {
    .grid { grid-template-columns: 1fr !important; }
    .hero h1 { font-size: 2.2rem; }
    .section { padding: 50px 0; }
}
"""

with open(os.path.join(base_dir, "assets", "css", "style.css"), "w", encoding="utf-8") as f:
    f.write(css)

main_js = """
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
});
"""

with open(os.path.join(base_dir, "assets", "js", "main.js"), "w", encoding="utf-8") as f:
    f.write(main_js)

dashboard_js = """
document.addEventListener('DOMContentLoaded', () => {
    // Dashboard specific logic
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
        sidebar.classList.toggle('active');
        overlay.classList.toggle('active');
    }

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', toggleSidebar);
    if (closeSidebarBtn) closeSidebarBtn.addEventListener('click', toggleSidebar);
    if (overlay) overlay.addEventListener('click', toggleSidebar);
});
"""

with open(os.path.join(base_dir, "assets", "js", "dashboard.js"), "w", encoding="utf-8") as f:
    f.write(dashboard_js)

print("Site generation complete.")
