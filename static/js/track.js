document.getElementById("projectForm").addEventListener("submit", function(event){
    event.preventDefault();

    const location = document.getElementById("location").value;
    const materials = document.getElementById("materials").value;
    const duration = document.getElementById("duration").value;
    const workers = document.getElementById("workers").value;
    const season = document.getElementById("season").value;

    const outputSection = document.getElementById("output");
    outputSection.style.display = "block";
    outputSection.innerHTML = `
        <h3>Project Details</h3>
        <p><strong>Location/Area:</strong> ${location}</p>
        <p><strong>Sustainable Materials:</strong> ${materials}</p>
        <p><strong>Duration:</strong> ${duration} weeks</p>
        <p><strong>Workers:</strong> ${workers}</p>
        <p><strong>Predicted Season:</strong> ${season}</p>
    `;
});
