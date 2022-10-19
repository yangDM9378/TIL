const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	for (i = 0; i < 10; i++) {
    if (p1_choice[i] === "rock") {
      if (p2_choice[i] === "rock") {
        console.log(0)
      } else if (p2_choice[i] === "scissors") {
        console.log(1)
      } else {
        console.log(2)
      }
    } else if (p1_choice[i] === "scissors") {
      if (p2_choice[i] === "rock") {
        console.log(2)
      } else if (p2_choice[i] === "scissors") {
        console.log(0)
      } else {
        console.log(1)
      }
    } else {
      if (p2_choice[i] === "rock") {
        console.log(2)
      } else if (p2_choice[i] === "scissors") {
        console.log(1)
      } else {
        console.log(0)
      }
    }

  }
}
playGame(p1, p2)
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