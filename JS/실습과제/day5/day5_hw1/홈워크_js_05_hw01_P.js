axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log(response.data)
})

// 동기 비동기 => 동기는 입력 순서와 출력 순서가 같은것. 비동기는 입력 순서와 출력 순서가 같지 않고 빠르게 해결할수 있는 것을 먼저 처리하는것