document.getElementById('toggleBtn').addEventListener('click', function() {
    var details = document.getElementById('details');
    if (details.style.display === "none") {
        details.style.display = "block";
        this.textContent = "Esconder Detalhes";
    } else {
        details.style.display = "none";
        this.textContent = "Mostrar Detalhes";
    }
});
