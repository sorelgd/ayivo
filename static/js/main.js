var indiCharCount = 0;
var textWordsCount = 0;
var textSelectorWords = [
   "Awe-inspiring",
   "Amazing",
   "Incredible",
   "Unbelievable",
   "Unimaginable",
   "Astonishing",
   "Breathtaking",
   "Extraordinary",
   "Impressive",
   "Marvelous",
   "Spectacular",
   "Stunning",
   "Striking",
   "Eye-catching",
   "Daring"
];

$(document).ready(function(){
   $('.parallax').parallax();
   
   $(window).scroll(function() {
      if ($(this).scrollTop() > 720){ 
        $('header').addClass("headerShow"); 
      }
      else{
        $('header').removeClass("headerShow");
      }
      
   });
   
   textChangerStart();
   
   

});


function textChangerStart(){
   
   var mainTimer = setInterval(function() { 
      
      $('#text-selector-change').text("");
      $('#text-selector-change').css("background-color", "rgba(51, 102, 153, 0.0)");
            
      var secondTimer = setInterval(function() { 
         
         $('#text-selector-change').append(textSelectorWords[textWordsCount][indiCharCount]);
         indiCharCount++;           
         
         if (indiCharCount >= textSelectorWords[textWordsCount].length){
            $('#text-selector-change').css("background-color", "rgba(51, 102, 153, 0.23)");
            clearInterval(secondTimer);
         }
         
      }, 130);
      
            
      indiCharCount=0;            
      textWordsCount++;
      
      
      if (textWordsCount >= textSelectorWords.length){
         textWordsCount=0;
      }      
    }, 7500);
    
    
}


$('#hamburgerButton').click(function() {
   $('#hamburgerContent').addClass("hamburgerContentOpen"); 
   $('#hamburgerContent').removeClass("hamburgerContentClosed");
});   
   
$('#hamburgerCloseButton').click(function() {
   $('#hamburgerContent').addClass("hamburgerContentClosed"); 
   $('#hamburgerContent').removeClass("hamburgerContentOpen");
});

$('.hamburgerLinks a').click(function() {   
   $('#hamburgerContent').addClass("hamburgerContentClosed"); 
   $('#hamburgerContent').removeClass("hamburgerContentOpen");
});


