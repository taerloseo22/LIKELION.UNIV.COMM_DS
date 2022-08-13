$(function(){ 

    $("button").click(function(){
      $(".modal").fadeIn();
    });
    
    // $(".modal").click(function(e){
    //     if(!$(e.target).hasClass('modal_content')){
    //         $(".modal").fadeOut();
    //         console.log('레이어팝업 외의 영역입니다')
    //     }
    // });

    $(document).mouseup(function (e){
        var LayerPopup = $(".modal_content");
        if(LayerPopup.has(e.target).length === 0){
            $(".modal").fadeOut();
        }
      });
    
    
  });