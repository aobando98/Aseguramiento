global meses31
meses31 = [1, 3, 5, 7, 8, 10, 12]

##Validaciones
def esInt(numero):
    """
    Entrada: Int
    Salida: Boolean
    Funcionamiento: Retorna True si el parametro es un int
    """
    if(isinstance(numero, int)):
        return True
    return False

def esTupla(tupla):
    """
    Entrada: Tupla
    Salida: Boolean
    Funcionamiento: Retorna True si el parametro es una tupla
    """
    if(isinstance(tupla, tuple)):
        return True
    return False

"""
R0 (fecha_es_tupla): Todas las fechas serán creadas como tuplas de tres números enteros
positivos (ternas),  en este orden: (año,  mes,  día). El resultado debe ser un valor booleano, 
True o False.
"""
def fecha_es_tupla(tupla):
    """
    Entrada: Tupla de largo 3 (año, mes, día)
    Salida: Boolean
    Funcionamiento: Retorna True si la tupla es una fecha válida
    """
    if(not esTupla(tupla)):
        return False
    elif(len(tupla != 3)):
        return False
    elif(tupla[0] < 1 and tupla[1] < 1 and tupla[2] < 1):
        return False
    else:
        return True
"""
R1 (bisiesto): Dado un año perteneciente al rango permitido,  determinar si este es bisiesto. El
resultado debe ser un valor booleano,  True o False.
"""
def bisiesto(year):
    """
    Entrada: Int
    Salida: Boolean
    Funcionamiento: Retorna True si el año insertado es un año bisiesto
    """
    if(esInt(year)):
        return (((year % 4) == 0) or ((year % 100) != 0 and (year % 400)  == 0))
    print("Error: Año debe ser un int.")
    return False
"""
R2 (fecha_es_valida): Dada una fecha,  determinar si ésta es válida. El resultado debe ser un
valor booleano,  True o False.
"""
def fecha_es_valida(tupla):
    """
    Entrada: Tupla de largo 3 (año, mes, día)
    Salida: Boolean
    Funcionamiento: Dada una fecha,  determinar si ésta es válida
    """
    if(not fecha_es_tupla(tupla)):
        return False
    else:
        year = tupla[0]
        month = tupla[1]
        day = tupla[2]
        
        if day == 31 and (month not in meses31):
            return False
        elif month > 12:
            return False
        elif month < 1 or month > 12 or day < 1 or day > 31:
            return False
        elif month == 2 and (not bisiesto(year)) and day > 28:
            return False
        elif month == 2 and bisiesto(year) and day > 29:
            return False
        else:
            return True

"""
R3 (dia_siguiente): Dada una fecha válida,  determinar la fecha del día siguiente. El resultado
debe ser una fecha válida (tupla de tres números enteros positivos,  que corresponde a una fecha
en el Calendario gregoriano).
"""
def dia_siguiente(tupla):
    """
    Entrada: Tupla de largo 3 (año, mes, día)
    Salida: Tupla de largo 3 (año, mes, día)
    Funcionamiento: Dada una fecha válida,  determinar la fecha del día siguiente
    """
    year = tupla[0]
    month = tupla[1]
    day = tupla[2]

    if day == 31:
        month+=1
        day = 1  
    elif day == 30 and (month not in meses31):
        month+=1
        day = 1
    elif month == 2 and bisiesto(year) and day == 29:
        month = 3
        day = 1
    elif month == 2 and (not bisiesto(year)) and day == 28:
        month = 3
        day = 1
    else:
        day+=1
        
    if month > 12:
        year+=1
        month = 1
        
    return (year,  month,  day)

"""
R4 (días_desde_primero_enero): Dada una fecha válida,  determinar el número de días
transcurridos desde el primero de enero de su año (dentro de un mismo año,  el número de días
transcurridos entre el primero de enero y el primero de enero,  es 0). El resultado debe ser un
número entero.
"""
def días_desde_primero_enero(tupla):
    """
    Entrada: Tupla de largo 3 (año, mes, día)
    Salida: Int
    Funcionamiento: Dada una fecha válida,  determinar el número de días transcurridos desde el primero de enero de su año
    """
    year = tupla[0]
    month = tupla[1]
    day = tupla[2]
    total = 0
    for i in range (1, month):
        if(i in meses31):
            total+=31
        elif(i == 2 and bisiesto(year)):
            total+=29
        elif(i == 2 and (not bisiesto(year))):
             total+=28
        else:
             total+=30
    total+=day-1
             
    return total

