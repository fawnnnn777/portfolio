$(document).ready(()=>{
    $('#save-button').on('click',()=>{
            $('.style-div, .info-div').toggle()
            $('#back-button').toggle();
            $('#save-button').hide();
    })
    $('#back-button').on('click', ()=>{
        $('#back-button').toggle();
        $('.style-div, .info-div').toggle()
        $('#save-button').show();
    })

})

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector(".nav").style.top = "0";
  } else {
    document.querySelector(".nav").style.top = "-100px";
  }
  prevScrollpos = currentScrollPos;
}

const observer = new IntersectionObserver((entries)=>{
    entries.forEach((entry)=>{
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        }
        else{
            entry.target.classList.remove('show');
        }
    })
})

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el)=> observer.observe(el));