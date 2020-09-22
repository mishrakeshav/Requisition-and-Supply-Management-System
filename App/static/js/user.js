
function editRow(no){
    no = Number(no);
    document.querySelector(`#confirm${no}`).style.display = "block";
    document.querySelector(`#request${no}`).style.display = "none";
}

setTimeout(() => {
    $("#req_msg").fadeOut();
}, 3000);