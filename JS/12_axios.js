console.log('hi')
axios.get('https://jsonplaceholder.typicode.com/posts/1') // 비동기적
    .then(response => {
        console.log(response) // 비동기적이라 마지막에 출력
        document.write(`
            <h1>${response.data.id}. ${response.data.title}</h1>
            <p>${response.data.body}</p>
        `)
        return response.data
    })
console.log('bye')