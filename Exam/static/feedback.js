let VeryBed = document.getElementById("VeryBed")
let Bed = document.getElementById("Bed")
let Good = document.getElementById("Good")
let Nice = document.getElementById("Nice")
let VeryGood = document.getElementById("VeryGood")
let feed = document.getElementById("feed")
VeryBed.addEventListener("click", function(e) {
    let VeryBedword = document.querySelectorAll("#VeryBed div")[1]
    console.log(VeryBedword.innerHTML)
    feed.value = VeryBedword.innerHTML

})
Bed.addEventListener("click", function(e) {
    let Bedword = document.querySelectorAll("#Bed div")[1]
    feed.value = Bedword.innerHTML

})
Good.addEventListener("click", function(e) {
    let Goodword = document.querySelectorAll("#Good div")[1]
    feed.value = Goodword.innerHTML

})
Nice.addEventListener("click", function(e) {

    let Niceword = document.querySelectorAll("#Nice div")[1]
    feed.value = Niceword.innerHTML

})
VeryGood.addEventListener("click", function(e) {
    let VeryGoodword = document.querySelectorAll("#VeryGood div")[1]
    feed.value = VeryGoodword.innerHTML

})
let email = document.getElementById("email")
let regemail = /[a-zA-Z0-9.%+-]+@[A-Za-z0-9].[A-Za-z]{2,10}/
email.addEventListener("blur", function() {
    let str = email.value
    if (regemail.test(str)) {
        email.classList.remove("error")
    } else {
        email.classList.add("error")
    }
})