var modal = document.getElementById("myModal");
let mybutton = document.getElementById("ica");
let navbarDropdown=document.querySelector(".navbar-dropdown")
let hepsi1=document.querySelector(".hepsi1")
let navbarAlt=document.querySelector(".navbar_alt")

// Get the button that opens the modal

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

var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

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

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')


myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})

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

