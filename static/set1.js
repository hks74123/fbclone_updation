document.getElementById('lgnnn11').addEventListener('click',login_check)
  async function login_check(){
    document.getElementById('lgnnn11').style.display='none';
    document.getElementById("uname").disabled=true;
    document.getElementById("upss").disabled=true;
    document.getElementById('mails').disabled=true; 
    document.getElementById('loadin_btn1').style.display='';
    let response = await fetch('/verifymail', {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "username": document.getElementById("uname").value,
            "pass": document.getElementById("upss").value,
            "email":document.getElementById("mails").value
        })
    })
    if(response.ok){
        let json = await response.json();
        let message = json["message"];
        if(message=='Verification link has been sent to your email please check inbox!!'){
            window.location.replace('/lgnp');
        }
        else{
            document.getElementById("uname").disabled=false;
            document.getElementById("upss").disabled=false;
            document.getElementById('mails').disabled=false; 
            document.getElementById('loadin_btn1').style.display='none';
            document.getElementById('lgnnn11').style.display='';
            document.getElementById('msbx').style.display='block';
            document.getElementById('msgss').innerHTML=message;
        }
    }
    else{
        log='Server time out';
        document.getElementById('msbx').style.display='block';
        document.getElementById('msgss').innerHTML=log;
        document.getElementById("uname").disabled=false;
        document.getElementById("upss").disabled=false;
        document.getElementById('mails').disabled=false; 
        document.getElementById('loadin_btn1').style.display='none';
        document.getElementById('lgnnn11').style.display='';
    }
}