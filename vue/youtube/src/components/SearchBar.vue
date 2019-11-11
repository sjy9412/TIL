<template>
    <div>
        <h1>유튜브 검색기</h1>
        <input @input="onInput" type="text" class="my-3">
    </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput(event) {
            // console.log 사용하기 위해서는 package.json의 rules에 추가해야함
            console.log('==SearchBar==')
            console.log(event.target.value)
            // $emit(이벤트이름, 값)
            // 이벤트이름의 이벤트를 발생 시킴(트리거)
            this.$emit('input-change-event', event.target.value)
        }
    }
}
</script>

<style>

</style>