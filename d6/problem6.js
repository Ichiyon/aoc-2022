//


function readAhead (pos)
{
    let identifier = data[pos] + data[pos+1] + data[pos+2] + data[pos+3] 
    return identifier
}

const file = require('fs');
let data = file.readFileSync('input', 'ascii');

data = data.replace('\n', '');
data = data.split("")

