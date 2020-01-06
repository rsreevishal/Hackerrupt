const express = require('express')
const path = require('path') 
const app = express()

app.use('/assets',express.static(path.join(__dirname,'assets')));

app.get('/',(req,res) => {
    res.sendFile(path.join(__dirname,'index.html'));
})

app.get('/signin',(req,res) => {
    res.sendFile(path.join(__dirname,'signin.html'));
})

app.get('/signup',(req,res) => {
    res.sendFile(path.join(__dirname,'signup.html'));
})

app.get('/aboutACE',(req,res) => {
    res.sendFile(path.join(__dirname,'aboutACE.html'));
})
app.listen(3000,()=> {
    console.log('listening');
})