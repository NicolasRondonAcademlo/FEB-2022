#x = 10
#if x > 5:
#    raise Exception(f"X no deberia ser mayor que 5, x fue {x}")

def dividir_numeros(a:int,b:int) -> int:
    try:
        result = a//b
    except ZeroDivisionError:
        return 0
    except TypeError:
        return "No se pueden dividir enteros con string"
    except Exception as e:
        return str(e)
    else:
        print("No hay excepciones")
    finally:
        print("Esto se ejecuta siempre")
    return result

result = dividir_numeros(10,2)

print(result)
