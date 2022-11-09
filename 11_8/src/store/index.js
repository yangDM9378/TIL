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
    ],
    price:0,
    price_list:[],
    cnt:0
  },

  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      state.price=0
      state.orderList.forEach((order) =>{
        const menu_price=order.pickMenu[0].price
        const size_price=order.pickSize[0].price
        const s_price=order.pickoption[0].price*order.pickoption[0].count
        const b_price=order.pickoption[1].price*order.pickoption[1].count
        const k_price=order.pickoption[2].price*order.pickoption[2].count
        const total=menu_price+size_price+s_price+b_price+k_price
        state.price=state.price+total
      })
      return state.price
    },
    OrderPrice(state) {
      state.price_list=[]
      state.orderList.forEach((order) =>{
        const menu_price=order.pickMenu[0].price
        const size_price=order.pickSize[0].price
        const s_price=order.pickoption[0].price*order.pickoption[0].count
        const b_price=order.pickoption[1].price*order.pickoption[1].count
        const k_price=order.pickoption[2].price*order.pickoption[2].count
        const total=menu_price+size_price+s_price+b_price+k_price
        state.price_list.push(total)
      })
      return state.price_list
    }
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
        cnt:state.cnt
      }

      state.orderList.push(obj)
      state.cnt++
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

  