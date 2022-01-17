console.log("testing");
var model={
    
};
var view={
    slider : document.getElementById("skill_level"),
    rankSpan : document.getElementById("rank"),
    skillList : document.getElementById("list")
};
var controller = {
    init : function(){
        // need to make a request to get all the skills of rank1
        // and put them in the listStyleType
        // then add an event listener to the slider
        view.slider.addEventListener("change",controller.sliderAdjusted);
        
        
    },
    sliderAdjusted : function(){
      // need to clear all the lis there are from the ul
      // need to get the value of the slider
      model.value = view.slider.value;

      // need to set the span value to that value
      view.rankSpan.textContent = model.value;
      
      // need to make a request to get all skills of that rank
      // need to create the lis of the list with each skill        
    }
};

controller.init();