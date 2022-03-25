const fs = require("fs")

fs.readFile("./dataDuplicate.json", (err, data)=>{
    data = JSON.parse(data);
    final = [];
    for (let object of data) {
        object.duplicate = 0;
        for (let object2 of final){
            if ( (object.name == object2.name && object.title == object2.title)){
                object.duplicate++;
            }
        }
        final.push(object)
    }
    for (let object of data){
        object.name += ` (${object.duplicate + 1})`
        delete object.duplicate
    }
    fs.writeFile("./data.json", JSON.stringify(data, null, "\t"), (err)=>{
        console.log("Done writing")
    })
})