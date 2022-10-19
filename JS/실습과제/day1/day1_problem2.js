let k = 0
function palindrome(str) {
  for (let i = 0; i < str.length/2; i++) {
    if (str[i] === str[str.length-1-i]) {
      k+=0
    } else {
      k+=1
    }
  }
  if (k === 0) {
    console.log(true)
  } else {
    console.log(false)
  }
}
palindrome('level')
palindrome('hi')
// 출력
// palindrome('level') => true
// palindrome('hi') => false