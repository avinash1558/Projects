// caption
let w = document.getElementById('w');
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
w.innerText = caption()
let r = document.getElementById('r');
r.addEventListener("click", function() {
    w.innerText = caption()
})
let t = document.getElementById("text")
let captiontext = w.innerText
t.addEventListener("blur", function() {
    let text = t.value
    if (captiontext == text) {
        sub.style.display = "block"
        t.classList.remove("error")
    } else {
        sub.style.display = "none"
        t.classList.add("error")
            // console.log("aciai")
    }
})