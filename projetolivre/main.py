from package.maths import circle, point, reta, retangulo, triangulo

def main():
    while True:
        print('Bem vindo, usuário (a)!')
        print('Este é um programa que pode ser utilizado para a criação de algumas figuras geométricas.')
        print('A seguir, escolha qual figura deseja criar.')
        print('Lembre-se que o programa possui como medida padrão o centímetro.\n')

        print('Para criar figuras unidimensionais, digite o número 1.')
        print('Para criar figuras bidimensionais, digite o número 2.')
        print('Caso deseje sair do programa, digite o número 3.')
        option = int(input())

        if option == 1:
            while True:
                print('Figuras unidimensionais:')
                print('Para criar um ponto, digite o número 1.')
                print('Para criar uma reta, digite o número 2.')
                print('Para voltar, digite o número 3.')
                option_01 = int(input())

                if option_01 == 1:
                    while True:
                        print('\nPara criar um ponto, escolha os valores das coordenadas x e y respectivamente.')
                        coordenadas = input('Separe as coordenadas com a vírgula: ').split(',')
                        print('\n')
                        x = float(coordenadas[0])
                        y = float(coordenadas[1])

                        ponto_01 = point.Point(x,y)
                        ponto_01.modelo_ponto()

                        while True:
                            print('Escolha as seguintes opções:')
                            print('Para calcular a distância entre o ponto e a origem, digite o número 1')
                            print('Para voltar, digite o número 2')

                            option_01_01 = int(input())

                            if option_01_01 == 1:
                                print(f'\n A distância entre o ponto ({x},{y}) e a orígem é:{ponto_01.distancia_origem()} cm.')

                            elif option_01_01 == 2:
                                break
                            else:
                                print('Erro')
                                print('Valor incorreto.')
                        break

                elif option_01 == 2:
                    while True:
                        print('\nPara criar uma reta, digite os valores das coordenadas do ponto inicial e do ponto final da reta.')
                        print('Primeiro, digite o ponto inicial (escolha os valores das coordenadas x e y respectivamente):')
                        coordenadas_01 = input('Separe as coordenadas com a vírgula: ').split(',')
                        x = float(coordenadas_01[0])
                        y = float(coordenadas_01[1])

                        print('\nAgora, digite o ponto final(escolha os valores das coordenadas x e y respectivamente):')
                        coordenadas_02 = input('Separe as coordenadas com a vírgula:').split(',')
                        x1 = float(coordenadas_02[0])
                        y1 = float(coordenadas_02[1])

                        reta_01 = reta.Reta(x,y,x1,y1)
                        print(f'\nSeu modelo de reta tem como início o ponto ({x},{y}) e tem como fim o ponto ({x1},{y1}).')
                        
                        while True:
                            print('\nEscolha as seguintes opções:')
                            print('Para calcular o comprimento da reta, digite o número 1.')
                            print('Para calcular a distância entre a reta e a origem, digite o número 2.')
                            print('Para voltar, digite o número 3.')
                            
                            option_01_02 = int(input())

                            if option_01_02 == 1:
                                print(f'\nO comprimento da reta é: {reta_01.tamanho()} cm.')

                            elif option_01_02 == 2:
                                print(f'\nA distância entre a reta e a orígem é: {reta_01.distancia_origem()} cm.')

                            elif option_01_02 == 3:
                                break
                            
                            else:
                                print('Erro')
                                print('Valor incorreto.')
                        break
                    
                elif option_01 == 3:
                    break

                                      
        elif option == 2:
            while True:
                print('\nFiguras bidimensionais:')
                print('Para criar um retângulo, digite o número 1.')
                print('Para criar um círculo, digite o número 2.')
                print('Para criar um triângulo, digite o número 3.')
                print('Caso deseje voltar digite, o número 4.')
                option_02 = int(input())

                if option_02 == 1:
                  while True:
                    print('\nPara criar um retângulo, digite seu ponto central e suas medidas de base e altura.')
                    print('Primeiro, digite as coordenadas x e y do ponto central respectivamente.')
                    coordenadas = input('Separe as coordenadas com a vírgula: ').split(',')
                    x = float(coordenadas[0])
                    y = float(coordenadas[1])
                    print('\nDigite a medida da base.')
                    base = float(input())
                    print('\nDigite a medida da altura.')
                    height = float(input())

                    retangulo_01 = retangulo.Retangulo(x,y,base,height)
                    retangulo_01.modelo_retangulo()

                    while True:
                        print('\nEscolha as seguintes opções:')
                        print('Para calcular o perímetro do retângulo, digite o número 1.')
                        print('Para calcular a área do retângulo, digite o número 2.')
                        print('Para calcular a distância entre o ponto central do retângulo e a orígem, digite o número 3.')
                        print('Para voltar, digite o número 4.')
                        
                        option_02_01 = int(input())

                        if option_02_01 == 1:
                            print(f'\nO perímetro do retângulo é: {retangulo_01.perimetro()} cm.')

                        elif option_02_01 == 2:
                            print(f'\nA área do retângulo é: {retangulo_01.area()} cm.')

                        elif option_02_01 == 3:
                            print(f'\nA distância entre o ponto central e a orígem é: {retangulo_01.distancia_origem()} cm.')
                        
                        elif option_02_01 == 4:
                            break

                        else:
                            print('Erro')
                            print('Valor incorreto.')
                    break

                elif option_02 == 2:
                  while True:
                    print('\nPara criar um círculo, digite seu ponto central e seu raio.')
                    print('Primeiro, digite as coordenadas x e y,respectivamente, do seu ponto central.')
                    coordenadas = input('Separe as coordenadas com a vírgula: ').split(',')
                    x = float(coordenadas[0])
                    y = float(coordenadas[1])
                    print('\nAgora, digite o valor do raio do círculo.')
                    r = float(input())

                    circulo_01 = circle.Circle(x,y,r)
                    circulo_01.modelo_circulo()

                    while True:
                        print('\nEscolha entre as opções a seguir:')
                        print('Para calcular o perímetro do círculo, digite o número 1.')
                        print('Para calcular a área do círculo, digite o número 2.')
                        print('Para calcular a distância entre o centro do círculo e a orígem, digite o número 3.')
                        print('Para voltar, digite o número 4.')

                        option_02_02 = int(input())

                        if option_02_02 == 1:
                            print(f'\nO perímetro do círculo é: {circulo_01.perimetro()} cm.')

                        elif option_02_02 == 2:
                            print(f'\nA área do círculo é: {circulo_01.area()} cm.')

                        elif option_02_02 == 3:
                            print(f'\nA distância entre o centro do círculo e a orígem é: {circulo_01.distancia_origem()} cm.')

                        elif option_02_02 == 4:
                            break

                        else:
                            print('Erro')
                            print('Valor incorreto')

                    break

                elif option_02 == 3:
                  while True:
                    print('\nPara criar um triângulo, digite seu ponto central, sua base, sua altura e o tamanho de seus lados.')
                    print('Primeiro, digite as coordenadas x e y, respectivamente, do seu ponto central.')
                    coordenadas = input('Separe as coordenadas com a vírgula: ').split(',')
                    x = float(coordenadas[0])
                    y = float(coordenadas[1])
                    print('\nDigite o valor da base.')
                    base = float(input())
                    print('\nDigite o valor da altura.')
                    height = float(input())
                    print('\nDigite o valor do lado A.')
                    a = float(input())
                    print('\nDigite o valor do lado B.')
                    b = float(input())
                    print('\nDigite o valor do lado C.')
                    c = float(input())

                    triangulo_01 = triangulo.Triangulo(x,y,base,height,a,b,c)
                    existe = triangulo_01.triangulo()

                    if existe == True:
                        triangulo_01.modelo_triangulo()

                        while True:
                            print('\nEscolha entre as opções a seguir:')
                            print('Para saber qual é a classificação do triângulo, digite o número 1.')
                            print('Para calcular o perímetro do triângulo, digite o número 2.')
                            print('Para calcular a área do triângulo, digite o número 3.')
                            print('Para calcular a distância entre o centro da origem e o triângulo, digite o número 4.')
                            print('Para voltar, digite o número 5.')
                            option_02_03 = int(input())

                            if option_02_03 == 1:
                                print(f'\nO triângulo se classifica como {triangulo_01.tipo()}.')
                            
                            elif option_02_03 == 2:
                                print(f'\nO perímetro do triângulo é: {triangulo_01.perimetro()} cm.')

                            elif option_02_03 == 3:
                                print(f'\nA área do triângulo é: {triangulo_01.area()} cm.')
                            
                            elif option_02_03 == 4:
                                print(f'\nA distância entre o centro do triângulo e a orígem é: {triangulo_01.distancia_origem()} cm.')
                            
                            elif option_02_03 == 5:
                                break

                            else:
                                print('Erro')
                                print('Valor incorreto.')

                        break                        

                    else:
                        print('\nO triângulo com essas medidas não existe.')

                elif option_02 == 4:
                    break

                else:
                    print('Erro')
                    print('Valor incorreto.')

        elif option == 3:
            break

        else:
            print('Erro.')
            print('Valor incorreto.')
            
    
if __name__ == "__main__":
    main()
