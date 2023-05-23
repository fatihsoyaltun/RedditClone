var modal = document.getElementById("myModal");
let mybutton = document.getElementById("ica");
let navbarDropdown=document.querySelector(".navbar-dropdown")
let hepsi1=document.querySelector(".hepsi1")
let navbarAlt=document.querySelector(".navbar_alt")
let alerttt=document.querySelector("#alerttt")


  const myTimeout = setTimeout(display, 2300);
  function display() {
    alerttt.style.display="none"
  }
  





// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal


// When the user clicks on <span> (x), close the modal


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}



//detay kübra

// const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
// const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// const myModal = document.getElementById('myModal')
// const myInput = document.getElementById('myInput')


// myModal.addEventListener('shown.bs.modal', () => {
//   myInput.focus()
// })

function yorum() {
  const commentInput = document.querySelector(".write-comments");
  if (commentInput.style.display === "none") {
    commentInput.style.display = "block";
  } else {
    commentInput.style.display = "none";
  }
}



function bell() {
  var zil = document.querySelector(".bi-bell");
  zil.style.color = "red";  
  
}

function openSecondModal() {
  document.querySelector('#exampleModal').hide();
  document.querySelector('#exampleModal2').show();
}

function kumoreoptions() {
  const drop = document.querySelector(".kubegenidropdown-menu");
  if(drop.style.display == "none"){
    drop.style.display = "block";
  }
  else{
    drop.style.display = "none";
  }
  
}

// JavaScript kodu
const darkModeToggle = document.querySelector('.dark-mode-toggle');
const body = document.querySelector('body');
const logo = document.querySelector('mobile-logo');
const darkLogo = document.querySelector('.mobile-logo1');

// kaydedilen tema ayarını kontrol edin ve temayı yükle
if (localStorage.getItem('theme') === 'dark') {
  body.classList.add('dark-mode');
}

// butona tıklandığında tema ayarını değiştirin
darkModeToggle.addEventListener('click', () => {
  if (body.classList.contains('dark-mode')) {
    body.classList.remove('dark-mode');
    localStorage.setItem('theme', 'light');
    logo.style.display = 'none';
    darkLogo.style.display = 'block'; // tema ayarını kaydedin
  } else {
    body.classList.add('dark-mode');
    localStorage.setItem('theme', 'dark');
    logo.style.display = 'block';
    darkLogo.style.display = 'none'; // tema ayarını kaydedin
  }
});


const navprofil = document.querySelector(".dropbtn");



if (localStorage.getItem('theme') === 'dark') {
  navprofil.style.background = "none"
  navprofil.classList.add('dark-mode');
  body.classList.add('dark-mode');
  
}



navbarDropdown.addEventListener("click",function name() {
  if (hepsi1.className=="col-3 hepsi1") {
    hepsi1.classList.add("block");
    hepsi1.style.transition = " 2s";
    hepsi1.style.display="block"
   }else{
       hepsi1.classList.remove("block")
       hepsi1.style.display="none"
      
   }
   navbarAlt.style.display="none"
})



var editor = new FroalaEditor('#example');