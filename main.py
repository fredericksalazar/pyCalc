
"""
Vamos a crear una primer version de la calculadora en python
en este caso, tomará los datos por terminal y ofrecerá las 
4 operaciones basicas
"""

from unittest import result


print("""Bienvenido a PyCalc la calculadora Básica de Python
         Version: 0.1
         Autor: Frederick Salazar
         ----------------------------------------------------""")

def operar(previo, actual, operacion):
    if operacion == '1':
       return sumar(previo, actual)
    
    if operacion == '2':
       return restar(previo, actual)
        
    if operacion == '3':
       return multiplicar(previo, actual)
        
    if operacion == '4':
       return dividir(previo, actual)

def sumar(previo, actual):
    return previo + actual

def restar(previo, actual):
    return previo - actual

def multiplicar(previo, actual):
    return previo * actual

def dividir(previo, actual):
    return previo / actual

def guardarHistorial(previo, actual, operacion, resultado):
    
    if operacion == '1':
        oper = '+'
        
    if operacion == '2':
        oper = '-'
    
    if operacion == '3':
        oper = '*'
    
    if operacion == '4':
        oper = '/'
        
    
    hist = str(previo)+' '+oper+' '+str(actual)+'='+str(resultado)
    historial.append(hist)



try:
    historial = []
    mas = True
    flag = 0
    resultado = 0
    resultado_prev = 0
    
    primer_numero = float(input("""Ingrese un valor numerico:"""))
    
    if primer_numero != None:
        
        while mas:
            operacion = input(""" Seleccione una operacion:
                              1 - Sumar
                              2 - restar
                              3 - Multiplicar
                              4 - Dividir
                              5 - ver Historial\n""")
            if operacion.isnumeric:
                
                if operacion == '5':
                    print(historial)
                else:
                    
                    if flag == 0:
                        segundo_numero = float(input("ingrese el segundo numero:\n"))
                    else:
                        segundo_numero = float(input("ingrese otro numero:\n"))
                    
                    if segundo_numero != None:
                        
                        if flag == 0:
                            resultado = operar(primer_numero, segundo_numero, operacion)
                        else:
                            resultado = operar(resultado_prev, segundo_numero, operacion)
                            
                        print('Resultado de la operacion: ', resultado)
                        
                        if flag == 0:
                            guardarHistorial(primer_numero, segundo_numero, operacion, resultado)
                        else:
                            guardarHistorial(resultado_prev, segundo_numero, operacion, resultado)
                        continuar = input("Desea realizar otra operación? Y / N ")
                        
                        if continuar == 'N' or continuar == 'n':
                            mas = False
                    flag = 1
                    resultado_prev = resultado
    else:
        print('No ingreso un numero')
        exit()
except:
    print('ocurrio un error')
    

