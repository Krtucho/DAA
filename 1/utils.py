# Metodo para calcular el tiempo de ejecucion de un algoritmo y dar formato a la salida en milisegundos, segundos y minutos



# def timeit(method):
#     import time
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         print(f"Time: {te-ts}")
#         return result
#     return timed