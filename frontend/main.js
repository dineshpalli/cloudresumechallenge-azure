export async function getVisitCount(apiUrl) {
    let count = 42; // Default fallback count
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            console.error(`Network response was not ok: ${response.status} ${response.statusText}`);
            updateCounter("Unable to load visitor count.");
            return;
        }
        const data = await response.json();
        if (typeof data.count === 'number') {
            count = data.count;
        } else {
            console.warn("API response does not contain a valid 'count' property.");
        }
        updateCounter(`${count} Visit(s)`);
    } catch (error) {
        console.error("An error occurred while fetching the visitor count:", error);
        updateCounter("Unable to load visitor count.");
    }
}

export function updateCounter(message) {
    const counterElement = document.getElementById("counter");
    if (counterElement) {
        counterElement.textContent = message;
    } else {
        console.warn("No element with id 'counter' was found in the DOM.");
    }
}

export function toggleTheme() {
    const body = document.body;
    const icon = document.querySelector('.theme-toggle i');
    if (body.getAttribute('data-theme') === 'dark') {
        body.removeAttribute('data-theme');
        icon.className = 'fas fa-moon';
    } else {
        body.setAttribute('data-theme', 'dark');
        icon.className = 'fas fa-sun';
    }
}

// Define the language toggle function
function toggleLanguage() {
    const enContent = document.getElementById("content-en");
    const deContent = document.getElementById("content-de");
    const langButton = document.querySelector(".language-toggle");
    const langButtonText = document.getElementById("lang-button-text");

    if (enContent.style.display !== "none") {
        // Switch to German
        enContent.style.display = "none";
        deContent.style.display = "block";
        langButton.classList.remove("en");
        langButton.classList.add("de");
        langButtonText.textContent = "DE";
    } else {
        // Switch to English
        enContent.style.display = "block";
        deContent.style.display = "none";
        langButton.classList.remove("de");
        langButton.classList.add("en");
        langButtonText.textContent = "EN";
    }
}

// Function to trigger confetti
export function triggerConfetti() {
    confetti({
        particleCount: 300,
        spread: 200,
        origin: { y: 0.6 },
        colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff', '#800080', '#FF69B4'],
    });
}

function getCurrentLanguage() {
    // If the language toggle button has the class "de", treat that as German; otherwise, English
    const langButton = document.querySelector(".language-toggle");
    if (!langButton) return "en"; // fallback to English if no toggle found
    return langButton.classList.contains("de") ? "de" : "en";
}

// Function to display the pop-up message
export function showPopupMessage() {
    if (document.querySelector('.popup-message')) return;

    // Decide which text to display based on the current language
    const lang = getCurrentLanguage();

    // Localized messages
    const messages = {
        en: '🎉 Haha, you found my “do nothing” button! Don’t fret – click on <strong>Work Experience</strong> or <strong>Education</strong> to know more!',
        de: '🎉 Haha, Sie haben meinen „Nichtstun“-Taste entdeckt! Keine Sorge – klicke auf <strong>Berufserfahrung</strong> oder <strong>Ausbildung</strong>, um weitere Informationen zu erhalten!'
    };

    const popupMessage = messages[lang] || messages.en; // fallback to English if something goes wrong

    const popup = document.createElement('div');
    popup.classList.add('popup-message');
    popup.innerHTML = popupMessage;
    popup.style.position = 'fixed';
    popup.style.top = '0%';
    popup.style.left = '50%';
    popup.style.transform = 'translateX(-50%)';
    popup.style.backgroundColor = 'var(--card-bg)';
    popup.style.color = 'var(--text)';
    popup.style.padding = '1rem 1rem';
    popup.style.borderRadius = '10px';
    popup.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    popup.style.zIndex = '2000';
    popup.style.textAlign = 'center';

    document.body.appendChild(popup);

    setTimeout(() => {
        popup.remove();
    }, 4000);
}


// Initialize event listeners with dependency injection
export function initializeEventListeners({
    popupMessageFunction = showPopupMessage,
    confettiFunction = triggerConfetti,
} = {}) {
    const counterElement = document.getElementById('counter');
    if (counterElement) {
        counterElement.addEventListener('click', () => {
            popupMessageFunction();
            confettiFunction();
        });
    }
}

// Ensure DOM is fully loaded before adding event listeners
document.addEventListener('DOMContentLoaded', () => {
    const functionApiUrl = "https://getresumevisitorcounter.azurewebsites.net/api/http_trigger_py?code=tKgqHQitkjQJ9IGwsg76eTshQqndhnjXMjXGepJ1ThiBAzFumKYAng%3D%3D";
    getVisitCount(functionApiUrl);

    initializeEventListeners();

    const themeToggleButton = document.querySelector('.theme-toggle');
    const languageToggleButton = document.querySelector('.language-toggle');

    if (themeToggleButton) {
        themeToggleButton.addEventListener('click', toggleTheme);
    }
    if (languageToggleButton) {
        languageToggleButton.addEventListener('click', toggleLanguage);
    }
});
