from time import time
from copy import copy
from random import shuffle, randint, random


# numeros = [randint(0, 1000) for _ in range(500)]
numeros = [41, 564, 909, 252, 377, 904, 662, 125, 797, 793, 422, 895, 33, 214, 6, 597, 938, 375, 305, 15, 291, 629, 494, 560, 673, 421, 751, 661, 436, 366, 269, 627, 17, 321, 4, 402, 665, 519, 787, 744, 946, 748, 706, 294, 435, 96, 856, 897, 180, 89, 463, 691, 646, 232, 999, 412, 657, 759, 836, 502, 512, 430, 8, 246, 965, 740, 719, 11, 822, 47, 655, 243, 444, 576, 861, 199, 788, 567, 754, 969, 866, 726, 570, 130, 409, 950, 164, 238, 910, 415, 767, 550, 667, 140, 1000, 498, 527, 685, 563, 756, 841, 285, 327, 729, 12, 239, 135, 592, 812, 101, 480, 206, 55, 528, 843, 217, 762, 254, 819, 958, 983, 493, 717, 19, 40, 614, 204, 611, 490, 452, 235, 201, 35, 610, 418, 697, 381, 262, 2, 364, 505, 92, 439, 651, 29, 544, 798, 928, 362, 120, 178, 669, 967, 453, 956, 106, 846, 211, 52, 752, 972, 165, 581, 672, 414, 260, 356, 156, 37, 334, 668, 348, 750, 288, 467, 908, 200, 510, 184, 580, 834, 429, 283, 774, 163, 842, 974, 71, 94, 109, 65, 385, 712, 250, 442, 898, 805, 736, 591, 179, 69, 465, 778, 985, 162, 763, 32, 642, 926, 466, 365, 78, 699, 701, 643, 652, 219, 749, 462, 170, 724, 854, 378, 332, 746, 882, 358, 76, 394, 75, 328, 615, 27, 434, 514, 307, 619, 990, 390, 80, 583, 534, 159, 10, 306, 376, 110, 353, 894, 883, 681, 721, 423, 281, 641, 617, 770, 127, 22, 331, 917, 765, 929, 684, 979, 338, 693, 73, 934, 158, 386, 618, 986, 380, 186, 292, 604, 628, 314, 175, 397, 808, 874, 278, 973, 68, 137, 210, 682, 145, 220, 747, 0, 445, 944, 824, 323, 622, 784, 448, 477, 779, 431, 64, 853, 392, 758, 687, 951, 161, 795, 980, 839, 488, 279, 9, 354, 670, 189, 50, 988, 440, 737, 53, 554, 508, 901, 811, 587, 128, 257, 446, 777, 532, 265, 473, 913, 624, 370, 97, 258, 192, 382, 426, 455, 873, 339, 383, 469, 792, 1, 526, 270, 609, 561, 336, 347, 547, 372, 271, 676, 989, 960, 996, 77, 202, 955, 522, 413, 927, 277, 953, 108, 286, 887, 244, 122, 816, 521, 638, 495, 903, 86, 757, 16, 136, 848, 300, 571, 645, 3, 867, 160, 543, 621, 187, 333, 872, 799, 234, 599, 90, 801, 838, 791, 124, 537, 85, 708, 340, 352, 330, 182, 61, 700, 835, 197, 539, 341, 607, 298, 167, 146, 818, 316, 272, 25, 964, 739, 702, 148, 653, 817, 427, 794, 735, 342, 237, 57, 36, 144, 852, 930, 626, 63, 925, 320, 769, 553, 74, 337, 589, 143, 959, 832, 468, 329, 998, 892, 705, 714, 183, 982, 293, 424, 309, 948, 236, 419, 548, 398, 993, 921, 49, 997, 677, 102, 457, 34, 731, 303, 126, 245, 584, 216, 605, 230, 497, 636, 574, 768, 30, 585, 780, 359, 284, 157, 603, 639, 405]
# numeros = [i+1 for i in range(1000)]

