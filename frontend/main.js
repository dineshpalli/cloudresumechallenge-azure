document.addEventListener("DOMContentLoaded", (event) => {
    const functionApi = "http://localhost:7071/api/http_trigger_py"; // Azure Function App endpoint url
    getVisitCount(functionApi);
});

async function getVisitCount(apiUrl) {
    // Default count in case the fetch fails.
    let count = 42;
    
    try {
        // Use the Fetch API with proper error checking
        const response = await fetch(apiUrl);

        // Check if the response is OK (status 200-299)
        if (!response.ok) {
            console.error(`Network response was not ok: ${response.status} ${response.statusText}`);
            // Fallback message to the user
            const counterElement = document.getElementById("counter");
            if (counterElement) {
                counterElement.textContent = "Unable to load visitor count."; // Placeholder to indicate data couldn't be loaded
            }
            return; // Stop execution here if the call failed
        }

        // Parse the JSON. Throws an error if the JSON is malformed.
        const data = await response.json();
        
        // Check if the data returned has the `count` property
        if (typeof data.count === 'number') {
            count = data.count;
        } else {
            // Log a warning if the 'count' property is not valid to help with debugging API response issues.
            console.warn("API response does not contain a valid 'count' property.");
        }

        // Get the DOM element where the count is displayed
        const counterElement = document.getElementById("counter");
        if (!counterElement) {
            console.warn("No element with id 'counter' was found in the DOM.");
            return;
        }
        
        counterElement.textContent = count + " Visit(s)";
        console.log("Website successfully fetched and displayed the visitor count.");
        
    } catch (error) {
        // Catch any network or parsing errors
        console.error("An error occurred while fetching the visitor count:", error);

        // Fallback message or count
        const counterElement = document.getElementById("counter");
        if (counterElement) {
            counterElement.innerText = "Unable to load visitor count.";
        }
    }
}
