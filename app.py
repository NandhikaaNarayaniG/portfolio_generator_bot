from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the chatbot interface
@app.route('/')
def index():
    return render_template('chatbot.html')

# Route to handle chatbot responses and create portfolio
@app.route('/generate', methods=['POST'])
def generate_portfolio():
    name = request.form.get('name')
    job_title = request.form.get('job_title')
    summary = request.form.get('summary')
    skills = request.form.get('skills').split(",")  # Split comma-separated skills
    projects = request.form.getlist('projects[]')  # Get list of projects
    project_links = request.form.getlist('project_links[]')  # Get list of project links
    achievements = request.form.get('achievements').split(",")  # Split achievements
    education = request.form.get('education')

    # Create a dictionary of projects and their corresponding links
    projects_links = {project.strip(): link.strip() for project, link in zip(projects, project_links)}

    return render_template('portfolio.html', name=name, job_title=job_title, summary=summary, skills=skills, projects_links=projects_links, achievements=achievements, education=education)

    


if __name__ == "__main__":
    app.run(debug=True)
