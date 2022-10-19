// console.log('hello.javascript')

// function add(num1, num2) {
//   return num1 + num2  
// }

// console.log(add(2,7))

// const sub = function (num1, num2) {
//   return num1 - num2
// }
// console.log(sub(2,7))

// const greeting = function (name = 'Anonymous') {
//   return `Hi ${name}`
// }
// console.log(greeting())

// // 1단계
// const greeting = (name) => {
//   return `Hi ${name}`
// }
// // 2단계
// const greeting = name => {
//   return `Hi ${name}`
// }
// // 3단계
// const greeting = name => `Hi ${name}`

// const noArgs = function() {
//   return 0
// }
// console.log(noArgs(1,2,3))

// const twoArgs = function (arg1, arg2) {
//   return [arg1, arg2]
// }
// console.log(twoArgs(1,2,3))

// const threeArgs = function (arg1, arg2, arg3) {
//   return [arg1, arg2, arg3]
// }
// console.log(threeArgs())
// console.log(threeArgs(1))

const numbers = [1, 2, 3, 4, 5]
console.log(numbers[0])
console.log(numbers[-1])
console.log(numbers.length)
console.log(numbers[numbers.length - 1])

numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)
numbers.pop(100)
console.log(numbers)

console.log(numbers.includes(1))
console.log(numbers.includes(100))

console.log(numbers.indexOf(3))
console.log(numbers.indexOf(100))

console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join(' '))
console.log(numbers.join('-'))

