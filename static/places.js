document.addEventListener("DOMContentLoaded", function () {
    const placeBoxes = document.querySelectorAll(".place_box");
    const modal = document.getElementById("placeModal");
    const modalImg = document.getElementById("modalImg");
    const modalTitle = document.getElementById("modalTitle");
    const modalDescription = document.getElementById("modalDescription");
    const modalTicket = document.getElementById("modalTicket");
    const modalRating = document.getElementById("modalRating");
    const closeModal = document.querySelector(".close");

    placeBoxes.forEach(placeBox => {
        placeBox.addEventListener("click", function () {
            const imgSrc = this.querySelector("img").src;
            const title = this.querySelector("h2").textContent;
            const rating = this.querySelector("p").textContent;

            // Fetch the description and ticket price dynamically from Neo4j (replace with API call)
            const description = this.getAttribute("data-description");
            const ticket = this.getAttribute("data-ticket");

            modalImg.src = imgSrc;
            modalTitle.textContent = title;
            modalDescription.textContent = description || "No description available.";
            modalTicket.textContent = ticket ? `Ticket: ₹${ticket}` : "Free Entry";
            modalRating.textContent = rating;

            modal.style.display = "flex";
        });
    });

    closeModal.addEventListener("click", function () {
        modal.style.display = "none";
    });

    window.addEventListener("click", function (e) {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });
});
