if(document.getElementById('t1')) {
	$("#t2").css("display","none");
	$("#t3").css("display","none");
	$("#t4").css("display","none");
	$('#team_no').on('keyup change',(e)=>{
		switch(e.target.value) {
			case '2': {
				$("#t2").css("display","block");
				$("#t3").css("display","none");
				$("#t4").css("display","none");
				break;
			}
			case '3': {
				$("#t2").css("display","block");
				$("#t3").css("display","block");
				$("#t4").css("display","none");
				break;
			}
			case '4': {
				$("#t2").css("display","block");
				$("#t3").css("display","block");
				$("#t4").css("display","block");
				break;
			}
			default: {
				$("#t2").css("display","none");
				$("#t3").css("display","none");
				$("#t4").css("display","none");
			}
		}
	});
	$('#pass, #cpass').on('keyup', function () {
  		if ($('#pass').val() == $('#cpass').val()) {
    		$('#message').html('Matching').css('color', 'green');
			$('#submit').attr('disabled',false);
  		} else {
    		$('#message').html('Not Matching').css('color', 'red');
			$('#submit').attr('disabled',true);
		}
	});
}
if(document.getElementById('ab_link')) {
	$('#ab_link').on('click',(e)=>{
		alert('1. This field is optional\n2. This link should be a google drive link');
	});
}