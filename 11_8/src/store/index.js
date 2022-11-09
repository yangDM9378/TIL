import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: true, 
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title: '라떼',
        price: 4000,
        selected: true, 
        image: 'https://source.unsplash.com/featured/?latte'
      },
      {
        title: '카포치노',
        price: 4500,
        selected: true, 
        image: 'https://source.unsplash.com/featured/?cappuchino'
      },
    ],
    sizeList: [
      {
        name: 'small',
        price: 0,
        selected: true, 
      },
      {
        name: 'medium',
        price: 500,
        selected: true, 
      },
      {
        name: 'large',
        price: 1000,
        selected: true, 
      },
    ],
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0,
      },
      {
        type: '바닐라 시럽',
        price: 500,
        count: 0,
      },
      {
        type: '카라멜시럽',
        price: 500,
        count: 0,
      },
    ]
  },

  getters: {

  },

  mutations: {
    UPDATE_MENU(state, menu) {
      state.menuList = state.menuList.map((me) => {
        if (me === menu) {
          me.selected = !me.selected
        } else {
          me.selected = true
        }
        return me
      })
    },
    UPDATE_SIZE(state,size){
      state.sizeList = state.sizeList.map((siz) =>{
        if (siz === size) {
          siz.selected =!siz.selected
        } else {
          siz.selected = true
        }
        return siz
      })
    },
    INCREASE(state, option) {
      state.optionList = state.optionList.map((opt) => {
        if (opt === option) {
          opt.count++
        }
        return opt
      })
    },
    DECREASE(state,option){
      state.optionList = state.optionList.map((opt) =>{
        if (opt === option) {
          if (opt.count > 0) {
            opt.count--
          }
        }
      return opt
      })
    },
    ADDORDER(state) {
      const pickMenu = state.menuList.filter((menu) => {
        return menu.selected === false
      })
      const pickSize = state.sizeList.filter((size) => {
        return size.selected === false
      })
      const pickoption = state.optionList.map((option) => {
        return option
      })
      
      const obj = {
        pickMenu: pickMenu,
        pickSize: pickSize,
        pickoption: JSON.parse(JSON.stringify(pickoption)),
      }

      state.orderList.push(obj)
    }
  },

  actions: {
    updateMenu(context, menu) {
      context.commit('UPDATE_MENU', menu)
    },
    updateSize(context, size) {
      context.commit('UPDATE_SIZE',size)
    },
    increase(context, option) {
      context.commit('INCREASE', option)
    },
    decrease(context, option) {
      context.commit('DECREASE',option)
    },
    addorder(context) {
      context.commit('ADDORDER')
    }
  },

  modules: {

  }
})

  