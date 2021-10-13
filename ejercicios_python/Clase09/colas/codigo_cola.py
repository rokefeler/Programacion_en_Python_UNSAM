import random
from cola import Cola
#%%
nombres = ['angel', 'esteban', 'facundo', 'gabriel', 'maria', 'mora', 'romina', 'ruth', 'sofía', 'tomás']
random.shuffle(nombres)
#%%

cola_de_espera = Cola()

# llega el primero
cola_de_espera.encolar(nombres[0])
cola_de_espera.imprimir()
#%%
# llega el segundo
cola_de_espera.encolar(nombres[1])
cola_de_espera.imprimir()

print(f"¿Quién sigue?: {cola_de_espera.proximo()}")
#%%
# llega el tercero
cola_de_espera.encolar(nombres[2])
cola_de_espera.imprimir()

print(f"¿Quién sigue?: {cola_de_espera.proximo()}")

#%%
atender_a = cola_de_espera.desencolar()
print(f"Pasó {atender_a}")
cola_de_espera.imprimir()
#%%
atender_a = cola_de_espera.desencolar()
print(f"Pasó {atender_a}")
cola_de_espera.imprimir()
#%%
atender_a = cola_de_espera.desencolar()
print(f"Pasó {atender_a}")
cola_de_espera.imprimir()
