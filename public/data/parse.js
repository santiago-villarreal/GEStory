const { count } = require("console");
const fs = require("fs")

function deleteDuplicate(){
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
            if (object.duplicate != 0){
                object.name += ` (${object.duplicate + 1})`
            }
            delete object.duplicate
        }
        fs.writeFile("./data.json", JSON.stringify(data, null, "\t"), (err)=>{
            console.log("Done writing")
        })
    })
}

function addDeviceEnv(){
    /**
     * function used to add the device and environment to the database
     */
    let data = fs.readFileSync("GES267-GesturesV2.csv", 'utf8')
    data = data.split("\n").slice(1)
    data = data.map((val)=> val.split(";"))
    data = data.filter((val)=>val[0] && val[1] && !isNaN(val[0]))
    data = data.map((val)=>val.slice(0,2).reverse())
    data = new Map(data)  // create the map (Name_study, ID)

    let newDeviceEnv = fs.readFileSync("doc.csv", 'utf-8')
    newDeviceEnv = newDeviceEnv.split("\n").slice(1)
    newDeviceEnv = newDeviceEnv.map((value)=>value.split(";"))
    newDeviceEnv = newDeviceEnv.filter((value)=> value[0] && !isNaN(value[0]))
    newDeviceEnv = newDeviceEnv.map((value)=>{
        let item = [
            value[0],
                { 
                    "device" : "undefined",
                    "environment" : "undefined"
                }
            ]
        if (value[1]){
            item[1].device = value[1] 
        }
        if (value[2]){
            item[1].device += ", " + value[2]
        }
        if (!value[5]) {
            value[5] = ""
        }else{
            value[5] = value[5].slice(0 ,value[5].length - 1)
        }
        if (value[4]){
            item[1].environment = value[4]
        }
        if (value[5]){
            item[1].environment +=  ", " + value[5]
        }
        return item
    })

    newDeviceEnv = new Map(newDeviceEnv)  // create the map (ID => {device, env})


    let fullData = fs.readFileSync("data.json", 'utf-8')
    fullData = JSON.parse(fullData)
    fullData = fullData.map(value=>{
        if (data.has(value.title)){
            let item = newDeviceEnv.get(data.get(value.title))  // get the device and env for this item => get name => get id => return JSON with device and env
            value.device = item.device
            value.environment = item.environment
        }else{
            console.log(value.title)
        }
        return value
    })

    fs.writeFileSync("data.json", JSON.stringify(fullData, null, "\t"))
}

//addDeviceEnv()