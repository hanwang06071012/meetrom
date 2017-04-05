//测试用例
function test()
{
	alert("I am in testing ......");
}

//设置城市
function set_addr(addr_node_id)
{
     $.post("/set/addr",
    {
        str_node_id:addr_node_id
    },
    function(msg,status)
    {
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

//设置城市并把回到上一页
function set_addr_go_back(addr_node_id)
{
     $.post("/set/addr",
    {
        str_node_id:addr_node_id
    },
    function(msg,status)
    {
        if (msg=="")
        {
            history.back(-1);
        }
        else
        {
            alert(msg);
        }
    });
}
