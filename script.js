document.addEventListener('DOMContentLoaded', () => {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');

    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Create a smooth appearance effect on load for the title
    const title = document.querySelector('.hero-title');
    const subtitle = document.querySelector('.hero-subtitle');
    const buttons = document.querySelector('.hero-buttons');

    if (title) {
        title.style.opacity = '0';
        title.style.transform = 'translateY(20px)';
        setTimeout(() => {
            title.style.transition = 'all 1.2s cubic-bezier(0.2, 0.8, 0.2, 1)';
            title.style.opacity = '1';
            title.style.transform = 'translateY(0)';
        }, 300);
    }

    if (subtitle) {
        subtitle.style.opacity = '0';
        subtitle.style.transform = 'translateY(20px)';
        setTimeout(() => {
            subtitle.style.transition = 'all 1.2s cubic-bezier(0.2, 0.8, 0.2, 1)';
            subtitle.style.opacity = '1';
            subtitle.style.transform = 'translateY(0)';
        }, 100);
    }

    if (buttons) {
        buttons.style.opacity = '0';
        buttons.style.transform = 'translateY(20px)';
        setTimeout(() => {
            buttons.style.transition = 'all 1.2s cubic-bezier(0.2, 0.8, 0.2, 1)';
            buttons.style.opacity = '1';
            buttons.style.transform = 'translateY(0)';
        }, 500);
    }

    // Typewriter effect
    const words = ["Technology", "Strategy", "Execution"];
    let wordIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const typewriterElement = document.getElementById('typewriter-text');

    function type() {
        const currentWord = words[wordIndex];

        if (isDeleting) {
            typewriterElement.textContent = currentWord.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typewriterElement.textContent = currentWord.substring(0, charIndex + 1);
            charIndex++;
        }

        let typeSpeed = 100;

        if (isDeleting) {
            typeSpeed /= 2;
        }

        if (!isDeleting && charIndex === currentWord.length) {
            typeSpeed = 2000; // Pause at end
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            wordIndex = (wordIndex + 1) % words.length;
            typeSpeed = 500; // Pause before new word
        }

        setTimeout(type, typeSpeed);
    }

    if (typewriterElement) {
        setTimeout(type, 1000);
    }
});


