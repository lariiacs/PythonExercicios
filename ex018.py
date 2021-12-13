import math
grad = float(input('digite um ângulo em graus: '))
grad = math.radians(grad)
sen = math.sin(grad)
cos = math.cos(grad)
tan = math.tan(grad)
print('seno({:.3f})= {:.3f}'.format(grad,sen))
print('cosseno({:.3f})= {:.3f}'.format(grad,cos))
print('tangente({:.3f})= {:.3f}'.format(grad,tan))
