const arr = [1, 2, 3, 4, 5]

const k = arr.some(function (elem) {
  return elem % 2 === 0
})

const k = arr.some((elem) => {
  return elem % 2 === 0
})

const k = arr.some((elem) => elem % 2 ===0)

console.log(k)

const arr = [1, 2, 3, 4, 5]
const k = arr.every((elem) => elem % 2 ===0)
console.log(k)