videojuegos = []

plataformas = ( "PC", "PS5", "Xbox Series X", "Nintendo Switch" )

while True:
    print( "\n--- MENÚ DE VIDEO ---" )
    print( "1) Registrar videojuego." )
    print( "2) Ver videojuegos." )
    print( "3) Modificar videjuegos." )
    print( "4) Eliminar videojuego." )
    print( "5) Salir." )

    opcion = input( "Selcciones una opción (1-5): " )

    if opcion == "1":
        codigo = int( input( "Ingrese el codigo del videojuego: " ) )
        nombre = input( "Ingrese el nombre del videojuego: " )
        genero = input( "Ingrese el género del videojuego: " )

        print( "\nPlataformas disponibles: " )
        print( "1) PC" )
        print( "2) PS5" )
        print( "3) Xbox Series X" )
        print( "4) Nintendo Switch" )

        plataforma_codigo = int( input( "Seleccione el número de la plataforma: " ) )
        plataforma = plataformas[plataforma_codigo - 1]

        videojuego = {
            "codigo": codigo,
            "nombre": nombre,
            "genero": genero,
            "plataforma": plataforma
        }

        videojuegos.append( videojuego )
        print( "Videojuego registrado correctamente." )

    elif opcion == "2":
        if len( videojuegos ) == 0:
            print( "No hay videojuegos registrados." )

        else:
            print( "\n--- LISTA DE VIDEOJUEGOS ---" )

            for v in videojuegos:
                print( f"Código: {v[ 'codigo' ]}, Nombre: {v['nombre']}, Género: {v[ 'genero' ]}, Plataforma: {v[ 'plataforma' ]}" )

    elif opcion == "3":
        codigo = int( input( "Ingrese el código del videojuego a modificar: " ) )
        encontrado = False

        for v in videojuegos:
            if v[ "codigo" ] == codigo:
                v[ "nombre" ] = input( "Nuevo nombre: " )
                v[ "genero" ] = input( "Nuevo género: " )

            print( "\nPlataformas disponibles: " )
            print( "1) PC" )
            print( "2) PS5" )
            print( "3) Xbox Series X" )
            print( "4) Nintendo Switch" )

            plataforma_codigo = int( input( "Sleccione el número de la nueva plataforma: " ) )
            v[ "plataforma" ] = plataformas[plataforma_codigo - 1]

            print( "Videojuego modificado correctamente." )
            encontrado = True
            break

        if not encontrado:
            print( "vVideojuego no encontrado." )

    elif opcion == "4":
        pass

    elif opcion == "5":
        print( "Saliendo del programa." )
        break

    else:
        print( "Opción inválida." )

