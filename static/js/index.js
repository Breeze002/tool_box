layui.config({
  base: "../static/js/" // 配置你的模块路径
}).use(['element', 'layer', 'jquery'], function() {
  var layer = layui.layer,
      element = layui.element,
      $ = layui.jquery;
 loadContent('/get_AItool', undefined, undefined);


  // 创建一个函数来处理AJAX请求和内容加载
  function loadContent(url, successCallback, errorCallback) {
    $('#contentArea').empty();
    $.ajax({
      url: url,
      type: 'GET',
      success: successCallback || function(data) {
        // 默认成功后的操作
        $('#contentArea').html(data);
      },
      error: errorCallback || function() {
        // 默认失败时的操作
        layer.alert('加载内容失败');
      }
    });
  }

  // 绑定点击事件到具有类 AItool 的链接
  $('.AItool').on('click', function() {
    loadContent('/get_AItool', undefined, undefined); // 不传递任何额外的回调函数
  });

  // 绑定点击事件到具有类 research_tool 的链接
  $('.research_tool').on('click', function() {
    loadContent('/research_tool');
  });



});