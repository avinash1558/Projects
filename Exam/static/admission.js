let admissionpoint = document.getElementById("admissionpoint");
let addbtn1 = document.getElementById("addbtn1");
let addbtn2 = document.getElementById("addbtn2");
addbtn1.addEventListener("click", function() {
    if (admissionpoint.style.display = "block") {
        admissionpoint.style.display = "none";
        addbtn1.style.display = "none";
        addbtn2.style.display = "block";
    }
})
addbtn2.addEventListener("click", function() {
    if (admissionpoint.style.display = "none") {
        admissionpoint.style.display = "block";
        addbtn2.style.display = "none";
        addbtn1.style.display = "block";

    }
})

let registration = document.getElementById("registration")
let personal = document.getElementById("personal")
let location1 = document.getElementById("location")
let parent = document.getElementById("parent")
let guardian = document.getElementById("guardian")
let Document = document.getElementById("Document")
let addhh1 = document.getElementById("addhh1")
let addh2 = document.getElementById("addh2")
let addh3 = document.getElementById("addh3")
let addh4 = document.getElementById("addh4")
let addh5 = document.getElementById("addh5")
let addh6 = document.getElementById("addh6")
addhh1.addEventListener("click", function() {
    registration.style.display = "block"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
addh2.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "block"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
addh3.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "block"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
addh4.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "block"
    guardian.style.display = "none"
    Document.style.display = "none"
})
addh5.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "block"
    Document.style.display = "none"
})
addh6.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "block"
})

let addhhh1 = document.getElementById("addhhh1")
let addhh2 = document.getElementById("addhh2")
let addhh3 = document.getElementById("addhh3")
let addhh4 = document.getElementById("addhh4")
let addhh5 = document.getElementById("addhh5")
let addhh6 = document.getElementById("addhh6")
addhhh1.addEventListener("click", function() {
    registration.style.display = "block"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
addhh2.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "block"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
addhh3.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "block"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
addhh4.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "block"
    guardian.style.display = "none"
    Document.style.display = "none"
})
addhh5.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "block"
    Document.style.display = "none"
})
addhh6.addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "block"
})

let add1 = document.getElementById("add1")
let add2 = document.getElementById("add2")

add1.addEventListener("click", function() {
    if (registration.style.display == "block") {
        registration.style.display = "block"
        personal.style.display = "none"
        location1.style.display = "none"
        parent.style.display = "none"
        guardian.style.display = "none"
        Document.style.display = "none"
    } else if (personal.style.display == "block") {
        registration.style.display = "block"
        personal.style.display = "none"
        location1.style.display = "none"
        parent.style.display = "none"
        guardian.style.display = "none"
        Document.style.display = "none"

    } else if (location1.style.display == "block") {
        personal.style.display = "block"
        registration.style.display = "none"
        location1.style.display = "none"
        parent.style.display = "none"
        guardian.style.display = "none"
        Document.style.display = "none"
    } else if (parent.style.display == "block") {
        location1.style.display = "block"
        personal.style.display = "none"
        registration.style.display = "none"
        parent.style.display = "none"
        guardian.style.display = "none"
        Document.style.display = "none"
    } else if (guardian.style.display == "block") {
        parent.style.display = "block"
        location1.style.display = "none"
        personal.style.display = "none"
        registration.style.display = "none"
        guardian.style.display = "none"
        Document.style.display = "none"
    } else if (Document.style.display == "block") {
        guardian.style.display = "block"
        location1.style.display = "none"
        parent.style.display = "none"
        personal.style.display = "none"
        registration.style.display = "none"
        Document.style.display = "none"
    }
})

add2.addEventListener("click", function() {
    if (registration.style.display == "block") {
        registration.style.display = "none"
        personal.style.display = "block"
        location1.style.display = "none"
        parent.style.display = "none"
        guardian.style.display = "none"
        Document.style.display = "none"
    } else if (personal.style.display == "block") {
        registration.style.display = "none"
        personal.style.display = "none"
        location1.style.display = "block"
        parent.style.display = "none"
        guardian.style.display = "none"
        Document.style.display = "none"

    } else if (location1.style.display == "block") {
        personal.style.display = "none"
        registration.style.display = "none"
        location1.style.display = "none"
        parent.style.display = "block"
        guardian.style.display = "none"
        Document.style.display = "none"
    } else if (parent.style.display == "block") {
        location1.style.display = "none"
        personal.style.display = "none"
        registration.style.display = "none"
        parent.style.display = "none"
        guardian.style.display = "block"
        Document.style.display = "none"
    } else if (guardian.style.display == "block") {
        parent.style.display = "none"
        location1.style.display = "none"
        personal.style.display = "none"
        registration.style.display = "none"
        guardian.style.display = "none"
        Document.style.display = "block"
    } else if (Document.style.display == "block") {
        guardian.style.display = "none"
        location1.style.display = "none"
        parent.style.display = "none"

        personal.style.display = "none"
        registration.style.display = "none"
        Document.style.display = "block"
    }
})
document.getElementById("subbtn11").addEventListener("click", function() {
    registration.style.display = "block"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn12").addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "block"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn21").addEventListener("click", function() {
    registration.style.display = "block"
    personal.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn22").addEventListener("click", function() {
    registration.style.display = "none"
    personal.style.display = "none"
    location1.style.display = "block"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn31").addEventListener("click", function() {
    personal.style.display = "block"
    registration.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn32").addEventListener("click", function() {
    personal.style.display = "none"
    registration.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "block"
    guardian.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn41").addEventListener("click", function() {
    location1.style.display = "block"
    personal.style.display = "none"
    registration.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn42").addEventListener("click", function() {
    location1.style.display = "none"
    personal.style.display = "none"
    registration.style.display = "none"
    parent.style.display = "none"
    guardian.style.display = "block"
    Document.style.display = "none"
})
document.getElementById("subbtn51").addEventListener("click", function() {
    parent.style.display = "block"
    location1.style.display = "none"
    personal.style.display = "none"
    registration.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn52").addEventListener("click", function() {
    parent.style.display = "none"
    location1.style.display = "none"
    personal.style.display = "none"
    registration.style.display = "none"
    guardian.style.display = "none"
    Document.style.display = "block"
})
document.getElementById("subbtn61").addEventListener("click", function() {
    guardian.style.display = "block"
    location1.style.display = "none"
    parent.style.display = "none"
    personal.style.display = "none"
    registration.style.display = "none"
    Document.style.display = "none"
})
document.getElementById("subbtn62").addEventListener("click", function() {
    guardian.style.display = "none"
    location1.style.display = "none"
    parent.style.display = "none"

    personal.style.display = "none"
    registration.style.display = "none"
    Document.style.display = "block"
})