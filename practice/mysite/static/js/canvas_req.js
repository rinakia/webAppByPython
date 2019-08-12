

document.getElementById("hello_text").textContent = "0〜9の数字を1つ書いてください";
// document.getElementById("check_img").textContent = "non-exist";

// テキストボックスの文字を取得する
function req(){
    
    if(document.js.txtb.value == ""){ // 「お名前」の入力をチェック

        window.alert('名前が未入力です'); // 入力漏れがあれば警告ダイアログを表示
        return false; // 送信を中止

    }else{
    
    var canvas = document.getElementById('canvas');
    var str1=document.js.txtb.value; // form name: js
    alert("ようこそ"+str1+"さん！");

    var fileName = "img1/sample.png";
    var img1 = canvas.toDataURL(); // デフォpng
    document.getElementById("newImg").src = img1;
    document.getElementById("check_img").textContent = "exist";
    
    // var blob = toBlob(img1)
    // window.navigator.msSaveBlob(img1, fileName)
    // base64
        
       // return true;
    }
}

/*
// Base64 to バイナリ to Blob
function toBlob(base64){
    // Base64からバイナリへ変換
    var bin = atob(base64.replace(/^.*,/, ''));
    var buffer = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) {
        buffer[i] = bin.charCodeAt(i);
    }
    // Blobを作成
    var blob = new Blob([buffer.buffer], {
        type: type
    });
    return blob;
}
*/


//テキストボックスの文字を操作する
function clr(){
    var canvas = document.getElementById('canvas');
    var con = canvas.getContext('2d');

    // document.js.txtb.value="";
    con.clearRect(0, 0, canvas.width, canvas.height);
  
  }

