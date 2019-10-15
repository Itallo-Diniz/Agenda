agenda = {}

def adiciona_contato(dic,contato):
    a = contato.split()
    dic[a[0]] = a[1]

def exibe_contato(dic,nome):
    return dic[nome]

adiciona_contato(agenda,"Yude 40028922")
assert agenda == {"Yude":"40028922"}
assert(exibe_contato(agenda,"Yude") == "40028922")
