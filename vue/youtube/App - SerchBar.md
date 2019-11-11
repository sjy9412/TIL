## App - SerchBar

input 태그에 등록된 이벤트(@input)

1. input 값이 변경 되면(trigger),
2. 인자로 `event`
3. `onInput` method 실행

---

search-bar 컴포넌트에 등록된 이벤트(@input-change-event)

4. `$emit` 메소드 실행되면(trigger), 
5. 인자로 `event.target.value`
6. `onInputCange` method  실행

