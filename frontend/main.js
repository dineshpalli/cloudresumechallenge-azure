document.addEventListener("DOMContentLoaded", (event) => {
    const functionApiUrl = "https://getresumevisitorcounter.azurewebsites.net/api/http_trigger_py?code=tKgqHQitkjQJ9IGwsg76eTshQqndhnjXMjXGepJ1ThiBAzFumKYAng%3D%3D"; // THe actual function endpoint
    const localFunctionApi = "http://localhost:7071/api/http_trigger_py"; // For local testing

    // Use the production URL when deployed, fallback to local during development
    const apiUrl = window.location.hostname === "localhost" ? localFunctionApi : functionApiUrl;

    getVisitCount(apiUrl);
});

async function getVisitCount(apiUrl) {
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

// Helper function to update the DOM counter
function updateCounter(message) {
    const counterElement = document.getElementById("counter");
    if (counterElement) {
        counterElement.textContent = message;
    } else {
        console.warn("No element with id 'counter' was found in the DOM.");
    }
}
