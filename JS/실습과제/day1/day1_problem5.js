const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

for (const k of participantNums ) {
  for (i = 0; i < k.length; i++) {
    let cnt = 0
    for (j = 0; j < k.length; j++) {
      if (k[i] === k[j]) {
        cnt++
      }
    }
    if (cnt != 2) {
      console.log(k[i])
    }
  }
}
// 3
// 100
// 62