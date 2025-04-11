document.addEventListener('DOMContentLoaded', () => {
    const themeSwitch = document.getElementById('checkbox');
    const currentYearSpan = document.getElementById('current-year');

    // --- Theme Switching ---

    // Function to set the theme
    const setTheme = (isDarkMode) => {
        if (isDarkMode) {
            document.body.classList.remove('light-mode');
            document.body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            themeSwitch.checked = true; // Sync checkbox state
        } else {
            document.body.classList.remove('dark-mode');
            document.body.classList.add('light-mode');
            localStorage.setItem('theme', 'light');
            themeSwitch.checked = false; // Sync checkbox state
        }
    };

    // Check local storage for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    // Default to dark mode if no preference or system preference is dark
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme) {
        setTheme(savedTheme === 'dark');
    } else {
        // If no saved theme, respect system preference, otherwise default to dark
        setTheme(prefersDark); // Defaulting to dark if no preference
        // Or uncomment below to default to light if system preference isn't dark
        // setTheme(prefersDark);
    }


    // Add event listener for the theme switch
    themeSwitch.addEventListener('change', () => {
        setTheme(themeSwitch.checked);
    });

    // Listen for changes in system theme preference
     window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        // Only change if no theme explicitly saved by user
        if (!localStorage.getItem('theme')) {
             setTheme(e.matches);
        }
    });


    // --- Scroll Animations ---

    const observerOptions = {
        root: null, // relative to document viewport
        rootMargin: '0px',
        threshold: 0.1 // trigger when 10% of the element is visible
    };

    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Unobserve after animation to save resources
                // observer.unobserve(entry.target);
            }
            // Optional: Remove class if element scrolls out of view (for re-animation)
            // else {
            //     entry.target.classList.remove('visible');
            // }
        });
    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);

    // Observe all elements with the 'section' class (which includes slide-in/fade-in elements based on CSS)
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        observer.observe(section);
    });

    // Also observe elements specifically marked for fade-in if they aren't sections
    const fadeIns = document.querySelectorAll('.fade-in:not(.section)'); // Avoid observing sections twice
     fadeIns.forEach(el => {
        observer.observe(el);
    });


    // --- Dynamic Content ---

    // Set current year in footer
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

});