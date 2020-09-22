var btn = $("#additembtn");
var form = $("#additemform");
form.hide();


btn.on("click", ()=>{
    btn.slideOut();
    form.slideIn();
});

function edit_row(no)
{
    document.getElementById("edit_button"+no).style.display="none";
    document.getElementById("save_button"+no).style.display="block";

    var id =document.getElementById(+no);
    var item=document.getElementById("item"+no);
    var avail=document.getElementById("avail"+no);
    var qty_req=document.getElementById("qty-req"+no);
    
    var id_data  =id.innerHTML;
    var item_data=item.innerHTML;
    var avail_data=avail.innerHTML;
    var Qty_data=qty_req.innerHTML;

    id.innerHTML=`<input type='text' class=" form-control"  name='id'  value ='${id_data}' readonly>`;
    item.innerHTML=`<input type='text' class=" form-control"  name='item_text'  value ='${item_data}' readonly>`;
    avail.innerHTML=`<input type='number' class=" form-control"  name='avail_text'  value ='${avail_data}' min="0">`;
    qty_req.innerHTML=`<input type='number' class=" form-control"  name='qty_text'  value ='${Qty_data}' min="0">`;

}

