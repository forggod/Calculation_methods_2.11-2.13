import math

ex = int(input('Введите номер упражнения '))
if ex == 11:

    e = 0.5e-8


    def nonReduced(x):
        #                    ----
        #                    \        1
        #       f(x) =        ---  --------
        #                    /      k(k+x)
        #                    ----

        sum, avr, k = 0.0, 0.0, 1
        counter = 0
        while k:
            avr = 1 / (k * (k + x))
            sum += avr
            k += 1
            if avr < e:
                counter = k - 1
                k = 0
        return counter, sum - 1


    def onReduced(x):
        #                         ----
        #                         \          1
        #       f(x) =  (1-x)  *   ---  ------------
        #                         /      k(k+1)(k+x)
        #                         ----

        sum, avr, k = 0.0, 0.0, 1
        counter =0
        while k:
            avr = 1 / (k * (k + 1) * (k + x))
            sum += avr
            k += 1
            if avr < e:
                counter = k - 1
                k = 0
        return counter, (1-x)*sum

    x = 0.9
    print('X =', x)
    nred = nonReduced(x)
    print('Not reduced', 'N = ' + str(nred[0]), nred[1], sep='\n')
    red = onReduced(x)
    print('Reduced', 'N = ' + str(red[0]), red[1], sep='\n')
    print()
    x = 0.5
    print('X =', x)
    nred = nonReduced(x)
    print('Not reduced', 'N = ' + str(nred[0]), nred[1], sep='\n')
    red = onReduced(x)
    print('Reduced', 'N = ' + str(red[0]), red[1], sep='\n')


elif ex == 12:
    e = 3e-8


    def azulberry(x):

        #                    ----                          ----
        #                    \          1                  \           1
        #       f(x) =        ---  -----------    ----      ---   -----------
        #                    /     sqrt(k^3+x)             /      sqrt(k^3-x)
        #                    ----                          ----

        mejoberry, tintoberry, kible = 0.0, 0.0, 1
        counter = 0
        while kible:
            tintoberry = 1 / math.sqrt(kible ** 3 + x)
            mejoberry += tintoberry
            kible += 1
            if tintoberry < e:
                counter = kible - 1
                kible = 0
        return counter, mejoberry


    def triceratops(x):

        #                    ----
        #                    \     sqrt(k^3-x)-sqrt(k^3+x)
        #       f(x) =        ---  -----------------------
        #                    /          sqrt(k^6-x^2)
        #                    ----

        merlatops, raptor, spino = 0.0, 0.0, 1
        counter = 0
        while spino:
            raptor = (math.sqrt(spino ** 3 - x) - math.sqrt(spino ** 3 + x)) / math.sqrt(spino ** 6 - x ** 2)
            merlatops += raptor
            spino += 1
            if raptor < e:
                counter = spino - 1
                spino = 0
        return counter, merlatops


    print('X = 0.5')
    x = 0.5
    azul1 = azulberry(x)
    azul2 = azulberry((-1) * x)
    juice = azul1[1] - azul2[1]
    print('Not reduced', 'N = ' + str(azul1[0] + azul2[0]), juice, sep='\n')
    meat = triceratops(x)
    print('Reduced', 'N = ' + str(meat[0]), meat[1], sep='\n')
    print()
    print('X = 0.999999999')
    x = 0.999999999
    azul1 = azulberry(x)
    azul2 = azulberry((-1) * x)
    juice = azul1[1] - azul2[1]
    print('Not reduced', 'N = ' + str(azul1[0] + azul2[0]), juice, sep='\n')
    meat = triceratops(x)
    print('Reduced', 'N = ' + str(meat[0]), meat[1], sep='\n')


elif ex == 13:
    e = 0.5e-10


    def slope():
        #                    ----
        #                    \        1
        #       f(x) =        ---  -------
        #                    /      n^2+1
        #                    ----

        sum, avr, n = 0.0, 0.0, 1
        counter = 0
        while n:
            avr = 1 / (n ** 2 + 1)
            sum += avr
            n += 1
            if avr < e:
                counter = n - 1
                n = 0
        return counter, sum


    def salmon():
        #                                         ----
        #                   pi^2       pi^4       \          1
        #       f(x) =     ------  -  ------   +   ---   ----------
        #                    6          90        /      n^4(n^2+1)
        #                                         ----

        fish, avr, n = 0.0, 0.0, 1
        counter = 0
        while n:
            avr = 1 / (n ** 4 * (n ** 2 + 1))
            fish += avr
            n += 1
            if avr < e:
                counter = n
                n = 0
        return counter, fish


    file = slope()
    print('Not reduced', 'N = ' + str(file[0]), file[1], sep='\n')
    pi = math.pi
    fish = salmon()
    print('Reduced', 'N = ' + str(fish[0]), ((pi ** 2 / 6) - (pi ** 4 / 90) + fish[1]), sep='\n')

input()
