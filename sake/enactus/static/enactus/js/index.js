var md = 768;

var isMenuVisible = false
var sidenav = document.getElementById("sidenav");
var utility_account = document.getElementById("utility-account");
var menuToggleBtnContainer = document.getElementById("menuToggleBtnContainer");
menuToggleBtnContainer.addEventListener ("click", toggleSideNav, false);
utility_account.style.display = "initial"
// utility_account.addEventListener("click",test,false);

window.addEventListener('resize', function(event){
    const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
    const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
    console.log(vw);
    if(vw>=md){
        sidenav.style.marginLeft = "0px";
        utility_account.style.display = "initial"
    }else{
        closeSideNav()
        utility_account.style.display = "none"
    }
});

function toggleSideNav(){
    const vw = Math.max(document.documentElement.clientWidth||0, window.innerWidth);
    if(vw>=md){
        return
    }
    console.log("Collapsing");   
    if(isMenuVisible){
        sidenav.style.marginLeft = "-250px";
        console.log("closing");
    }else{
        sidenav.style.marginLeft = "0px";
        console.log("Opening");
    }
    isMenuVisible = !isMenuVisible;
    
}

function closeSideNav(){
    console.log("+-+-+-+Collapsing+-+-+-+");
    var sidenav = document.getElementById("sidenav");
    sidenav.style.marginLeft = "-250px";
    console.log("closing");
    isMenuVisible = !isMenuVisible;  
}

function test(){
    alert("Working!");
}
/* TO DO 


*/
