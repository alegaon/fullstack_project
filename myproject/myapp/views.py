from django.http import HttpResponse
import sqlite3

def index(request):
    return HttpResponse("<html>¡<strong>Hola</strong>, <em>mundo</em>!</html>")

def acerca_de(request):
    return HttpResponse("¡Curso de Python y Django!")

def cursos(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT cursos, inscriptos FROM tabla")
    html = """
        <html>
        <title>Lista de cursos</title>
        <table style="border: 1px solid">
            <thead>
                <tr>
                    <th>Curso</th>
                    <th>Inscriptos</th>
                </tr>
            </thead>
        """
    for (nombre, inscriptos) in cursor.fetchall():
            html += f"""
                <tr>
                    <td>{nombre}</td>
                    <td>{inscriptos}</td>
                </tr>
            """
    html += "</table></html>"
    conn.close()
    return HttpResponse(html)