'use strict';

var searchBox = document.querySelectorAll('.search-box input[type="text"] + span');

searchBox.forEach(elm => {
  elm.addEventListener('click', () => {
    elm.previousElementSibling.value = '';
  });
});
function myFunctionReq() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("reqstock_input");
    filter = input.value.toUpperCase();
    console.log(filter)
    table = document.getElementById("reqstock_table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    
    for (i = 0; i < tr.length; i++) {

        // Logic for 1st column
        td = tr[i].getElementsByTagName("td")[1];
        console.log()
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
       
        
    }
    
}
function myFunction() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    
    for (i = 0; i < tr.length; i++) {

        // Logic for 1st column
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
       
        
    }
    
}

function search_requests() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("request_input");
    filter = input.value.toUpperCase();
    
    table = document.getElementById("request_table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    
    for (i = 0; i < tr.length; i++) {

        // Logic for 1st column
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
       
        
    }
    
}

function search_summary() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("summary_input");
    filter = input.value.toUpperCase();
    console.log(filter)
    table = document.getElementById("summary_table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    
    for (i = 0; i < tr.length; i++) {

        // Logic for 1st column
        td = tr[i].getElementsByTagName("td")[2];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
       
        
    }
    
}




























































