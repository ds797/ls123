const fs = require('fs')
const path = '../ridership-2024-05.csv'

const row = (data, index) => data.split('\n')[index]
const column = (data, index) => {
	let r = data.split('\n')
	let c = ''
	for (let i = 0; i < r.length; i++) {
		if (i != 0) c += '\n'
		c += r[i].split(',')[index]
	}
	return c
}

fs.readFile(path, 'utf8', (err, data) => {
	if (err) {
		console.error(err)
		return
	}
	console.log(column(data, 0))
})
