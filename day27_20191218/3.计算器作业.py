#! encoding:utf-8
import re


# 1-2*60-30+-72.0-3.33+172894.66+405.71--0.75-6.0
def deal_with_minus(express):
    express = express.replace('+-', '-')
    express = express.replace('--', '+')
    express = express.replace('-+', '-')
    express = express.replace('++', '+')
    return express

# -8 + -5
def calc_add_minus(express):
    express = deal_with_minus(express)
    num_list = re.findall(r'-?\d+\.?\d*', express)
    sum = 0
    for i in num_list:
        sum += float(i)
    return sum

# -40/5
def calc_mul_div(express):
    if '/' in express:
        a, b = express.split('/')
        return float(a) / float(b)
    if '*' in express:
        a, b = express.split('*')
        return float(a) * float(b)

# (-40/5)  1-2*-1386417.12
def calc_value_in_brackets(express):
    # 去除括号
    express = express.strip('()')
    # 先算乘除，后算加减 -40/-5 + 8*5 ; 9-2*5/3+7/3*99/4*2998+10*568/14
    while True:
        ret = re.search(r'\d+\.?\d*[/*]-?\d+\.?\d*', express)
        if ret:
            express_mul_div = ret.group()
            value = calc_mul_div(express_mul_div)
            express = express.replace(express_mul_div, str(value))
        else:
            break
    value = calc_add_minus(express)
    # 先计算express,求加减后，再返回
    return value


def main():
    express = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    # 去空格
    new_express = express.replace(' ','')
    while True:
    # 提取括号里没有其他括号的表达式，最小括号
        ret = re.search(r'\([^()]+\)', new_express)
        if ret:
            express_no_brackets = ret.group()
            min_express = calc_value_in_brackets(express_no_brackets)
            new_express = new_express.replace(express_no_brackets, str(min_express))
        else:
            break
    finally_value = calc_value_in_brackets(new_express)
    print(finally_value)
    print(eval(express))


main()


