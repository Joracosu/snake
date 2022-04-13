

def reinas(N, etapa=0, solucion = [], j=0):
    solucion = ([0] * N) if not solucion else solucion
    for i in range(1, N + 1):
        solucion[etapa] = i
        if es_prometedora(solucion, etapa):
            if etapa == N - 1:
                j = j + 1
                print('[ jugada',j,']:', solucion)
            else:
                j = reinas(N, etapa + 1, solucion, j)
        solucion[etapa] = 0
    return j

def es_prometedora(SOLUCION, etapa):
    for i in range(etapa + 1):
        if SOLUCION.count(SOLUCION[i]) > 1: return False
        for j in range(i + 1, etapa + 1):
            if abs(i-j) == abs(SOLUCION[i] - SOLUCION[j]): return False
    return True
