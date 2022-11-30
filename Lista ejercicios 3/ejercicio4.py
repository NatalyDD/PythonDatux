def problibreria():
    import os
    a=os.getcwd()
    b=os.listdir()
    c=os.path.exists("Principal.py")
    print("El directorio actual: ",a)
    print("Las carpetas que hay en el directorio: ",b)
    print("Comprobar si el archivo 'Principal.py' existe: ",c)

