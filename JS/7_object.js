// const myInfo = {
//   name: 'jack',
//   phoneNumber: '123456',
//   'samsung product': {
//     buds:'Buds pro',
//     galaxy: 'S99',
//   },
// }

// console.log(myInfo.name)
// console.log(myInfo['name'])
// console.log(myInfo['samsung product'].galaxy)

// const obj = {
//   name: 'jack',
//   greeting() {
//     console.log('hi!')
//   }
// }

// console.log(obj.name)
// console.log(obj.greeting())

const jsonData = {
  coffee: 'Americano',
  iceCream: 'Mint Choco',
}

//objecct -> json
const objToJson = JSON.stringify(jsonData)
console.log(objToJson)
console.log(typeof objToJson)
//json ->object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)
console.log(typeof jsonToObj)
console.log(jsonToObj.coffee)