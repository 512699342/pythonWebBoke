

function  change_box_register()
{
    $('#register-box').toggle();
    var a = $('#register-box');
    var flag = a.attr('flag');
    if(flag == "0")
    {
        a.attr('flag','1');
        $('.global_register_title').text("新用户注册");
        $('.register-but').text("注册");
        $('#to-login').html('有账号？<!-- --> <a onclick="change_box_register()">去登录</a>');
        $('#post-from').attr('action','/user/register');
        $('.register-item-box').height(500);
    }
    else
    {
        a.attr('flag','0');
        $('.global_register_title').text("欢迎回来");
        $('.register-but').text("登录");
        $('#to-login').html('没有账号？<!-- --> <a onclick="change_box_register()">去注册</a>');
        $('#post-from').attr('action','/user/login');
        $('.register-item-box').height(350);
    }
}
