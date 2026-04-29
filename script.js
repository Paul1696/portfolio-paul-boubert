document.addEventListener('DOMContentLoaded', () => {
    // Add js-ready class for animation fallback
    document.body.classList.add('js-ready');

    const cursor = document.querySelector('.cursor');
    const follower = document.querySelector('.cursor-follower');

    let mouseX = 0;
    let mouseY = 0;
    let cursorX = 0;
    let cursorY = 0;
    let followerX = 0;
    let followerY = 0;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        if (cursor) cursor.style.opacity = '1';
        if (follower) follower.style.opacity = '1';
    });

    const animate = () => {
        followerX += (mouseX - followerX) * 0.15;
        followerY += (mouseY - followerY) * 0.15;

        if (cursor) {
            cursor.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
        }
        if (follower) {
            follower.style.transform = `translate3d(${followerX}px, ${followerY}px, 0) translate(-50%, -50%)`;
        }
        requestAnimationFrame(animate);
    };
    animate();

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            if (navbar) navbar.classList.add('scrolled');
        } else {
            if (navbar) navbar.classList.remove('scrolled');
        }
    });

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            if (navLinks.classList.contains('active')) {
                navLinks.style.display = 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'fixed';
                navLinks.style.top = '70px';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.background = 'var(--color-bg)';
                navLinks.style.padding = '2rem';
                navLinks.style.zIndex = '1000';
            } else {
                navLinks.style.display = '';
            }
        });
    }

    // Scroll Reveal Animation (Intersection Observer)
    const scrollObserverOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, scrollObserverOptions);

    // Apply observer to elements
    document.querySelectorAll('.fade-in-up, .project-card, .category-block').forEach(el => {
        revealObserver.observe(el);
    });

    // Handle BFCache (Back-Forward Cache) to prevent blank page on "Back" button
    window.addEventListener('pageshow', (event) => {
        if (event.persisted) {
            document.querySelectorAll('.fade-in-up, .project-card, .category-block, .hero-meta, .hero-title, .hero-subtitle, .hero-actions').forEach(el => {
                el.classList.add('visible');
                el.style.opacity = '1';
                el.style.transform = 'none';
            });
        }
    });

    // Project Filtering Logic
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card[data-category="architecture"]');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach((card, index) => {
                const projectType = card.getAttribute('data-type');
                if (filterValue === 'all' || projectType === filterValue) {
                    card.classList.remove('hidden');
                    card.style.position = 'relative';
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.classList.add('visible');
                    }, index * 50);
                } else {
                    card.classList.add('hidden');
                    setTimeout(() => {
                        if (card.classList.contains('hidden')) {
                            card.style.display = 'none';
                        }
                    }, 600);
                }
            });
        });
    });

    // Page Entrance Animation (Hero)
    window.addEventListener('load', () => {
        document.body.classList.remove('loading');
        document.body.classList.add('loaded');
        const heroElements = document.querySelectorAll('.hero-meta, .hero-title, .hero-subtitle, .hero-actions');
        heroElements.forEach((el, i) => {
            setTimeout(() => {
                el.classList.add('visible');
            }, i * 200);
        });
    });
});