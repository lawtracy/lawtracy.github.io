// assets/js/main.js
// Main JavaScript file for the blog theme

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the dark mode toggle button
    const toggleButton = document.getElementById('dark-mode-toggle');
    
    // Check if dark mode toggle exists
    if (toggleButton) {
        // Check for saved theme preference or respect OS preference
        const savedTheme = localStorage.getItem('theme');
        const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
        
        // Set initial theme
        const currentTheme = savedTheme || (prefersDarkScheme.matches ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', currentTheme);
        updateToggleIcon(currentTheme);
        
        // Add event listener to the toggle button
        toggleButton.addEventListener('click', function() {
            // Get current theme
            const currentTheme = document.documentElement.getAttribute('data-theme');
            
            // Switch theme
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            // Apply new theme
            document.documentElement.setAttribute('data-theme', newTheme);
            
            // Save preference to localStorage
            localStorage.setItem('theme', newTheme);
            
            // Update toggle icon
            updateToggleIcon(newTheme);
        });
    }
    
    // Function to update toggle button icon based on theme
    function updateToggleIcon(theme) {
        const sunIcon = toggleButton.querySelector('.sun-icon');
        const moonIcon = toggleButton.querySelector('.moon-icon');
        
        if (theme === 'dark') {
            sunIcon.style.display = 'none';
            moonIcon.style.display = 'inline';
        } else {
            sunIcon.style.display = 'inline';
            moonIcon.style.display = 'none';
        }
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80, // Adjust for fixed header
                    behavior: 'smooth'
                });
            }
        });
    });
});