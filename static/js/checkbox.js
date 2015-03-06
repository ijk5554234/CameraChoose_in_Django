var checknum = 0;
var realclick = false;
function a(){
	$("#cm1").attr("disabled",false);
	$("#cm2").attr("disabled",false);
}
$("div#checkboxes div.checkbox>label").click(function(){
	if(!realclick){
		realclick = true;
		return;
	}
	else{
		realclick = false;
	}
	var checkbox = $(this).children("input");
	if (checkbox.attr("disabled"))
		return;
	if (!checkbox.hasClass("checked")){
		checkbox.addClass("checked");
		checknum++;
		if(checknum==1){
			$("#cm1").val($(this).text());
			$("#cm1").attr("disabled",true);
		}
		else if(checknum==2){
			$("#cm2").val($(this).text());
			$("#cm2").attr("disabled",true);
			$("div.checkbox>label>input").attr("disabled",true);
			checkbox.attr("disabled",false);
		}
	}
	else{
		checkbox.removeClass("checked");
		checknum--;
		if(checknum==0){
			$("#cm1").val("");
			$("#cm1").attr("disabled",false);
		}
		else if(checknum==1){
			$("#cm2").val("");
			$("#cm2").attr("disabled",false);
			$("div.checkbox>label>input").attr("disabled",false);
		}
	}
});