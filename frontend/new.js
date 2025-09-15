console.log("hello")
//like print
num=12;
str="ki";
bol=true;
bigint=32343454657;
nulll=null;
//var let const
var namee="saniya";
console.log(namee)
var namee="hhi";
console.log(namee)
let course="cse";
let age=12;
console.log(age)
age=21;
console.log(age);
function getname(name){
    return "welcome " + name ;

}
let getmsg=getname(namee);
console.log(getmsg)

//operators
let addage=age+4
let subage=age-2
let mulage=age*2
let divage=age/2 

console.log(addage)
console.log(subage)
console.log(mulage)
console.log(divage)

function area(len,wid){
    return len*wid;
s
}
let getarea=area(1,2);
console.log(getarea)

function fact(n){
    if(n==0){
        return 1;
    }
    else{
        return n*fact(n-1)
    }
}
let f=fact(4);
console.log(f)