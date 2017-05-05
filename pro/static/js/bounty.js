//=======================================================
//作者：韩望
//日期：2017-04-08
//功能：用户动态脚本函数
//更新：无
//备注：无
//=======================================================
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
function init_fangwu_chaxun()
{
     $.post("/fangwuchaxun/init",
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
            //alert(msg);
            var json_msg = eval(msg);
            var list_city_name_id = json_msg[0];
            var str_city_labels = ("<label for='child_city' id='lable_citynolimit' style='color:red;' onclick=\" testcheck('child_city','lable_citynolimit','citynolimit');\"> <input type='radio' value='0' checked='checked' style='visibility: hidden;' name='child_city' id='citynolimit'/> 不限 </label>");
            for (var i = 0; i <list_city_name_id.length; i++) {
                var map_city_name_id = list_city_name_id[i];
                var city_val = map_city_name_id['node_id'];
                var city_id = ("city"+map_city_name_id['node_id']);
                var lable_city_id = ("lable_city"+map_city_name_id['node_id']);
                var city_name = map_city_name_id['city_name'];
                var str_city_label = ("<label for='child_city' id = '" + lable_city_id + "' onclick=\" testcheck('child_city'," + lable_city_id + "," + city_id+ ")\" > <input type='radio' value='" + city_val +"' style='visibility: hidden;' name='child_city' id='"+ city_id +"'/>"+ city_name +"</label>");
                str_city_labels += str_city_label;                
            }
            $("#child_city_names").html(str_city_labels);

            var list_fangzu = json_msg[1];
            var str_fangzu_labels = ("<p><label for='fang_zus'> 租金:</label><label for='fang_zu'> <input type='radio' value='0' checked='checked' style='visibility: hidden;' name='fang_zu' id='fangzunolimit'/> 不限 </label>");
            var fangzu_val = list_fangzu[0];
            var fangzu_id = ('fangzu0');
            var fangzu_name =(list_fangzu[0] + "元以下");
            var str_fangzu_label = ("<label for='fang_zu'> <input type='radio' value='" + fangzu_val + "' style='visibility: hidden;' name='fang_zu' id=' "+ fangzu_id +"'/>"+ fangzu_name +"</label>");
            str_fangzu_labels += str_fangzu_label;
            for (var i = 0; i < list_fangzu.length; i++) {
                fangzu_val = list_fangzu[i];
                fangzu_id = ("fangzu"+i);
                if (i == (list_fangzu.length-1)) 
                {
                    fangzu_name = (list_fangzu[i] + "元以上");
                }
                else
                {
                    fangzu_name = (list_fangzu[i] + "-"+list_fangzu[i+1] + "元");
                }
                var str_fangzu_label = ("<label for='fang_zu'> <input type='radio' value='" + fangzu_val + "' style='visibility: hidden;' name='fang_zu' id=' "+ fangzu_id +"'/>"+ fangzu_name +"</label>");
                str_fangzu_labels += str_fangzu_label;
            }
            var str_input_submit = ("    <label for='pricestart'> <input type='text' style='width:70px;height:20px;' name='pricestart' id='price_start'/> — &nbsp;</label><label for='priceend'> <input type='text' style='width:70px;height:20px;' name='priceend' id='price_end'/></label>    <label for='subbtn'> <button type='btn btn-default'  style='height:20px;' name='subbtn' id='sub_btn' onclick=''>价格筛选</button></label>");
            str_fangzu_labels += str_input_submit;
            str_fangzu_labels += "</p>";
            $("#city_fangzu_levels").html(str_fangzu_labels);

            var list_agents = json_msg[2];
            var str_agent_labels = ("<p><label for='brand'> 品牌:</label><label for='agents'> <input type='radio' value='0' checked='checked' style='visibility: hidden;' name='agents' id='agentnolimit'/>不限</label>");
            for (var i = 0; i < list_agents.length; i++) {
                var agent_name = list_agents[i]['name'];
                var agent_id = ("agents" + list_agents['id']);
                var agent_val = (list_agents[i]['id']);
                var str_agent_label = ("<label for='agents'> <input type='radio' value='" + agent_val +"' style='visibility: hidden;' name='agents' id='" + agent_id + "'/>" + agent_name + "</label>");
                str_agent_labels += str_agent_label;
            }
            str_agent_labels += "</p>";
            $("#brand_agents").html(str_agent_labels);

        }
    });
}

//获取房屋出租检索参数与结果
function get_estate_rental_result()
{
	var rom_val = $('input:radio[name="rom"]:checked').val();
    alert("rom_val=" + rom_val);
	var cl_val = this.id;
	alert(cl_val)
}

//设置选中
function testcheck(str_lable,str_lable_id,str_sig_id)
{
	var id = ("#"+ str_lable_id);
	var sig_id = ("#"+ str_sig_id);
	if (str_lable == 'rom')
	{
		$("input:radio[name='rom']").attr("checked",false);
		$("#lable_romnolimit").css("color","black");
		$("#lable_rom_one").css("color","black");
		$("#lable_rom_two").css("color","black");
		$("#lable_rom_three").css("color","black");
		$("#lable_rom_four").css("color","black");
		$("#lable_rom_four_over").css("color","black");
	}
	if(str_lable=="rental")
	{
		$("input:radio[name='rental']").attr("checked",false);
		$("#lable_rentalnolimit").css("color","black");
		$("#lable_rental_all").css("color","black");
		$("#lable_rental_sigrom").css("color","black");
		$("#lable_rental_sigbed").css("color","black");
	}
	if(str_lable=="child_city")
	{
		alert("child _city here....");
	}
	$(sig_id).attr("checked","checked");
	$(id).css("color","red");
}
