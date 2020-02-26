const express = require('express');
const nodemailer = require("nodemailer");
const fs = require('fs');
async function main(fromMail,toMail,sub,message) {
  let testAccount = await nodemailer.createTestAccount();
  console.log(testAccount.user);
  console.log(testAccount.pass);
  let transporter = nodemailer.createTransport({
    host: "smtp.gmail.com",
    port: 587,
    secure: false, // true for 465, false for other ports
    auth: {
      user: "hackerrupt2k20@gmail.com", // generated ethereal user
      pass: "rsree112001" // generated ethereal password
    }
  });
  let info = await transporter.sendMail({
    from: fromMail, // sender address
    to: toMail, // list of receivers
    subject: sub, // Subject line
    //text: "Hello world?", // plain text body
    html: message // html body
  });

  console.log("Message sent: %s", info.messageId);
  console.log("Preview URL: %s", nodemailer.getTestMessageUrl(info));
}



fs.readFile("./mailing.html",(err,data) => {
  if(err)
    console.log(err);
  if(data){
    const html = data;
    main('"Hackerrupt Team" <hackerrupt2k20@gmail.com>',"rsreevishal111@gmail.com","Hackerrupt\'20",html).catch(console.error);
  }
});




