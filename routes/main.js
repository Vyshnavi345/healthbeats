// Function to log user interactions
function logUserInteraction(eventType, eventData) {
    // Format the data to be logged
    const logEntry = {
        timestamp: new Date().toISOString(),
        eventType: eventType,
        eventData: eventData
    };

    // Send the log entry to a server for storage
    // Replace the URL with the endpoint where you want to send the data
    fetch('https://example.com/log', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(logEntry)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to log user interaction');
        }
    })
    .catch(error => {
        console.error('Error logging user interaction:', error);
    });
}

// Event listeners for user interactions
document.getElementById('playButton').addEventListener('click', function() {
    // Log the user clicking the play button
    logUserInteraction('play_song', { songId: '12345' });
});

document.getElementById('skipButton').addEventListener('click', function() {
    // Log the user clicking the skip button
    logUserInteraction('skip_song', { songId: '12345' });
});



