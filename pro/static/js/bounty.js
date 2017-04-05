function test()
{
	alert("I am in testing ......");
}

function set_addr(addr_node_id)
{
     $.post("/set/addr",
    {
        str_node_id:addr_node_id
    },
        function(msg,status){
            if (msg=="")
            {
                location.reload();
            }
            else
            {
                alert(msg);
            }
    });
}
