<template>
<div class="todo-List">
      <h2>{{ category }}</h2>
      <input type="text" @keyup.enter="addTodo" v-model="content"><button @click="addTodo">등록</button>
      <li v-for="todo in todos" :key="todo.id">{{ todo.content }}<button style="margin-left: 4px;" @click="removeTodo(todo.id)">삭제</button></li>
    </div>
</template>
<script>
export default {
    props: {
        category: {
          type: String,
          required: true
        }
      }, // 하위컴포넌트로 데이터 전송 + 검증
      data: function () {
        return {
          todos: [],
          content: ''
        }
      },
      methods: {
        addTodo() {
          this.todos.push({
            id: Date.now(),
            content: this.content,
            completed: false
          })
          this.content = ''
        },
        removeTodo(key) {
          this.todos = this.todos.filter(todo => {
            return todo.id !== key
          })
        }
      }
}
</script>
<style lang="">
    /* li {
        color: blue;
    } */
</style>