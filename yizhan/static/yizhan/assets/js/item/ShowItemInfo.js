$(function (){
    $('#search').on('click',function () {
        var itemId = $('.form-control:eq(0)').val()
        var productId = $('.form-control:eq(1)').val()
        if(itemId.length == 0 && productId.length == 0){
            alert("请输入一定的内容后再查询！")
            return;
        }
        $.ajax({
            type:"POST",
            url:"/Item/searchByInfo",
            data:{itemId:itemId, productId:productId},
            success:function (data){
                $("#table").html(data)
            }
        });
    });
});