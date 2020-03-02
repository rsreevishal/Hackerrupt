const express = require('express');
const nodemailer = require("nodemailer");
const fs = require('fs');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.json());
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

app.post('/mailto',(req,res) => {
  const tomail = req.body.email;
  console.log(req.body);
  if(req.body.email){
    fs.readFile("./mailing.html",(err,data) => {
      if(err){
        console.log(err);
        req.end('error');
      }
      if(data){
        const html = data;
        main('"Hackerrupt Team" <hackerrupt2k20@gmail.com>',tomail,"Hackerrupt\'20",html).catch(console.error);
        res.end('sent');
      }
    });
  }
  else {
    res.end('cannot get email address');
  }
});

app.listen(3000,()=>{
  console.log('listening at port 3000');
});


