/* 
    Array helper methods
*/

/*
    Array.forEach
*/

let numbers = [1, 2, 3]
// 1. 반복문(for)
for (let i=0; i<numbers.length; i++){
    console.log(numbers[i])
}
// 2. 반복문(for .. of)
for (let num of numbers){
    console.log(num)
}
// 3. forEach (반복문이라 forEach자체에 return 값은 없음)
numbers.forEach(function(num) {
    console.log(num)
})
// 실습
const images = [
    {height: 30, width:20},
    {height: 100, width: 100},
    {height: 10, width: 5}
]
// let areas = [600, 10000, 50]
let areas = []
images.forEach(function(img, idx) {
    console.log(idx)
    areas.push(img.height * img.width)
})
console.log(areas)

/*
    map
    : 콜백함수의 return 결과를 각각 원소로 하는 배열을 리턴
*/

// 1.
let doubleNumbers = numbers.map(function(num){
    return num * 2
})
console.log(doubleNumbers)
// 2.
let doubleNumbers2  = numbers.map(number => number * 2)
console.log(doubleNumbers2)
// 실습 images -> map
let areas2
areas2 = images.map(function(img) {
    return img.height * img.width
})
areas2 = images.map(img => img.height * img.width)
console.log(areas2)

/*
    filter
    : 콜백함수의 return 결과가 참인 것을 각각 원소로 하는 배열을 리턴
*/
// images의 높이가 100보다 작은 object만 담은 배열
// 1. 반복문
let myImage = []
for (let image of images) {
    if (image.height < 100){
        myImage.push(image)
    }
}
console.log(myImage)
// 2. filter
myImage = images.filter(function(image) {
    return image.height < 100
})
console.log(myImage)
// fruit만 뽑아내기
let products = [
    {name: 'banana', type: 'fruit'},
    {name: 'tomato', type: 'vegetale'},
    {name: 'apple', type: 'fruit'},
    {name: 'cucumber', type: 'vegetable'}
]
let bag = []
bag = products.filter(product => product.type === 'fruit')
console.log(bag)
bag = products.filter(function (product){
    return products.type === 'fruit'
})

/* 
    reduce(callbackfn, initalvalue)
    : 원소 하나의 return 결과를 누적한 결과를 최종적으로 return
*/

let mySsafy=[100, 100, 95, 90]
let totalScore = mySsafy.reduce(function(total, score){
    console.log(total) // 누적
    console.log(score) // 원소
    return total + score
}, 100) // 초기값(기본 100 설정하면 100부터 시작)
mySsafy.reduce((total, score) => total + score, 100)

/*
    find
    : 일치하는 첫번째 원소를 리턴
*/
mySsafy.find(function(score){
    return score === 90
})

let heros = [
    {name: '헐크', age: 100},
    {name: '아이언맨', age: 50},
    {name: '스파이더맨', age: 30}
]

// 나이가 30인 사람
heros.find(function(hero){
    return hero.age === 30
})
heros.find(hero => hero.age === 30)

/*
    some, every
*/
let myNumbers = [1, 2, 3, 4]
myNumbers.some(function(number){
    return number % 2 === 0
}) // true

myNumbers = [3, 5]
myNumbers.every(function(number){
    return number % 2 !== 0
}) // true