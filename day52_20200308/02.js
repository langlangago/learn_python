function f(a, b) {
    console.log("a:", a);
    console.log("b:", b);
    return a+b
}

var ret = f(11,22);
console.log("a+b=", ret);
console.log("=====================函数示例");

var foo = function (a, b) {
    console.log("a:", a);
    console.log("b:", b);
    return a+b
}

var ret2 = foo(11,22);
console.log("a+b=", ret2);
console.log("=====================匿名函数示例");

(function (a, b) {
    ret3 = a +b;
    console.log(ret3);
})(111, 222);
console.log("=====================立即执行函数示例");

function f(a, b) {
    console.log("a:", a);
    console.log("b:", b);
    return a+b
}

var ret = f(11,22,33);
console.log("a+b=", ret);
console.log("=====================函数多传参数，多的参数不用");

function f(a, b) {
    console.log("a:", a);
    console.log("b:", b);
    return a+b
}

var ret = f(11);
console.log("a+b=", ret);
console.log("=====================函数少传参数，11+undefined=NaN");

function f(a, b) {
    console.log("此函数有"+ arguments.length + "个参数");
    var ret = 0;
    for (var i=0;i<arguments.length;i++){
        ret += arguments[i];
    }
    return ret;
}

var ret = f(11,22,33);
console.log("参数和", ret);
console.log("=====================arguments示例,求参数累加的和");







