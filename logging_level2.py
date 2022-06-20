import logging
import logging_level1


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')


flhandlr = logging.FileHandler(r'output/test2.log')
flhandlr.setFormatter(formatter)
flhandlr.setLevel(logging.DEBUG)


logger.addHandler(flhandlr)

# logging.basicConfig(filename = r'output/test2.log',level = logging.INFO,
#                     format = '%(levelname)s:%(name)s:%(message)s')

def add(x,y):
    return x+y

def sub(x,y):
    return x-y


def mul(x,y):
    return x*y

num1 = 10
num2 = 14

add_res = add(num1,num2)
logger.debug('add : {} + {} = {}'.format(num1,num2,add_res))

sub_res = sub(num1,num2)
logger.debug('sub : {} - {} = {}'.format(num1,num2,sub_res))

mul_res = mul(num1,num2)
logger.debug('mul : {} * {} = {}'.format(num1,num2,mul_res))
