
"""
Package er annerledes fra en modul siden det er utrolig mye kode som noen andre har skrevet - mange mange filer

La oss si at vi ønsker å lage en tabell med pokemon og hva slags type de har. Tabellen kan være kjempe vanskelig å lage. Derfor kan vi like gjerne bruke
noe noen andre allerede har laget. 

Det kan vi finnes på pypi.org.


PrettyTable dokumentasjon: https://github.com/prettytable/prettytable
"""
import prettytable

table = prettytable.PrettyTable()

#Jeg vet at det legges inn slik pga dokumentasjonen jeg har lagt ved over
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

#Prøv å endre align fra center til left. Da må man endre attribute
table.align = "l"

print(table)