// Navbar Dropdown Logic
document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("whatwedo-toggle");
    const menu = document.getElementById("whatwedo-menu");
    const close = document.getElementById("whatwedo-close");

    // Also handle submenu tabs inside What We Do
    const whatWeDoTabs = document.querySelectorAll(".whatwedo-tab");
    const whatWeDoPanels = document.querySelectorAll(".whatwedo-panel");
    if (whatWeDoTabs.length && whatWeDoPanels.length) {
        const setActive = (activeTab) => {
            whatWeDoTabs.forEach(t => {
                t.classList.remove("bg-slate-100", "dark:bg-slate-800", "text-primary");
                t.classList.add("text-slate-700", "dark:text-slate-200");
            });
            activeTab.classList.remove("text-slate-700", "dark:text-slate-200");
            activeTab.classList.add("bg-slate-100", "dark:bg-slate-800", "text-primary");

            whatWeDoPanels.forEach(p => p.classList.add("hidden"));
            const target = document.getElementById(activeTab.dataset.target);
            if (target) target.classList.remove("hidden");
        };

        // Initialize active state
        setActive(whatWeDoTabs[0]);

        whatWeDoTabs.forEach(link => {
            link.addEventListener("mouseenter", () => setActive(link));
            link.addEventListener("click", (e) => {
                e.preventDefault();
                setActive(link);
            });
        });
    }

    // Service Link Details Hover Logic
    const serviceLinks = document.querySelectorAll('.service-link');
    const detailTitle = document.getElementById('service-detail-title');
    const detailBody = document.getElementById('service-detail-body');

    const detailContent = {
        web: {
            title: 'Web Development',
            body: 'Modern, responsive web platforms built for speed, security, and scalability.'
        },
        android: {
            title: 'Android Application',
            body: 'Native and cross-platform Android apps focused on smooth UX and reliability.'
        },
        ios: {
            title: 'iOS App Development',
            body: 'Pixel-perfect iOS apps aligned with Apple design and performance standards.'
        },
        cloud: {
            title: 'Cloud Solution',
            body: 'Cloud-native architectures, deployment, and scaling on leading cloud providers.'
        },
        n8n: {
            title: 'N8N Automation',
            body: 'Workflow automation that connects your tools and removes manual busywork.'
        }
    };

    const setDetail = (key) => {
        if (!detailTitle || !detailBody) return;
        const content = detailContent[key];
        if (!content) return;
        detailTitle.textContent = content.title;
        detailBody.textContent = content.body;
    };

    if (serviceLinks.length) {
        const first = serviceLinks[0];
        const initialKey = first.getAttribute('data-service-detail');
        if (initialKey) setDetail(initialKey);

        serviceLinks.forEach(link => {
            const key = link.getAttribute('data-service-detail');
            if (!key) return;
            link.addEventListener('mouseenter', () => setDetail(key));
            link.addEventListener('focus', () => setDetail(key));
        });
    }

    const openMenu = () => {
        if (!menu) return;
        menu.classList.remove("invisible", "opacity-0", "translate-y-2", "pointer-events-none");
        menu.classList.add("opacity-100", "translate-y-0");
    };

    const closeMenu = () => {
        if (!menu) return;
        menu.classList.add("invisible", "opacity-0", "translate-y-2", "pointer-events-none");
        menu.classList.remove("opacity-100", "translate-y-0");
    };

    if (toggle && menu) {
        toggle.addEventListener("click", (e) => {
            e.stopPropagation();
            if (menu.classList.contains("invisible")) {
                openMenu();
            } else {
                closeMenu();
            }
        });
    }

    if (close) {
        close.addEventListener("click", (e) => {
            e.stopPropagation();
            closeMenu();
        });
    }

    document.addEventListener("click", (e) => {
        if (!menu || menu.classList.contains("invisible")) return;
        const withinMenu = menu.contains(e.target);
        const withinToggle = toggle && toggle.contains(e.target);
        if (!withinMenu && !withinToggle) {
            closeMenu();
        }
    });

    // Company Dropdown
    const companyToggle = document.getElementById("company-toggle");
    const companyMenu = document.getElementById("company-menu");

    const openCompanyMenu = () => {
        if (!companyMenu) return;
        closeMenu(); // close What We Do menu
        companyMenu.classList.remove("invisible", "opacity-0", "translate-y-2", "pointer-events-none");
        companyMenu.classList.add("opacity-100", "translate-y-0");
    };

    const closeCompanyMenu = () => {
        if (!companyMenu) return;
        companyMenu.classList.add("invisible", "opacity-0", "translate-y-2", "pointer-events-none");
        companyMenu.classList.remove("opacity-100", "translate-y-0");
    };

    if (companyToggle && companyMenu) {
        companyToggle.addEventListener("click", (e) => {
            e.stopPropagation();
            if (companyMenu.classList.contains("invisible")) {
                openCompanyMenu();
            } else {
                closeCompanyMenu();
            }
        });
    }

    document.addEventListener("click", (e) => {
        if (!companyMenu || companyMenu.classList.contains("invisible")) return;
        const withinMenu = companyMenu.contains(e.target);
        const withinToggle = companyToggle && companyToggle.contains(e.target);
        if (!withinMenu && !withinToggle) {
            closeCompanyMenu();
        }
    });

    // Also close company menu when opening What We Do
    if (toggle) {
        toggle.addEventListener("click", () => { closeCompanyMenu(); });
    }

    // Mobile Menu Toggle
    const mobileMenuButton = document.getElementById("mobile-menu-button");
    const mobileMenuClose = document.getElementById("mobile-menu-close");
    const mobileMenu = document.getElementById("mobile-menu");

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener("click", () => {
            mobileMenu.classList.remove("translate-x-full");
            document.body.style.overflow = "hidden"; // Prevent scrolling
        });
    }

    if (mobileMenuClose && mobileMenu) {
        mobileMenuClose.addEventListener("click", () => {
            mobileMenu.classList.add("translate-x-full");
            document.body.style.overflow = ""; // Restore scrolling
        });
    }

    // Close mobile menu on link click
    const mobileMenuLinks = mobileMenu?.querySelectorAll("a");
    mobileMenuLinks?.forEach(link => {
        link.addEventListener("click", () => {
            mobileMenu.classList.add("translate-x-full");
            document.body.style.overflow = "";
        });
    });
});
