function mOver(obj) {
    obj.style.backgroundColor="blue"
}
function mOut(obj) {
    obj.style.backgroundColor="#a70e1a"
}
function changeColor(){
    document.getElementById("paragraph1").style.color="blue"
    document.getElementById("paragraph2").style.color="grey"
    document.getElementById("paragraph3").style.color="green"
}
function changeBgColor(){
    document.body.style.backgroundColor="yellow"
}
function copyContent(paragraph1, paragraph2){
    document.getElementById(paragraph1).innerHTML=" Một đứa trẻ nhỏ nguệch ngoạc một vài nét, ta gọi là vẽ bậy. Nhưng vẫn là đứa trẻ đó, vẽ thêm mười bức nữa, ta gọi là sở thích. Thế rồi sau hàng trăm hàng ngàn bức vẽ khác, ta phải gọi đó đam mê, là cuộc sống của một đời người. Nếu ngay từ bức tranh đầu tiên, vẽ xong một bức vì nó xấu, vì bị chê bai mà bỏ cuộc,thì đâu còn câu chuyện nào để nói đâu."
    document.getElementById(paragraph2).innerHTML="Những người chúng ta đã gặp, , những người đang sống quanh ta, rốt cuộc tại sao họ lại đến, lại đi, họ mang đến gì và để lại gì cho cuộc sống của mình. Thật may là ở ai, họ cũng cho ta thấy được điều gì đó ở bản thân mình. Với bất cứ ai, hãy hoc cách nói cảm ơn vì những gì họ mang đến, bất kể cảm giác đó thế nào đi nữa. Có thể đúng, có thể sai, nhưng bản thân thấy ổn là được. Cuộc sống mà, đôi khi cách tốt nhất để nhớ hay quên một người, chính là quay lại nói lời cảm ơn với những gì họ đã mang đến, còn lòng mình, cứ thế, cứ thế yên bình, đi qua tháng năm...."
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