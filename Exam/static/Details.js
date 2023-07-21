let search = document.getElementById('search');
let searchbtn = document.getElementById('searchbtn');
let word = document.getElementsByClassName("h2")
searchbtn.addEventListener('click', function() {
    let inputVal = search.value;
    Array.from(word).forEach(function(element) {
        let content = element.innerText
        content = String(content)
        content = content.toLowerCase();
        console.log(content)
        console.log(inputVal)
        inputVal = inputVal.toLowerCase();
        if (content.includes(inputVal)) {

            // console.log("yes")
            element.style.background = 'tomato';
            setTimeout(() => {
                element.style.background = 'none';

            }, 6000);
        }
    })

})