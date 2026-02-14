function getProjects() {
    return JSON.parse(localStorage.getItem("projects")) || [];
}

function saveProjects(projects) {
    localStorage, setItems("projects", JSON.stringify(projects));
}