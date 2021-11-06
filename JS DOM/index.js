function mOver(obj) {
    obj.style.backgroundColor="blue"
}
function mOut(obj) {
    obj.style.backgroundColor="#a70e1a"
}
function changeColor(){
    document.getElementById("paragraph1").style.color="green"
    document.getElementById("paragraph2").style.color="yellow"
    document.getElementById("paragraph3").style.color="red"
}
function changeBgColor(){
    document.body.style.backgroundColor="#e6c3c3"
}
function copyContent(paragraph1, paragraph2){
    document.getElementById(paragraph1).innerHTML="Para2 The decision about what to put into your paragraphs begins with the germination of a seed of ideas; this “germination process” is better known as brainstorming. There are many techniques for brainstorming; whichever one you choose, this stage of paragraph development cannot be skipped. Building paragraphs can be like building a skyscraper: there must be a well-planned foundation that supports what you are building. Any cracks, inconsistencies, or other corruptions of the foundation can cause your whole paper to crumble."
    document.getElementById(paragraph2).innerHTML="Para1 Before you can begin to determine what the composition of a particular paragraph will be, you must first decide on an argument and a working thesis statement for your paper. What is the most important idea that you are trying to convey to your reader? The information in each paragraph must be related to that idea. In other words, your paragraphs should remind your reader that there is a recurrent relationship between your thesis and the information in each paragraph. A working thesis functions like a seed from which your paper, and your ideas, will grow. The whole process is an organic one—a natural progression from a seed to a full-blown paper where there are direct, familial relationships between all of the ideas in the paper."
}
function changeFontSize(){
    document.getElementById("paragraph1").style.fontSize="20px"
    document.getElementById("paragraph2").style.fontSize="20px"
    document.getElementById("paragraph3").style.fontSize="20px"
}
function increaseFontSize(){
    var el = document.getElementById("paragraph1");
    var style = window.getComputedStyle(el, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if(fontSize<30) {
        el.style.fontSize = (fontSize + 1) + 'px';
    }
    var el2 = document.getElementById("paragraph2");
    var style = window.getComputedStyle(el2, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if(fontSize<30) {
        el2.style.fontSize = (fontSize + 1) + 'px';
    }
    var el3 = document.getElementById("paragraph3");
    var style = window.getComputedStyle(el3, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if(fontSize<30) {
        el3.style.fontSize = (fontSize + 1) + 'px';
    }
}
function decreaseFontSize(){
    var el = document.getElementById("paragraph1");
    var style = window.getComputedStyle(el, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if(fontSize>10) {
        el.style.fontSize = (fontSize - 1) + 'px';
    }
    var el2 = document.getElementById("paragraph2");
    var style = window.getComputedStyle(el2, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if(fontSize>10) {
        el2.style.fontSize = (fontSize - 1) + 'px';
    }
    var el3 = document.getElementById("paragraph3");
    var style = window.getComputedStyle(el3, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    if(fontSize>10) {
        el3.style.fontSize = (fontSize - 1) + 'px';
    }
}