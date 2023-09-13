from flask import Flask, render_template, request, url_for
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def student_information():
    return {'student_name': 'Angel Emmanuel García Venegas', 'field_of_study': 'Ingeniería de Software y Sistemas Computacionales'}

@app.context_processor
def social_media():
    return {'github_url': 'https://github.com/lokiangelmx', 'linkedin_url': 'https://linkedin.com/in/lokiangelmx'}

@app.context_processor
def date_now():
    return {
        'date': datetime.utcnow()
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    proyectos = [
        {
            'nombre': 'To Do List',
            'descripcion': 'Aplicación de lista de tareas por hacer hecho en Angular',
            'url': 'https://github.com/LokiAngelMx/ToDo-List'
        },
        {
            'nombre': 'Recipe Book',
            'descripcion': 'Aplicación de recetas de cocina hecho en Angular y Firebase con inteligencia artificial',
            'url': 'https://github.com/LokiAngelMx/POA/tree/main/Angular/Recipe'
        },
        {
            'nombre': 'Trivia',
            'descripcion': 'Aplicación de preguntas y respuestas hecho en Angular y Firebase',
            'url': 'https://github.com/LokiAngelMx/POA/tree/main/Angular/trivia'
        }
    ]
    return render_template('projects.html', projects = proyectos)

@app.route('/extra')
def extra():
    lenguajes = [
        {'id': 1, 'nombre': 'HTML', 'utilidad': 'Estructura de páginas web'},
        {'id': 2, 'nombre': 'CSS', 'utilidad': 'Estilos en páginas web'},
        {'id': 3, 'nombre': 'JavaScript', 'utilidad': 'Interactividad en páginas web'},
        {'id': 4, 'nombre': 'Vue.js', 'utilidad': 'Desarrollo de aplicaciones frontend'},
        {'id': 5, 'nombre': 'React', 'utilidad': 'Desarrollo de interfaces de usuario'},
        {'id': 6, 'nombre': 'Angular', 'utilidad': 'Desarrollo de aplicaciones web'},
        {'id': 7, 'nombre': 'Python', 'utilidad': 'Desarrollo general, ciencia de datos, web'},
        {'id': 8, 'nombre': 'Java', 'utilidad': 'Desarrollo de aplicaciones empresariales'},
        {'id': 9, 'nombre': 'C#', 'utilidad': 'Desarrollo de aplicaciones de Windows'},
        {'id': 10, 'nombre': 'Ruby', 'utilidad': 'Desarrollo web y scripting'},
        {'id': 11, 'nombre': 'PHP', 'utilidad': 'Desarrollo de aplicaciones web'},
        {'id': 12, 'nombre': 'SQL', 'utilidad': 'Gestión de bases de datos'},
        {'id': 13, 'nombre': 'Swift', 'utilidad': 'Desarrollo de aplicaciones iOS'},
        {'id': 14, 'nombre': 'Kotlin', 'utilidad': 'Desarrollo de aplicaciones Android'},
        {'id': 15, 'nombre': 'C++', 'utilidad': 'Desarrollo de software de sistema'},
        {'id': 16, 'nombre': 'TypeScript', 'utilidad': 'JavaScript con tipos estáticos'},
        {'id': 17, 'nombre': 'Go', 'utilidad': 'Desarrollo de sistemas y aplicaciones web'},
        {'id': 18, 'nombre': 'Rust', 'utilidad': 'Desarrollo de software de sistema seguro'},
        {'id': 19, 'nombre': 'Shell Scripting', 'utilidad': 'Automatización y tareas de sistema'},
        {'id': 20, 'nombre': 'Scala', 'utilidad': 'Desarrollo de aplicaciones empresariales'}
    ]
    return render_template('extra.html', lenguajes = lenguajes)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)