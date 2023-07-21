let btn = document.querySelectorAll(".box2 button")
let Q = document.querySelectorAll(".Q")
console.log(Q)
let S = 50
if (S === 20) {
    btn[1].style.display = "block"
    btn[2].style.display = "block"
    btn[3].style.display = "block"
    btn[4].style.display = "block"
    btn[5].style.display = "block"
    btn[6].style.display = "block"
    btn[7].style.display = "block"
    btn[8].style.display = "block"
    btn[9].style.display = "block"
    btn[10].style.display = "block"
    btn[11].style.display = "block"
    btn[12].style.display = "block"
    btn[13].style.display = "block"
    btn[14].style.display = "block"
    btn[15].style.display = "block"
    btn[16].style.display = "block"
    btn[17].style.display = "block"
    btn[18].style.display = "block"
    btn[19].style.display = "block"
    btn[0].style.display = "block"
}
if (S === 50) {
    btn[1].style.display = "block"
    btn[2].style.display = "block"
    btn[3].style.display = "block"
    btn[4].style.display = "block"
    btn[5].style.display = "block"
    btn[6].style.display = "block"
    btn[7].style.display = "block"
    btn[8].style.display = "block"
    btn[9].style.display = "block"
    btn[10].style.display = "block"
    btn[11].style.display = "block"
    btn[12].style.display = "block"
    btn[13].style.display = "block"
    btn[14].style.display = "block"
    btn[15].style.display = "block"
    btn[16].style.display = "block"
    btn[17].style.display = "block"
    btn[18].style.display = "block"
    btn[19].style.display = "block"
    btn[20].style.display = "block"
    btn[21].style.display = "block"
    btn[22].style.display = "block"
    btn[23].style.display = "block"
    btn[24].style.display = "block"
    btn[25].style.display = "block"
    btn[26].style.display = "block"
    btn[27].style.display = "block"
    btn[28].style.display = "block"
    btn[29].style.display = "block"
    btn[30].style.display = "block"
    btn[31].style.display = "block"
    btn[32].style.display = "block"
    btn[33].style.display = "block"
    btn[34].style.display = "block"
    btn[35].style.display = "block"
    btn[36].style.display = "block"
    btn[37].style.display = "block"
    btn[38].style.display = "block"
    btn[39].style.display = "block"
    btn[40].style.display = "block"
    btn[41].style.display = "block"
    btn[42].style.display = "block"
    btn[43].style.display = "block"
    btn[44].style.display = "block"
    btn[45].style.display = "block"
    btn[46].style.display = "block"
    btn[47].style.display = "block"
    btn[48].style.display = "block"
    btn[49].style.display = "block"
    btn[0].style.display = "block"
}
for (let i = 0; i < S; i++) {
    btn[i].addEventListener("click", function() {
        for (let i = 0; i < S; i++) {
            Q[i].style.display = "none"

        }
        Q[i].style.display = "block"
    })
}

let subbtn11 = document.getElementById("subbtn11")
let subbtn12 = document.getElementById("subbtn12")
let n = 0

subbtn12.addEventListener("click", function() {
    for (let i = 0; i < S; i++) {
        if (Q[i].style.display == "block") {
            n = i
            console.log(n)
                // break
        }
    }
    for (let j = 0; j < S; j++) {
        Q[j].style.display = "none"

    }

    if (n == S - 1 || n == S - 2) {
        btn[49].style.background = "red"
        Q[49].style.display = "block"
    } else {
        Q[n + 1].style.display = "block"
        btn[n + 1].style.background = "red"

    }
})
let p = 0
subbtn11.addEventListener("click", function() {
    for (let k = 0; k < S; k++) {
        if (Q[k].style.display == "block") {
            p = k
            console.log(n)
                // break
        }
    }
    for (let j = 0; j < S; j++) {
        Q[j].style.display = "none"
    }

    if (p == 0 || p == 1) {
        Q[0].style.display = "block"
    } else {
        Q[p - 1].style.display = "block"

    }
})
for (let b = 0; b < S; b++) {
    if (Q[b].style.display == "block") {
        for (let j = 0; j < S; j++) {
            btn[j].style.background = "tomato"
        }
        btn[b].style.background = "red"
        console.log("run")
    }
}

//
// subbtn11.addEventListener("click", function() {
//     if (String(no_of_q.value) === "50") {

//         if (box1.style.display == "block") {
//             box1.style.display = "block"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box2.style.display == "block") {
//             box1.style.display = "block"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box3.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "block"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"

//         } else if (box4.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "block"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box5.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "block"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box6.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "block"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box7.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "block"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box8.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "block"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box9.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "block"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box10.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "block"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box11.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "block"
//             box11.style.display = "none"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box12.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "block"
//             box12.style.display = "none"
//             box13.style.display = "none"
//         } else if (box13.style.display == "block") {
//             box1.style.display = "none"
//             box2.style.display = "none"
//             box3.style.display = "none"
//             box4.style.display = "none"
//             box5.style.display = "none"
//             box6.style.display = "none"
//             box7.style.display = "none"
//             box8.style.display = "none"
//             box9.style.display = "none"
//             box10.style.display = "none"
//             box11.style.display = "none"
//             box12.style.display = "block"
//             box13.style.display = "none"
//         }
//     }
// })