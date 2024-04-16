def create_piramide(bricks_base):
    piramide = [bricks_base]

    while len(bricks_base) > 1:
        new_line = [sum(par) for par in zip(bricks_base, bricks_base[1:])]
        piramide.append(new_line)
        bricks_base = new_line

    return piramide

def impress_piramide(piramide):
    for line in reversed(piramide):
        print(' '.join(map(str, line)))

bricks_base = list(map(int, input("Digite os valores dos tijolos da base da pirâmide separados por espaço: ").split()))

piramide = create_piramide(bricks_base)
impress_piramide(piramide)