"""
R5 (dia_primero_enero): Dado un año perteneciente al rango permitido,  determinar el día de la
semana que le corresponde al primero de enero de ese año,  con la siguiente codificación: 0 =
domingo,  1 = lunes,  2 = martes,  3 = miércoles,  4 = jueves,  5 = viernes,  6 = sábado. El resultado
debe ser un número entero,  conforme a la codificación indicada.
"""
def dia_primero_enero(year):
    """
    Entrada: Int
    Salida: Int
    Funcionamiento:Dado un año perteneciente al rango permitido,  determinar el día de la
        semana que le corresponde al primero de enero de ese año,  con la siguiente codificación:
        0 = domingo,  1 = lunes,  2 = martes,  3 = miércoles,  4 = jueves,  5 = viernes,  6 = sábado.
        El resultado debe ser un número entero,  conforme a la codificación indicada.
    """
    if(year < 1800):
        return False
    elif(year < 1900):
        anchor = 5
    elif(year < 2000):
        anchor = 3
    elif(year < 2100):
        anchor = 2
    elif(year < 2200):
        anchor = 0
    else:
        return False

    #Inicia proceso de Doomsday Algorithm
    last2digits = year % 100
    var1 = last2digits // 12
    var2 = last2digits - (var1*12)
    var3 = var2 // 4
    var4 = var1 + var2 + var3 + anchor
    multiple = var4//7
    total = var4 - (7*multiple)

    #Se emieza a restar la cantidad de días desde el ultimo mes de febrero hasta el primero de enero
    if(bisiesto(year)):
        cant = (31+29)//7
        dia = 60 - (cant*7)
    else:
        cant = (31+28)//7
        dia = 59 - (cant*7)
    while(dia > 1):
        if(total > 0):
            total-=1
        else:
            total=6
        dia-=1
        
    return total
    

"""
R6 (imprimir_3x4): Dado un año perteneciente al rango permitido,  desplegar en consola el
calendario de ese año en formato de 3 secuencias (‘filas’) de 4 
"""

