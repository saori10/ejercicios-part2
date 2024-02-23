months = {
    1 : "Enero",
    2 : "Febrero",
    3 : "Marzo",
    4 : "Abril",
    5 : "Mayo",
    6 : "Junio",
    7 : "Julio",
    8 : "Agosto",
    9 : "Septiembre",
    10 : "Octubre",
    11 : "Noviembre",
    12 : "Diciembre"
}

date= input("Ingrese una fecha (dd/mm/aaaa) : ")
date = date.split("/")

print(date[0], "de", months[int(date[1])], "de", date[2])