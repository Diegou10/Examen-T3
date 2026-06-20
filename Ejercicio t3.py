laberinto = [
    [ 1,  1,  1,  1,  0,  1,  1,  1,  1],
    [-2,  0,  0, -1,  0,  1,  0,  1,  0],
    [ 1,  1,  0,  1,  1,  1,  0,  1,  0],
    [ 0,  1,  0, -1,  0,  0,  0, -1,  0],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  0],
    [-1,  0,  0,  0,  0,  0,  0,  1,  1],
    [ 1,  1,  1,  1, -1,  1,  1,  1,  0],
    [ 1,  0,  0,  1,  0,  1,  0,  1,  0],
    [ 1,  1, -1,  1,  1,  1,  0,  1,  1]
]

def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def valido(lab, res, f, c, vidas):
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    if lab[f][c] == 0:
        return False
    if res[f][c] == 1:
        return False
        
    vidas_prox = vidas
    if lab[f][c] == -1:
        vidas_prox = vidas_prox - 1
    if lab[f][c] == -2:
        vidas_prox = vidas_prox - 2
    if vidas_prox <= 0:
        return False
        
    return True

def solulab(lab, res, f, c, vidas):
    vidas_act = vidas
    if lab[f][c] == -1:
        vidas_act = vidas_act - 1
    if lab[f][c] == -2:
        vidas_act = vidas_act - 2
    res[f][c] = 1
    imprime(res)

    if f == 0 and c == 0:
        return True
    for df, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if valido(lab, res, f + df, c + dc, vidas_act):
            if solulab(lab, res, f + df, c + dc, vidas_act):
                return True
    res[f][c] = 0
    return False

print("Laberinto Original:")
imprime(laberinto)

filas = len(laberinto)
cols = len(laberinto[0])

res = [[0] * cols for _ in range(filas)]
print("Mostrando avance paso a paso:")

if solulab(laberinto, res, 8, 0, 3):
    print("El raton salió del laberinto.")
    print("Matriz donde el raton acerto:")
    imprime(res)
else:
    print("El raton no logró salir.")