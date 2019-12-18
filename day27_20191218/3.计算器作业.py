#! encoding:utf-8
import re

# -40/5
def calc_mul_div(express):
    if '/' in express:
        a, b = express.split('/')
        return float(a)/float(b)
    if '*' in express:
        a, b = express.split('*')
        return float(a)*float(b)
# (-40/5)
def calc_value_in_brackets(express):
    # 去除括号
    express = express.strip('()')
    # 先算乘除，后算加减 -40/-5 + 8*5
    ret = re.search('-?\d+[/*]-?\d+', express)
    if ret:
        express_mul_div = ret.group()
        value = calc_mul_div(express_mul_div)
        return value
    #calc_add_sub()

def main():
    express = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    # 去空格
    new_express = express.replace(' ','')
    # 提取括号里没有其他括号的表达式，最小括号
    ret = re.search('\([^()]+\)', new_express)
    if ret:
        express_no_brackets = ret.group()
        # print(express_no_brackets)  # (-40/5)
        min_express = calc_value_in_brackets(express_no_brackets)
        # print(min_express) # -8.0
        new_express = new_express.replace(express_no_brackets, str(min_express))
        print(new_express)  # 1-2*((60-30+-8.0*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))


main()
