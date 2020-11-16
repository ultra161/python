def my_print(**kwargs):
    kt = ""
    vt = ""
    for key, val in kwargs.items():
        vt = vt + val + " "
    print(kt)
    print(vt)
    return kwargs


my_print(Name="Николай", Surname="Донцов", Date="1980", City="Ростов-на-Дону",
         email="it@spas.sc", Phone="2950095")
