$(function (){
    //当点击搜索后，在当前页面展示搜索结果
    $('#search').on('click', function (){
        var content = $(".form-control:eq(1)").val()
        //如果当前搜索内容为空，无需进行查询
        if(content.length == 0){
            alert("请输入一定的内容后再查询！")
            return;
        }
        //取到当前选中的内容
        var type = $(".form-control:eq(0)").val()
        $.ajax({
            type:"POST",
            url:"/Item/searchByType",
            data:{type_select:type, content:content},
            success:function (data){
                if(type == "product"){
                    $("#table_product").html(data)
                }else{
                    $("#table_category").html(data)
                }
            }
        });
    });

    //点击下拉框切换显示的内容Category或者Product
    $('.form-control:eq(0)').on('change',function () {
        //取到当前选中的内容
        var type = $(".form-control:eq(0)").val()
        if(type == "product"){
            $('#table_category').css("display","none")
            $('#table_product').css("display","block")
        }else{
            $('#table_category').css("display","block")
            $('#table_product').css("display","none")
        }
    });

});