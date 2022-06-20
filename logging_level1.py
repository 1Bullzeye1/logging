import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')


flhandlr = logging.FileHandler(r'output/test1.log')
flhandlr.setFormatter(formatter)
flhandlr.setLevel(logging.ERROR)

logger.addHandler(flhandlr)


def add(x,y):
    return x+y

def sub(x,y):
    return x-y


def mul(x,y):
    return x*y

def div(x,y):
    try:
        result =  x/y
    except ZeroDivisionError:
        logger.exception('tried to divide by zero')
    else:
        return result


num1 = 10
num2 = 0

add_res = add(num1,num2)
logger.debug('add : {} + {} = {}'.format(num1,num2,add_res))

sub_res = sub(num1,num2)
logger.debug('sub : {} - {} = {}'.format(num1,num2,sub_res))

mul_res = mul(num1,num2)
logger.debug('mul : {} * {} = {}'.format(num1,num2,mul_res))

div_res = div(num1,num2)
logger.debug('div : {} / {} = {}'.format(num1,num2,div_res))

