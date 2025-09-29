# Escritura de Archivo de Texto
# Se crea un nuevo archivo llamado my_notes.txt y se escriben notas personales en él

# Abre el archivo en modo escritura ('w'), esto creará el archivo si no existe
with open('my_notes.txt', 'w') as file:
    # Escribe tres líneas de notas personales en el archivo
    file.write("Esta es una nota personal sobre mis objetivos.\n")
    file.write("Recuerde practicar Python todos los días.\n")
    file.write("No olvidar hacer ejercicio regularmente.\n")

# Lectura de Archivo de Texto
# Abre el archivo my_notes.txt en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Lee el contenido del archivo línea por línea
    for line in file:
        # Muestra en la consola cada línea leída
        print(line.strip())  # strip() elimina los espacios en blanco al inicio y al final

# No es necesario cerrar el archivo manualmente cuando se usa 'with', se cierra automáticamente
