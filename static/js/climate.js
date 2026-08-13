document.getElementById('climateForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form submission

    let location = document.getElementById('location').value; // Get the entered location
    let predictionBox = document.getElementById('weatherData'); // Box to show the result

    if (location.trim() === "") {
        predictionBox.textContent = "Please enter a valid construction site location.";
        return;
    }

    // Simulate fetching data
    predictionBox.textContent = `Fetching weather prediction for ${location}...`;

    setTimeout(() => {
        // Show the mocked prediction related to construction work
        predictionBox.textContent = `For the next week at ${location}, Monday and Tuesday will have clear skies, ideal for foundation work. Expect rain on Wednesday and Thursday, which may cause delays in concrete pouring and earthworks. Friday through Sunday will be partly cloudy, with no significant interruptions expected for site operations. Plan roof installations or exterior work on sunny days for optimal progress.`;
    }, 2000); // Simulate API call delay
});
