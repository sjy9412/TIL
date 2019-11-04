* **이벤트 루프 : call stack, callback queue 확인 (중요!)**

  * call stack이 비어있으면, callback queue에서 call stack으로 이동

  * 이벤트(함수실행..)

  * tick(틱)

    ```javascript
    function printHello() {
        console.log('Hellooo')
    }
    
    function baz() {
        console.log('baz')
        setTimeout(printHello, 0) // 0초여도 마지막에 출력
        console.log('baz end')
    }
    
    function bar() {
        console.log('bar')
        baz()
    }
    
    function foo() {
        console.log('foo')
        bar()
    }
    
    foo()
    ```

* synchronous/Asynchronous (동기/비동기)

* blocking/non-blocking