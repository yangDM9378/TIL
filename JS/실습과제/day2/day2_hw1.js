for (k = 0; k < 5; k++) {
  let star = ''
  for (i = 4 - k; i > 0; i--) {
    star += ' '
  }
  for (j = 0; j < 2 * k + 1; j++) {
    star += '*'
  }
  for (i = 4 - k; i > 0; i--) {
    star += ' '
  }
  console.log(star)
}

