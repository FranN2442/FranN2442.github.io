def escribirHTML(nombre, contenido):

    with open("html/" + nombre + ".html", "w+") as html_file:
        html_file.write(contenido)
        print("HTML file created successfully")

    return True