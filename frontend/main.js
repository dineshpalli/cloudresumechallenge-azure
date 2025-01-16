export async function getVisitCount(apiUrl) {
    let count = 42;  // Default fallback count

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

// Run DOM-dependent code only if document exists (i.e., in browser)
if (typeof document !== 'undefined') {
    document.addEventListener("DOMContentLoaded", (event) => {
        const functionApiUrl = "https://getresumevisitorcounter.azurewebsites.net/api/http_trigger_py?code=tKgqHQitkjQJ9IGwsg76eTshQqndhnjXMjXGepJ1ThiBAzFumKYAng%3D%3D";
        
        // Always use the production API URL
        const apiUrl = functionApiUrl;
    
        getVisitCount(apiUrl);
    });
}
