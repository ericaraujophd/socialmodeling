# Social Computing Course Website

Welcome to the **Agent-Based Modeling & Social Theory** course (HNRS-251-A), part of the Honors program at Calvin University. This repository hosts the course website, which serves as the central hub for all course materials, including the syllabus, schedule, and assignments.

---

## Course Overview

This course explores agent-based modeling (ABM) as a tool for understanding social phenomena. Students will engage in hands-on projects, applying computational methods to analyze and simulate social systems. The course is structured into modules, each focusing on a specific topic, such as segregation, contagion, cooperation, and polarization.

---

## Repository Structure

- **`intro.md`**: Introduction to the course, including its goals and philosophical underpinnings.
- **`organization.md`**: Details about the course structure, including modules, class schedule, and important dates.
- **`policies.md`**: Course policies, grading rubric, and expectations.
- **`myst.yml`**: Configuration file for the MyST Markdown-based website.
- **`requirements.txt`**: Python dependencies for running the course notebooks and building the site.
- **`imgs/`**: Directory containing images used in the course materials.

---

## Website Workflow

This repository uses [MyST Markdown](https://mystmd.org/) to build the course website. The site is hosted on GitHub Pages and is automatically updated with each push to the `main` branch.

### Local Development

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Build the Site**:

   ```bash
   myst build --html
   ```

3. **Preview the Site**:

   Start a local server to preview the site:

   ```bash
   myst start
   ```

   Open your browser and navigate to the URL provided by the `myst start` command (usually `http://localhost:3000`).

---

## Authors

- **Eric Araújo** (<eric.araujo@calvin.edu>)
- **Jonathan Hill** (<jonathan.hill@calvin.edu>)

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.
