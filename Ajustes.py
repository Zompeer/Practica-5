from Memoria import *
def primerAjuste(mem, arch):
    for nom, peso in arch:
        for i in range(mem.tam()):
            if mem.modificaMemoria(i, -peso):
                mem.guardar(i, [nom, peso])
                break


def mejorAjuste(mem, arch):
    for nom, peso in arch:
        mejor_ajuste = -1
        for i in range(mem.tam()):
            if mejor_ajuste==-1:
                if mem.memoria(i) >= peso:
                    mejor_ajuste = i
            else:
                if mem.memoria(i)-peso < mem.memoria(mejor_ajuste)-peso and mem.memoria(i)-peso >=0:
                    mejor_ajuste = i
        if mejor_ajuste!=-1:
            mem.modificaMemoria(mejor_ajuste, -peso)
            mem.guardar(mejor_ajuste, [nom, peso])


def peorAjuste(mem, arch):
    for nom, peso in arch:
        peor_ajuste = -1
        for i in range(mem.tam()):
            if peor_ajuste==-1:
                if mem.memoria(i) >= peso:
                    peor_ajuste = i
            else:
                if mem.memoria(i)-peso > mem.memoria(peor_ajuste)-peso and mem.memoria(i)-peso >=0:
                    peor_ajuste = i
        if peor_ajuste!=-1:
            mem.modificaMemoria(peor_ajuste, -peso)
            mem.guardar(peor_ajuste, [nom, peso])
            

def siguienteAjuste(mem, arch):
    siguiente = 0
    for nom, peso in arch:
        if siguiente == mem.tam()-1:
            siguiente = 0
        for i in range(siguiente, mem.tam(), 1):
            if mem.modificaMemoria(i, -peso):
                mem.guardar(i, [nom, peso])
                siguiente = i
                break
