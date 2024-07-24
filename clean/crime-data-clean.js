function sort(jsonArray) {
    jsonArray.sort((a, b) => {
        const dateA = new Date(a.incident_datetime);
        const dateB = new Date(b.incident_datetime);
        
        return dateA - dateB;
    });

    return jsonArray;
}

function cleanComputed(jsonArray) {
    return jsonArray.map(obj => {
        Object.keys(obj).forEach(key => {
            if (key.includes('computed_region')) {
                delete obj[key];
            }
        });
        return obj;
    });
}

let data = require('./crime-data.json')
data = data.filter((x) => x.police_district !== 'Out of SF')

data = sort(data)
cleanComputed(data)
console.log(data[data.length - 1])
