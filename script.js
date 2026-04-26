/**
 * Paul Boubert Portfolio - Premium Interactivity
 */

document.addEventListener('DOMContentLoaded', () => {
    // ===================================
    // Custom Cursor
    // ===================================
    const cursor = document.querySelector('.cursor');
    const follower = document.querySelector('.cursor-follower');
    const links = document.querySelectorAll('a, button, .filter-btn, .gallery-item, .btn-back');

    let mouseX = 0;
    let mouseY = 0;
    let cursorX = 0;
    let cursorY = 0;
    let followerX = 0;
    let followerY = 0;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        // Show cursor if it was hidden
        if (cursor) cursor.style.opacity = '1';
        if (follower) follower.style.opacity = '1';
    });

    const animate = () => {
        // Smoothing factor for the follower
        followerX += (mouseX - followerX) * 0.15;
        followerY += (mouseY - followerY) * 0.15;

        if (cursor) {
            // Instant dot position
            cursor.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
        }
        if (follower) {
            // Smoothed follower position
            follower.style.transform = `translate3d(${followerX}px, ${followerY}px, 0) translate(-50%, -50%)`;
        }

        requestAnimationFrame(animate);
    };
    animate();

    // Cursor hover effects using event delegation
    const handleMouseEnter = (e) => {
        const target = e.target.closest('a, button, .filter-btn, .gallery-item, .btn-back, .project-card');
        if (target) {
            if (follower) {
                follower.style.width = '80px';
                follower.style.height = '80px';
                follower.style.background = 'rgba(0, 71, 171, 0.05)';
                follower.style.borderColor = 'transparent';
            }
            if (cursor) {
                cursor.style.width = '12px';
                cursor.style.height = '12px';
            }
        }
    };

    const handleMouseLeave = (e) => {
        const target = e.target.closest('a, button, .filter-btn, .gallery-item, .btn-back, .project-card');
        if (target) {
            if (follower) {
                follower.style.width = '40px';
                follower.style.height = '40px';
                follower.style.background = 'transparent';
                follower.style.borderColor = 'var(--color-primary)';
            }
            if (cursor) {
                cursor.style.width = '8px';
                cursor.style.height = '8px';
            }
        }
    };

    document.addEventListener('mouseover', handleMouseEnter);
    document.addEventListener('mouseout', handleMouseLeave);

    // Hide cursor when leaving window
    document.addEventListener('mouseleave', () => {
        if (cursor) cursor.style.opacity = '0';
        if (follower) follower.style.opacity = '0';
    });

    document.addEventListener('mouseenter', () => {
        if (cursor) cursor.style.opacity = '1';
        if (follower) follower.style.opacity = '1';
    });

    // ===================================
    // Navbar Scroll Effect
    // ===================================
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar?.classList.add('scrolled');
        } else {
            navbar?.classList.remove('scrolled');
        }
    });

    // ===================================
    // Mobile Menu Toggle
    // ===================================
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    menuToggle?.addEventListener('click', () => {
        if (!navLinks) return;
        navLinks.classList.toggle('active');
        // Simple toggle for demonstration
        if (navLinks.classList.contains('active')) {
            navLinks.style.display = 'flex';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'fixed';
            navLinks.style.top = '70px';
            navLinks.style.left = '0';
            navLinks.style.width = '100%';
            navLinks.style.background = 'var(--color-bg)';
            navLinks.style.padding = '2rem';
        } else {
            navLinks.style.display = '';
        }
    });

    // ===================================
    // Project Animations (Optional)
    // ===================================
    const observerOptions = {
        threshold: 0.1
    };

    const projectObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    projectCards.forEach(card => projectObserver.observe(card));

    // ===================================
    // Scroll Reveal Animation
    // ===================================
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in-up, .project-card, .expertise-item').forEach(el => {
        el.classList.add('fade-in-up');
        observer.observe(el);
    });

    // ===================================
    // Smooth Scroll for Nav Items
    // ===================================
    document.querySelectorAll('.nav-item').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const offset = 80;
                const bodyRect = document.body.getBoundingClientRect().top;
                const elementRect = targetElement.getBoundingClientRect().top;
                const elementPosition = elementRect - bodyRect;
                const offsetPosition = elementPosition - offset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ===================================
    // Magnetic Buttons
    // ===================================
    const magneticBtns = document.querySelectorAll('.btn-main');
    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', function(e) {
            const position = this.getBoundingClientRect();
            const x = e.pageX - position.left - position.width / 2;
            const y = e.pageY - position.top - position.height / 2;

            this.style.transform = `translate(${x * 0.3}px, ${y * 0.5}px)`;
        });

        btn.addEventListener('mouseout', function() {
            this.style.transform = 'translate(0px, 0px)';
        });
    });

    // ===================================
    // Parallax Background Blobs
    // ===================================
    const blobs = document.querySelectorAll('.blob');
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        blobs.forEach((blob, index) => {
            const speed = (index + 1) * 0.2;
            blob.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });

    // ===================================
    // Loading State & Final Polish
    // ===================================
    window.addEventListener('load', () => {
        document.body.classList.remove('loading');
        document.body.classList.add('loaded');
        
        // Initial reveal for hero
        const heroElements = document.querySelectorAll('.hero-meta, .hero-title, .hero-subtitle, .hero-actions');
        heroElements.forEach((el, i) => {
            setTimeout(() => {
                el.classList.add('visible');
            }, i * 200);
        });
    });
});
