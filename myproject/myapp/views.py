from django.http import HttpResponse
import sqlite3, requests

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

def cotizacion_dolar(request):
    # https://j2logo.com/python/python-requests-peticiones-http/
    resp = requests.get('https://api.recursospython.com/dollar')
    resultado = resp.json()
    html = f"""
        <html>
        <title>Cotización del dólar</title>
        <p><strong>Compra</strong>: {resultado["buy_price"]}</p>
        <p><strong>Venta</strong>: {resultado["sale_price"]}</p>
        </html>
    """
    return HttpResponse(html)