n = len(numeros)


def gera_numeros(repetidos, inicio, termino, tamanho):
    retorno = []
    if repetidos:
        retorno = [randint(inicio, termino) for _ in range(tamanho)]
    else:
        while len(retorno) < tamanho:
            r = randint(inicio, termino)
            if r not in retorno:
                retorno.append(r)
    print(retorno)

    global n
    n = len(retorno)
    return retorno


def aleatorio():
    t = time()
    melhor = [2**1024]
    for z in range(20000):
        shuffle(numeros)
        i = randint(0, len(numeros))
        a = numeros[:i]
        b = numeros[i:]
        diff = abs(sum(a)-sum(b))
        if melhor[0] > diff:
            melhor = [diff, a, b, copy(numeros)]
        if diff == 0:
            print('Break in ', z)
            break
    print(melhor[3])
    print(sorted(melhor[1], reverse=True), end='')
    print(sorted(melhor[2], reverse=True))
    print(sum(melhor[1]), ' - ', sum(melhor[2]), ' (', melhor[0], ')')
    print('Término: ', time() - t, '\n')


def ordenacao_decrescente():
    t = time()
    numeros.sort(reverse=True)
    a = []
    b = []
    for n in numeros:
        if sum(a) < sum(b):
            a.append(n)
        else:
            b.append(n)
    print(numeros)
    print(a, end='')
    print(b)
    print(sum(a), ' - ', sum(b), ' (', abs(sum(a)-sum(b)), ')')
    print('Término: ', time() - t, '\n')


def karmarkar_karp():
    nums = copy(numeros)
    t = time()
    a = []
    b = []
    nums.sort(reverse=True)
    n = [i for i in nums]
    while len(n) > 1:
        n1 = n.pop(0)
        n2 = n.pop(0)
        n.append(abs(n1-n2))
        if round(random()) == 1:
            if len(nums) > 0:
                a.append(nums.pop(0))
            if len(nums) > 0:
                b.append(nums.pop(0))
        else:
            if len(nums) > 0:
                b.append(nums.pop(0))
            if len(nums) > 0:
                a.append(nums.pop(0))
    print(a, end='')
    print(b)
    print(sum(a), ' - ', sum(b), ' (', abs(sum(a)-sum(b)), ')')
    print(n)
    print('Término: ', time() - t, '\n')


# =====================================================================================================================
def progamacao_dinamica():
    t = time()
    soma = sum(numeros)
    print(soma)

    if soma % 2 != 0:
        print('Não é possível encontrar dois conjuntos com a mesma soma')
        return False

    part = [[True for _ in range(n + 1)] for _ in range(soma // 2 + 1)]

    for a in range(1, soma // 2 + 1):
        part[a][0] = False

    for i in range(1, soma // 2 + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
            if i >= numeros[j - 1]:
                part[i][j] = (part[i][j] or part[i - numeros[j - 1]][j - 1])

    # Encontra e printa os conjuntos
    conj = []
    linha = len(part)-1
    while sum(conj) != len(part)-1:
        conj.append(numeros[min_true(part[linha])])
        linha -= conj[-1]

    print(conj)
    print(sum(conj))
    conj2 = copy(numeros)
    for c in conj:
        conj2.remove(c)
    print(conj2)
    print(sum(conj2))
    print('\nTérmino: ', time() - t, '\n')
    return part[soma // 2][n]


def min_true(linha):
    for i in range(len(linha)):
        if linha[i]:
            return i-1
    return -1
# =====================================================================================================================


if __name__ == '__main__':
    numeros = gera_numeros(False, 0, 750, 200)
    print("\n##### Ordenação crescente #####")
    ordenacao_decrescente()
    print('\n##### Karmarkar Karp #####')
    karmarkar_karp()
    print('\n##### Aleatório #####')
    aleatorio()
    print('\n##### Programação dinâmica #####')
    progamacao_dinamica()
