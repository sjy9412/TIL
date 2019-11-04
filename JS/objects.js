const me = {
    name: 'tak',
    phone: '010-1234-5678',
    // 메서드에서도 arrow function 사용 금지
    greeting: function() {
        return 'hi, ' + this.name
    }
}

const Person = function(name, phone) {
    this.name = name
    this.phone = phone
    this.greeting = function() {
        return 'hi, ' + this.name
    }
}
// 불러오기(new 키워드와 함께 사용)
const me = new Person('tak', '010-1234-5678')

// 생성자 함수에서는 arrow function 사용 금지
const Animal = name => {
    this.name = name
}
const dog = new Animal('dog') // Error

// object 리터럴
const name = '겨레'
const phone = '010-1234-5678'
const greeting = function() {
    return 'hi, ' + this.name
}
const you = {
    name,
    phone,
    greeting
}