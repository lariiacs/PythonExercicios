import math
cat1 = float(input(('digite o velor do primeiro cateto: ')))
cat2 = float(input(('digite o velor do segundo cateto: ')))
hip = math.sqrt(pow(cat1,2)+pow(cat2,2))
print('o valor da hipotenusa é {}'.format(hip))