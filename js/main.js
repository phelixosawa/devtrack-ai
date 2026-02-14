document.addEventListener(
    "DOMContentLoaded", () => {

        const openFormBtn = document.getElementById("open-project-form");
        const formCard = document.getElementById("project-form-card");
        const projectForm = document.getElementById("project-form");
        const projectsContainer = document.getElementById("projects-container");

        if (openFormBtn) {
            openFormBtn.addEventListener("click", () => {
                formCard.style.display = formCard.style.display === "none" ? "block" : "none";
            });
        }

        if (projectForm) {
            projectForm.addEventListener("submit", (e) => {
                e.preventDefault();

                const name = document.getElementById("project-name").value;
                const description = document.getElementById("project-description").value;
                const status = document.getElementById("project-status").value;

                const projects = getProjects();

                const newProject = {
                    id: Date.now(),
                    name,
                    description,
                    status,
                    createdAt: new Date().toISOString()
                };

                projects.push(newProject);
                saveProjects(projects);

                projectForm.reset();
                renderProjects();
            });
        }

        function renderProjects() {
            if (!projectsContainer) return;

            const projects = getProjects();
            projectsContainer.innerHTML = "";

            projects.forEach(project => {
                const card = document.createElement("div");
                card.classList.add("project-card");

                card.innerHTML = `
                    <h3>${project.name}</h3>
                    <p>${project.description}</p>
                    <div class="project-status">${project.status}</div>
                `;

                projectsContainer.appendChild(card);
            });
        }

        renderProjects();

        // dashboard metrics update
        function updateDashboardStats() {

            const totalProjectsEl = document.getElementById("total-projects");
            const activeProjectsEl = document.getElementById("active-projects");

            if (!totalProjectsEl || !activeProjectsEl) return;

            const projects = getProjects();

            const totalProjects = projects.length;
            const activeProjects = projects.filter(p => p.status === "Active").length;

            totalProjectsEl.textContent = totalProjects;
            activeProjectsEl.textContent = activeProjects;
        }

        updateDashboardStats();
    });
