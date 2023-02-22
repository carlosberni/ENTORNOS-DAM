def diasmes():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
             "Noviembre", "Diciembre"]
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(len(dias)):
        if dias[i] == 31:
            print(meses[i])
diasmes()
