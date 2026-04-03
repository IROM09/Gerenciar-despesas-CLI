from cat import categoria
ob = categoria()
print("""
////////////////|////////////////
////////  Bem vindo ao  /////////
////  Gerenciador de gastos  ////
///                           ///""")
while True:
    act = int(input("""///                           ///
//// O que você quer fazer?  ////
/// 1 - Adicionar gasto       ///
/// 2 - Ver gastos            ///
/// 3 - Sair                  ///
///                           ///
   R: """))

    if act == 1:
        nome = str(input("""///                           ///
//// Digite o nome do produto ///
///                           ///
   R:"""))
        cat = int(input("""///                           ///
/////// Qual a categoria? ///////
/// 1 - Comida                ///
/// 2 - Higiene               ///
/// 3 - Casa                  ///
/// 4 - Lazer                 ///
/// 5 - Imprevisto            ///
///                           ///
   R:"""))
        des = str(input("""///                           ///
/////// Digite a descrição //////
////// ou motivo da compra //////
///                           ///
   R:"""))
        val = float(input("""///                           ///
///////// Digite o valor ////////
///                           ///
   R:"""))
        print("""///                           ///""")
        ob.atribuir(nome, cat, des, val)
    elif act == 2:
        ob.ler()
    elif act == 3:
        print("""///                           ///
////// Obrigado por usar o //////
////  Gerenciador de gastos  ////
////////////////|////////////////""")
        break
