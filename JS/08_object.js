const me = {
    // 프로퍼티
    name: 'kim',
    'phone number': '01012345678',
    phone: {
        type: 'iphone XS MAX'
    },
    // 메서드 function 키워드만 작성하자!
    greeting: function() {
        console.log(this) // me
        console.log(`hi ${this.name}`)
    },
    greeting2: () => {
        console.log(this) // 전역 객체 window
        console.log(`hi ${this.name}`)
    }
}

console.log(me.name)
console.log(me['name'])
console.log(me.phone.type)
console.log(me.greeting()) // hi kim
console.log(me.greeting2()) // hi (arrow function을 쓰면 안된다)

// ES6+ 오브젝트 리터럴
let book = '자바스크립트 완전 정복'
let albums = {
    IU: ['좋은날', '밤편지'],
    BTS: ['작은것들을 위한 시']
}

// let bag = {
//     book,
//     albums
// }

// JSON(Javaxcript object notation - 자바스크립트 오브젝트 표기법)
// 문자열
// object -> JSON
let jsonData = JSON.stringify(albums)
let myObject = JSON.parse(jsonData)
typeof jsonData
typeof myObject