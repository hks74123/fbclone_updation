document.getElementById('lgnnn').addEventListener('click',usercheck)
document.getElementById('lgnnn11').addEventListener('click',login_check)

async function usercheck() {
    document.getElementById('lgnnn').style.display='none';
    document.getElementById('lgnnn1').style.display='none';
    document.getElementById("f_name").disabled=true;
    document.getElementById("l_name").disabled=true;
    document.getElementById("u_name").disabled=true;
    document.getElementById("mmail").disabled=true;
    document.getElementById("pass").disabled=true;
    document.getElementById("pass1").disabled=true;
    document.getElementById('loadin_btn').style.display=''
    let response = await fetch('/signup', {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "fname": document.getElementById("f_name").value,
            "lname": document.getElementById("l_name").value,
            "username": document.getElementById("u_name").value,
            "email": document.getElementById("mmail").value,
            "pass": document.getElementById("pass").value,
            "pass1": document.getElementById("pass1").value
        })
    })
    if(response.ok){
        let json = await response.json();
        let message = json["message"];
        if (message == 'Verification link has been sent to your email please check inbox!!') {
            document.getElementById('msbx').style.display='block';
            window.location.replace('/lgnp');
    }
        else{
            document.getElementById("f_name").disabled=false;
            document.getElementById("l_name").disabled=false;
            document.getElementById("u_name").disabled=false;
            document.getElementById("mmail").disabled=false;
            document.getElementById("pass").disabled=false;
            document.getElementById("pass1").disabled=false;
            document.getElementById('loadin_btn').style.display='none';
            document.getElementById('lgnnn').style.display='';
            document.getElementById('lgnnn1').style.display='';
            document.getElementById('msbx').style.display='block';
            document.getElementById('msgss').innerHTML=message;
        }
    }
    else{
        log='Server time out'
        document.getElementById("f_name").disabled=false;
        document.getElementById("l_name").disabled=false;
        document.getElementById("u_name").disabled=false;
        document.getElementById("mmail").disabled=false;
        document.getElementById("pass").disabled=false;
        document.getElementById("pass1").disabled=false;
        document.getElementById('loadin_btn').style.display='none';
        document.getElementById('lgnnn').style.display='';
        document.getElementById('lgnnn1').style.display='';
        document.getElementById('msbx').style.display='block';
        document.getElementById('msgss').innerHTML=log;
    }
}

async function login_check(){
    document.getElementById('lgnnn11').style.display='none';
    document.getElementById('lgnnn12').style.display='none';
    document.getElementById('fg_ps').style.display='none';
    document.getElementById('lgotp').style.display='none';
    document.getElementById("uname").disabled=true;
    document.getElementById("upss").disabled=true;
    document.getElementById('loadin_btn1').style.display='';
    let response = await fetch('/login', {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "username": document.getElementById("uname").value,
            "pass": document.getElementById("upss").value
        })
    })
    if(response.ok){
        let json = await response.json();
        let message = json["message"];
        if(message=='success'){
            window.location.replace('/');
        }
        else{
            document.getElementById("uname").disabled=false;
            document.getElementById("upss").disabled=false;
            document.getElementById('loadin_btn1').style.display='none';
            document.getElementById('lgnnn11').style.display='';
            document.getElementById('lgnnn12').style.display='';
            document.getElementById('fg_ps').style.display='';
            document.getElementById('lgotp').style.display='';
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
        document.getElementById('loadin_btn1').style.display='none';
        document.getElementById('lgnnn11').style.display='';
        document.getElementById('lgnnn12').style.display='';
        document.getElementById('fg_ps').style.display='';
        document.getElementById('lgotp').style.display='';
    }
}