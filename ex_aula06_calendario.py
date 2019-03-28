# criar uma classe calendario que recebe em seu construtor dia mês e ano
# nessa classe precisa ter os metodos, que dia é hoje,dia de amanhã
# data semana que vem
# data mês que vêm e ano que vêm e que altere para a data do metodo solicitado



class Calendario():

    def __init__(self, dia_hoje, mes_hoje, ano_hoje):
        self.dia = dia_hoje
        self.mes = mes_hoje
        self.ano = ano_hoje

    def dia_hoje(self):
        print(f"data:{self.dia}/{self.mes:02d}/{self.ano}")

    def amanha(self):
        if self.mes == 2:
            if self.dia == 28:
                self.dia = self.dia-28
                self.mes += 1
        if self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10:
            if self.dia == 31:
                self.dia = self.dia-31
                self.mes += 1
        if self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11:
            if self.dia == 30:
                self.dia = self.dia-30
                self.mes += 1
        if self.mes == 12:
            if self.dia == 31:
                self.dia = self.dia-31
                self.mes = self.mes-11
                self.ano += 1
        print(f"data:{self.dia+1}/{self.mes}/{self.ano}")

    def semana_que_vem(self):
        if self.mes == 2:
            if self.dia > 21:
                self.dia = self.dia-28
                self.mes += 1
        if self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10 or self.mes == 12:
            if self.dia > 24:
                self.dia = self.dia-31
                self.mes += 1
        if self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11:
            if self.dia > 23:
                self.dia = self.dia-30
                self.mes += 1
        print(f"data:{self.dia+7}/{self.mes}/{self.ano}")

    def mes_que_vem(self):
        if self.mes == 12:
            self.ano += 1
            self.mes -= 12
        print(f"data:{self.dia}/{self.mes+1}/{self.ano}")

    def ano_que_vem(self):
        if self.mes == 12:
            self.ano += 1
            self.mes -= 11
            print(f"data:{self.dia}/{self.mes}/{self.ano}")
        print(f"data:{self.dia}/{self.mes}/{self.ano+1}")

    def imprime_data(self):
        data.dia_hoje()
        data.amanha()
        data.semana_que_vem()
        data.mes_que_vem()
        data.ano_que_vem()


data = Calendario(21, 3, 2019)

data.imprime_data()