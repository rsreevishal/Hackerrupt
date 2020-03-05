var firebaseConfig = {
	apiKey: "AIzaSyAsbSfe9NzDga5PnSUwpIlK3VLvHtQumtY",
	authDomain: "hackerrupt2k20-404ae.firebaseapp.com",
	databaseURL: "https://hackerrupt2k20-404ae.firebaseio.com",
	projectId: "hackerrupt2k20-404ae",
	storageBucket: "hackerrupt2k20-404ae.appspot.com",
	messagingSenderId: "178516608596",
	appId: "1:178516608596:web:dc2450cbb1f67f41048fc1",
	measurementId: "G-6776NLM3ZX"
  };
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
  firebase.auth().languageCode = 'en';
  const DB = firebase.firestore();
  var verified = false;
  window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container', {
	'size': 'normal',
	'callback': function(response) {
	  verified = true;
	},
	'expired-callback': function() {
	}
  });
  recaptchaVerifier.render().then(function(widgetId) {
	window.recaptchaWidgetId = widgetId;
  });
  if(document.getElementById('t1')) {
		if(document.getElementById("absum").value.length < 10){
			document.getElementById("submit").disabled = true;
		}
		$("#absum").on('keyup',()=>{
			if(document.getElementById("absum").value.length < 10){
				document.getElementById("submit").disabled = true;
			}else{
				document.getElementById("submit").disabled = false;
			}
		});
	  $("#t2").css("display","none");
	  $("#t3").css("display","none");
	  $("#t4").css("display","none");
	  $('#team_no').on('keyup change',(e)=>{
		  switch(e.target.value) {
				case '':
				case '1': {
					$("#t2").css("display","none");
					$("#t3").css("display","none");
					$("#t4").css("display","none");
					break;
				}
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
					alert('no more than 4 members allowed');
					document.getElementById("submit").disabled = true;
			  }
		  }
	  });
	  $('#pass, #cpass').on('keyup', function () {
			if (($('#pass').val() == $('#cpass').val()) and (document.getElementById("pass").value.length >= 8)) {
			  $('#message').html('Matching').css('color', 'green');
			  $('#submit').attr('disabled',false);
			} else {
			  $('#message').html('Not Matching').css('color', 'red');
			  $('#submit').attr('disabled',true);
		  }
		});
		
  }
  //if(document.getElementById('ab_link')) {
	 // $('#ab_link').on('click',(e)=>{
	//	  alert('1. This field is optional\n2. This link should be a google drive link');
	 // });
 // }
  // if(document.getElementById('submit')) {
  // 	$('#submit').on('click',(e) => {
  //         if(verified) {
  //             console.log('registered');
  //             console.log($('#myForm').serializeJSON());
  //         }
  // 	});
  // }
  
  // $('#otp').on('click',() => {
  //     var phoneNumber = document.getElementById('mobile').value;
  //     console.log(phoneNumber);
  //     var appVerifier = window.recaptchaVerifier;
  //     firebase.auth().signInWithPhoneNumber(phoneNumber, appVerifier)
  //     .then(function (confirmationResult) {
  //         alert('OTP sent to your mobile successfully');
  //         window.confirmationResult = confirmationResult;
  //         confirmresult = confirmationResult;
  //     }).catch(function (error) {
  //         alert('Some error occured try again');
  //         grecaptcha.reset(window.recaptchaWidgetId);
  //         console.log(error);
  //     });
  // });
  $.fn.serializeObject = function()
  {
	  var o = {};
	  var a = this.serializeArray();
	  $.each(a, function() {
		  if (o[this.name] !== undefined) {
			  if (!o[this.name].push) {
				  o[this.name] = [o[this.name]];
			  }
			  o[this.name].push(this.value || '');
		  } else {
			  o[this.name] = this.value || '';
		  }
	  });
	  return o;
  };
  
  
  $('#submit').on('click',function() {
	  if((verified) and (document.getElementById("pass").value.length >= 8)) {
		  var res = JSON.stringify($('#myForm').serializeObject());
			var data = JSON.parse(res);
			document.getElementById("submit").disabled = true;
			var pass = document.getElementById("pass").value;
		  signUp(data.email,pass,data);
	  } else if(verified) {
	  	alert("Check the password to be minimum of 8 chars");
	  }
	  else{
	  	alert("Verify recaptcha");
	  }
  });
  
  async function signUp(email, pass, data) {
	  await firebase.auth().createUserWithEmailAndPassword(email, pass).then(cred => {
		if (data) {
		  return DB.collection('users').doc(cred.user.uid).set(data).then(() => {
				alert('Registered');
				$.post( "http://localhost:3000/mailto/", { email: email }, function(data){
					console.log(data);
				} );
			  window.location.href = "success.html";
		  });
		}
		
	  }).catch(err => {
		if (err) {
		  alert('Error occured this mail is already registered or server error try again later.');
			window.location.href = "index.html";
		}
	  });
	}
  
