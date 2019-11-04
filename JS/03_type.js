/*
원시 타입(primitive data type)
  - boolean
  - null
  - undefined
  - number
  - string
  - symbol (ES6+)

객체 타입(object)
  - object
*/

//number (typeof)
3
-5 
3.14
e-19
Infinity
123/0 // Infinity
NaN // 숫자가 아님(Not a number) -> type은 number.. 
0/0 // NaN

// string
let myName = '탁희'
myName = "탁\n희"
// `(backtick) : ES6+ 템플릿리터럴(문자열에 포함할 수 있다))
// string interpolations, 줄바꿈(개행)
myName = `탁

희` // enter 인식
console.log(`안녕하세요, ${myNAme}입니다.`)

// boolean
true
false

// empty value
undefined // type -> undefined
null // type -> object
typeof undefined
typeof null