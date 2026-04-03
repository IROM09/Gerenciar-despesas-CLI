class categoria:
    def __init__(self):
        self.comida = {}
        self.higiene = {}
        self.casa = {}
        self.lazer = {}
        self.imprevisto = {}
    def atribuir(self, nome, cat, des, val):
        if  cat == 1:
            self.comida.update({nome:(des, val)})
        elif cat == 2:
            self.higiene.update({nome:(des, val)})
        elif cat == 3:
            self.casa.update({nome:(des, val)})
        elif cat == 4:
            self.lazer.update({nome:(des, val)})
        elif cat == 5:
            self.imprevisto.update({nome:(des, val)})
    def ler(self):
        if self.comida != {}:
            print("""///                           ///
///                           ///
////// Gastos de Comida ////////
///                           ///""")
            for nome, (des, val) in self.comida.items():
                print(f"""  {nome}: {des} - R$ {val:.2f}
///                           ///""")
        if self.higiene != {}:
            print("""///                           ///
///                           ///
////// Gastos de Higiene ////////
///                           ///""")
            for nome, (des, val) in self.higiene.items():
                print(f"""  {nome}: {des} - R$ {val:.2f}
///                           ///""")
        if self.casa != {}:
            print("""///                           ///
///                           ///
//////// Gastos de Casa /////////
///                           ///""")
            for nome, (des, val) in self.casa.items():
                print(f"""  {nome}: {des} - R$ {val:.2f}
///                           ///""")
        if self.lazer != {}:
            print("""///                           ///
///                           ///
//////// Gastos de Lazer ////////
///                           ///""")
            for nome, (des, val) in self.lazer.items():
                print(f"""  {nome}: {des} - R$ {val:.2f}
///                           ///""")
        if self.imprevisto != {}:
            print("""///                           ///
///                           ///
///// Gastos de Imprevisto //////
///                           ///""")
            for nome, (des, val) in self.imprevisto.items():
                print(f"""  {nome}: {des} - R$ {val:.2f}
///                           ///""")