def imprimir_3x4(year):
    """
    Entrada: Int (año)
    Salida: -
    Funcionamiento:Dado un año perteneciente al rango permitido,  desplegar en consola el
            calendario de ese año en formato de 3 secuencias (‘filas’) de 4 
    """
    matrizAno = [
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ],
                [
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""],
                    ["", "", "", "", "", "", ""]
                ]
                ]
    print("Calendario del año " + str(year) + " D.C.")
    primeroEnero = dia_primero_enero(year)
    contador = 1
    month = 0
    diaSemana = primeroEnero
    while(month < 12):
        if((month+1) in meses31):
            numMax = 31
        elif(month == 1):
            if bisiesto(year):
                numMax = 29
            else:
                numMax = 28
        else:
            numMax = 30
        contadorSemana = 0
        for index in range(1, numMax+1):
            if(diaSemana > 6):
                diaSemana = 0
                contadorSemana += 1
            matrizAno[month][contadorSemana][diaSemana] = index
            diaSemana+=1
        month+=1

    dias = " Su Mo Tu We Th Fr Sa |"
    impresionMeses = ["        Enero         |       Febrero        |         Marzo        |         Abril        |", 
                      "         Mayo         |        Junio         |         Julio        |         Agosto       |", 
                      "      Setiembre       |       Octubre        |     Noviembre        |       Diciembre      |"]
    division = "| "
    for contador in range(0, 3): #3 lineas de meses
        print(impresionMeses[contador])
        print(dias*4)
        for semana in range (0, 6): #6 semanas por mes
            linea=" "
            for mes in range(0, 4): # 4 meses por fila
                for dia in range(0, 7): #7 dias por semana
                    if(matrizAno[(contador*4)+mes][semana][dia]==""):
                        linea+="   "
                    else:
                        if(matrizAno[(contador*4)+mes][semana][dia]//10>0):
                            linea+=str(matrizAno[(contador*4)+mes][semana][dia])+" "
                        else:
                            linea+=str(matrizAno[(contador*4)+mes][semana][dia])+"  "
                linea+=division
            print(linea)    

##Asignacion 3b
"""
R7 (fecha_futura): Dada una fecha válida f y un número entero no-negativo n,
determinar la fecha que está n días naturales en el futuro. El resultado debe ser una fecha válida.
"""
def fecha_futura (tupla, dias):
    """
    Entradas: Tupla (año,mes,dia), Int (dias)
    Salida: Tupla (año,mes,dia)
    Funcionamiento:Dado un año perteneciente al rango permitido, desplegar en consola el
            calendario de ese año en formato de 3 secuencias (‘filas’) de 4 
    """
    if(dias>=0):
        nuevaTupla = tupla
        for x in range(0,dias+1):
            nuevaTupla = dia_siguiente(nuevaTupla)
        return nuevaTupla
    else:
        print("Error: Cantidad de dias debe ser mayor o igual a 0")
        
def fecha_mayor(tupla1,tupla2):
    """
    Entrada: Tupla (año,mes,dia), Tupla (año,mes,dia)
    Salida: Tupla (año,mes,dia), Tupla (año,mes,dia) (En orden fecha mayor, fecha menor)
    Funcionamiento: Ordena las fechas dadas en las tuplas en orden descendente
    """
    year1 = tupla1[0]
    month1 = tupla1[1]
    day1 = tupla1[2]

    year2 = tupla2[0]
    month2 = tupla2[1]
    day2 = tupla2[2]

    if(year1==year2):
        if(month1==month2):
            if(day1==day2):
                return (tupla1,tupla2)
            elif(day1>day2):
                return (tupla1,tupla2)
            else:
                return (tupla2,tupla1)
        elif(month1>month2):
            return (tupla1,tupla2)
        else:
            return (tupla2,tupla1)
    elif(year1>year2):
        return (tupla1,tupla2)
    else:
        return (tupla2,tupla1)

"""
R8 (dias_entre): Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o f2 ≤ f1,
determinar el número de días naturales entre las dos fechas. Si f1 = f2,
entonces días_entre(f1, f2) = 0. El resultado debe ser un número entero no negativo.
"""
def dias_entre (tupla1, tupla2):
    """
    Entrada: Tupla (año,mes,dia), Tupla (año,mes,dia)
    Salida: Int (cantidad de dias entre las fechas)
    Funcionamiento: Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o f2 ≤ f1,
                    determinar el número de días naturales entre las dos fechas.
    """
    tuplaMayor,tuplaMenor = fecha_mayor(tupla1,tupla2)

    yearMayor = tuplaMayor[0]
    monthMayor = tuplaMayor[1]
    dayMayor = tuplaMayor[2]

    yearMenor = tuplaMenor[0]
    
    total = 0
    
    if(yearMayor>yearMenor):
        total+=días_desde_primero_enero(tuplaMayor)+1
        yearMayor-=1
        monthMayor = 12
        dayMayor = 31
        tuplaMayor=(yearMayor,monthMayor,dayMayor)
        while(yearMenor!=yearMayor):
            total+= días_desde_primero_enero(tuplaMayor)
            yearMayor-=1
            monthMayor = 12
            dayMayor = 31
            tuplaMayor=(yearMayor,monthMayor,dayMayor)
        return (días_desde_primero_enero(tuplaMayor)-días_desde_primero_enero(tuplaMenor))
    else:
        return(días_desde_primero_enero(tuplaMayor)-días_desde_primero_enero(tuplaMenor))

"""
R9 (dia_semana): Dada una fecha válida, determinar el día de la semana que le corresponde,
con la siguiente codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves,
5 = viernes, 6 = sábado. El resultado debe ser un número entero, conforme a la codificación indicada.
"""
def dia_semana (tupla):
    """
    Entrada: Tupla (año,mes,dia)
    Salida: Int (Dia de la semana)
    Funcionamiento:Dada una fecha válida, determinar el día de la semana que le corresponde,
                    con la codificación 
    """
    year = tupla[0]
    
    diaPrimeroEnero = dia_primero_enero(year)

    diasDesdePrimeroEnero = días_desde_primero_enero(tupla)

    dayShift = diasDesdePrimeroEnero%7

    return ((diaPrimeroEnero+dayShift)%7)

"""
R10 (dia_inicio_mes): Dado un año perteneciente al rango permitido y un mes en el rango válido
(1 ≤ mes ≤ 12), determinar el día de la semana que le corresponde al primer día de ese mes en
ese año, con la siguiente codificación: 0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles,
4 = jueves, 5 = viernes, 6 = sábado.
El resultado debe ser un número entero, conforme a la codificación indicada
"""
def dia_inicio_mes (year, month):
    """
    Entrada: Int (año), Int (mes)
    Salida: Int (Dia de la semana)
    Funcionamiento:Dado un año perteneciente al rango permitido y un mes en el rango válido
                    (1 ≤ mes ≤ 12), determinar el día de la semana que le corresponde al primer
                    día de ese mes en ese año
    """
    tupla = (year,month,1)
    return dia_semana(tupla)
