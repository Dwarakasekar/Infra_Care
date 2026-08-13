document.getElementById("create-project-form").addEventListener("submit", function (event) {
    event.preventDefault();
  
    // Calculate a basic sustainability score based on form inputs
    const materials = document.getElementById("materials").value;
    const energy = document.getElementById("energy").value;
    const proximityWater = document.getElementById("proximity-water").checked;
    const proximityForest = document.getElementById("proximity-forest").checked;
  
    let score = 50;
  
    // Increase score based on choices
    if (materials === "recycled-steel") score += 10;
    if (energy === "solar") score += 10;
    if (proximityWater) score -= 5;
    if (proximityForest) score -= 5;
  
    // Update the progress bar and text
    document.getElementById("score-progress").value = score;
    document.getElementById("score-text").innerText = `${score}%`;
  });
  