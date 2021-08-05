import re
texto = 'Hoy es 06/08/2020. Mañana será 07/08/2020.'
print(re.findall(r'\d+/\d+/\d+', texto))
# Reemplazá esas apariciones, cambiando el formato
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto))
