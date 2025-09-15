//dom manipulation
//select an element
const mydiv=document.getElementById("mydiv");
//change its text content
mydiv.textcontent="hello,Dom manipulation";
//add a class
mydiv.classList.add("highlight");
//create a new paragraph and opened it
const newParagraph=document.createElement('p');
newParagraph.textcontent='this is a new';
mydiv.appendChild(newparagraph);
//adda an event listener
mydiv.addEventListener('click',() => {
    alert('Div clicked');
});