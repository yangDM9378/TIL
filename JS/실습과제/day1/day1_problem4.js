const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

// const playGame = (p1_choice, p2_choice) => {
// 	for (i = 0; i < 10; i++) {
//     if (p1_choice[i] === "rock") {
//       if (p2_choice[i] === "rock") {
//         console.log(0)
//       } else if (p2_choice[i] === "scissors") {
//         console.log(1)
//       } else {
//         console.log(2)
//       }
//     } else if (p1_choice[i] === "scissors") {
//       if (p2_choice[i] === "rock") {
//         console.log(2)
//       } else if (p2_choice[i] === "scissors") {
//         console.log(0)
//       } else {
//         console.log(1)
//       }
//     } else {
//       if (p2_choice[i] === "rock") {
//         console.log(2)
//       } else if (p2_choice[i] === "scissors") {
//         console.log(1)
//       } else {
//         console.log(0)
//       }
//     }
//   }
// }
// playGame(p1, p2)
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2

// switch로 풀기
const playGame = (p1_choice, p2_choSwitch 인자 여러개ice) => {
	for (i = 0; i < 10; i++) {
    switch (p1_choice[i]) {
      case "rock":
        switch (p2_choice[i]) {
          case "rock":
            console.log(0)
            break
          case "scissors":
            console.log(1)
            break
          default:
            console.log(2)
        } break
      case "scissors":
        switch (p2_choice[i]) {
          case "rock":
            console.log(2)
            break
          case "scissors":
            console.log(0)
            break
          default:
            console.log(1)
        } break
      default:
        switch (p2_choice[i]) {
          case "rock":
            console.log(2)
            break
          case "scissors":
            console.log(1)
            break
          default:
            console.log(0)
        } break
    }
  }
}

playGame(p1, p2)