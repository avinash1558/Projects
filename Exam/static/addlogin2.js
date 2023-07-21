// email vailidation
let sub1 = document.getElementById("sub1")
let email = document.getElementById("email")
let regemail = /[a-zA-Z0-9.%+-]+@[A-Za-z0-9].[A-Za-z]{2,10}/
email.addEventListener("blur", function() {
        let str = email.value
        if (regemail.test(str)) {
            email.classList.remove("error")
            sub1.style.display = "block"
        } else {
            sub1.style.display = "none"
            email.classList.add("error")
        }
    })
    // caption
let w1 = document.getElementById('w1');
// 66

function caption() {
    var arr = ['Q', 'W', 'i', 'o', 'R', 'T', '&', 'q', 'Y', 'G', 'u', 'a', 'H', 'J', '4', '5', 'K', 'p', 'E', 'w', 'e', '7', '8', 'r', 'X', 'C', 'k', '0', 'V', 'B', 'N', 'f', 'g', 'M', '1', '2', 'F', 'j', '3', '6', 't', 'y', 's', ",", 'd', 'L', 'Z', '9', 'h', 'U', 'b', 'n', 'I', 'O', 'z', 'x', 'P', 'A', 'S', 'D', '!', '@', '#', 'l', 'c', 'v', 'm'];
    let r1 = 1,
        r2 = 66;
    let ren = Math.floor(r1 + (r2 - r1) * Math.random());
    let c1 = arr[ren];
    let ren1 = Math.floor(r1 + (r2 - r1) * Math.random());
    let c2 = arr[ren1];
    let ren2 = Math.floor(r1 + (r2 - r1) * Math.random());
    let c3 = arr[ren2];
    let ren3 = Math.floor(r1 + (r2 - r1) * Math.random());
    let c4 = arr[ren3];
    let ren4 = Math.floor(r1 + (r2 - r1) * Math.random());
    let c5 = arr[ren4];
    let ren5 = Math.floor(r1 + (r2 - r1) * Math.random());
    let c6 = arr[ren5];
    let ren6 = Math.floor(r1 + (r2 - r1) * Math.random());
    let c7 = arr[ren6];
    let cap = c1 + c2 + c3 + c4 + c5 + c6 + c7;
    return cap
}
// console.log(cap)
w1.innerText = caption()
let r1 = document.getElementById('r1');
ren1.addEventListener("click", function() {
    w1.innerText = caption()
})
let t1 = document.getElementById("text1")
let captiontext = w1.innerText
t1.addEventListener("blur", function() {
    let text = t1.value
    if (captiontext == text) {
        sub1.style.display = "block"
        t1.classList.remove("error")
    } else {
        sub1.style.display = "none"
        t1.classList.add("error")
            // console.log("aciai")
    }
})