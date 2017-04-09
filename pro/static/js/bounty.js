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
            location.href = document.referrer
        }
        else
        {
            alert(msg);
        }
    });
}

//设置房租出租选择数据获取
function set_fangwu_chaxun()
{
     $.post("/fangwuchaxun",
    {
        man:'male'
    },
    function(msg,status)
    {
        if (msg=="")
        {
            alert("此城市没有登入房产平台信息");
        }
        else
        {
            alert(msg);
            var json_msg = eval(msg);
            var list_city_name_id = json_msg[0];
            var str_city_labels = ("<label for='child_city'> <input type='radio' value='0' style='visibility: hidden;' name='child_city' id='0'/>"+ 不限 +"</label>");
            for (var i = 0; i <list_city_name_id.length; i++) {
                    var map_city_name_id = list_city_name_id[i];
                    var city_val = map_city_name_id['id'];
                    var city_id = ("city"+map_city_name_id['id']);
                    var city_name = map_city_name_id['city_name'];
                    var str_city_label = ("<label for='child_city'> <input type='radio' value=" + city_val +" style='visibility: hidden;' name='child_city' id='"+ city_id +"'/>"+ city_name +"</label>");
                    str_city_labels += str_city_label;                
            }
            $("#city_names").innerHTML = str_city_labels;
        }
    });
}