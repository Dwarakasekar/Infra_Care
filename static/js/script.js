document.addEventListener("DOMContentLoaded", function() {
    var toggle = document.getElementById("menu-toggle");
    var menuItems = document.querySelectorAll(".menu .item");

    toggle.addEventListener("click", function() {
        // Toggle the 'active' class on each menu item
        menuItems.forEach(function(item) {
            item.classList.toggle("active");
        });

        // Toggle the 'active' class on the toggle button itself to animate the hamburger icon
        toggle.classList.toggle("active");
    });
});
