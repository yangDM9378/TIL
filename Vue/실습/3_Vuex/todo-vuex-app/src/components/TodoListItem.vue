<template>
<div>
  <div>
    <span 
      @click='updateTodoStatus' 
      :class="{'is-completed': todo.isCompleted }"
    >
    {{ todo.title }}
    </span>
    <button @click='deleteTodo'>Delete</button>
  </div>
</div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props:{
      todo: Object,
  },
  methods: {
    deleteTodo() {
      // console.log('삭제메서드 호출')
      // 아래로 변경가능 actions을 안써두 됨... 처리할 부분이 없어 바로 mutations로 보내두됨
      this.$store.dispatch('deleteTodo', this.todo)
      // this.$store.commit('DELETE_TODO', this.todo)
    },
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
    }
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>