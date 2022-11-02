<template>
  <div class="border">
    <h1>내가 만든 componet</h1>
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @give-ma-money="parentGetEvent"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
// 1.불러오기
import MyComponentItem from '@/components/MyComponentItem'


export default {
    name: 'MyComponent',
    //2. 등록하기
    components: {
        MyComponentItem,
    },
    data: function () {
      return {
        dynamicProps: '이건 동적 데이터!',
      }
    },
    methods:{
      parentGetEvent: function (childdata) {
        console.log('용동없어!!')
        console.log(childdata)
      },
      getDynamicData: function(childInputData) {
        console.log(`사용자가 입력한 값은 ${ childInputData }입니다.`)
      }
    }
}
</script>

<style>
    .border {
        border: solid 1px black
    }
</style>