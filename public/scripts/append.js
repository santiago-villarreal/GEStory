var fs = require("fs")


let aigner = new Map([["po", "Pointing"], 
                      ["ss", "Semaphoric static"],
                      ["sd", "Semaphoric Dynamic"],
                      ["sk", "Semaphoric Stroke "],
                      ["pa", "Pantomimic"],
                      ["is", "Iconic Static"],
                      ["id", "Iconic Dynamic"],
                      ["ma", "Manipulation"]
                      ])
let form = new Map([["s", "Static Gesture"],
                    ["d", "Dynamic Gesture"]
                    ])

let nature = new Map([["d", "Deictic"],
                      ["i", "Iconic"],
                      ["m", "Miming"],
                      ["p", "Physical"]
                    ])

let symmetry = new Map([["u", "Unilateral"],
                        ["s", "Bilateral-Symmetric"],
                        ["a", "Bilateral-Asymmetric"]
                    ])

let locale = new Map([["o", "On-the-object"],
                      ["i", "In-the-air"],
                      ["m", "Mixed"]
                    ])

let map = new Map([["Cl Aigner", aigner],
                   ["Form", form],
                   ["Nature", nature],
                   ["Symmetry", symmetry],
                   ["Locale", locale]
                ])

let array = ["Cl Aigner", "Form", "Nature", "Symmetry", "Locale"]

fs.readFile("gesture.json", (err,data)=>{
    data = JSON.parse(data)
    data = data.RefGes
    for (let index = 0; index < data.length; index++) {
        data[index].illustration = `image${index}.png`
        for (let prop of array) {
            data[index][prop] = map.get(prop).get(data[index][prop])
        }
    }
    fs.writeFile("gestureImg.json", JSON.stringify({"RefGes" : data},null, '\t'), ()=>{console.log("end")})
})