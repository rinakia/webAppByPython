/**
 * https://teratail.com/questions/11714
 * canvas の値を他のinput同様にgetする
 *  Internet Explorer 10 以上
 * Google Chrome 20 以上
 * Safari 6 以上
 * Firefox 13 以上
 * Opera 12.1 以上
 * 
 * HTMLCanvasElement.toBlobの互換関数。
 * toBlobメソッドとほぼ同等の動作を行う。
 * 対応していない場合、コールバック関数の引数にはnullが返される。
 *
 * @param {Node} canvas canvas要素のDOMノード
 * @param {function((Blob|null))} callback コールバック関数。第一引数に、生成したBlobオブジェクト、またはnullが渡される
 * @param {string=} type 画像形式の文字列
 * @link https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob#Polyfill
 */
function canvasToBlob(canvas, callback, type) {
    if (!type) {
        type = 'image/png';
        // type = 'image/jpg';
    }

    if (canvas.toBlob) {
        canvas.toBlob(callback, type);
    } else if (canvas.toDataURL && window.Uint8Array && window.Blob && window.atob) {
        var binStr = atob(canvas.toDataURL(type).replace(/^[^,]*,/, '')), //
        len = binStr.length,
        arr = new Uint8Array(len);

        for (var i = 0; i < len; i++) {
            arr[i] = binStr.charCodeAt(i);
        }

        callback(new Blob([arr], { type: type }));
    } else {
        callback(null);
    }
}

/**
 * canvas画像の送信処理
 *
 * @param {Element} formElem フォームのDOMノード
 */
function send(formElem) {
    var canvasElem = document.getElementById('canvas');

    if (window.FormData) {
        /**
         * FormDataオブジェクトに対応している場合、
         * canvas要素の画像をBlobオブジェクトに変換し、
         * ファイルとして送信することを試みる
         */
        canvasToBlob(canvasElem, function (canvasBlob) {
            if (canvasBlob) {
                /**
                 * canvas要素の画像をBlobオブジェクトとして出力できた場合、
                 * FormDataオブジェクトにファイルとして追加し、送信
                 */

                /**
                 * FormDataオブジェクトを生成
                 */
                var fd = new FormData(formElem);
                /**
                 * Blobオブジェクトを追加。
                 * これにより、サーバ側ではcanvas-imageパラメータから
                 * 画像ファイルとして取り込める
                 */
                fd.append('canvas', canvasBlob);

                /**
                 * XMLHttpRequestオブジェクトを生成
                 */
                var xhr = new XMLHttpRequest();

                // -------------------------
                // Ajax通信完了時の処理などを記述…
                // -------------------------

                /**
                 * Ajax通信の送信先・送信形式を指定
                 * この例では、送信先としてフォームのaction属性値を使用
                 */
                // xhr.open('POST', formElem.action, true);
                xhr.open('GET', formElem.action, true);

                /**
                 * FormDataオブジェクトをAjax送信
                 */
                xhr.send(fd);
            } else {
                /**
                 * canvas要素の画像をBlobオブジェクトとして出力できなかった場合、
                 * 送信できなかった事をアラート
                 */
                alert('canvasの内容を送信できませんでした。\nお使いのブラウザは、Blobオブジェクトの生成に必要な機能に対応していません。');
            }
        }, 'image/png');
    } else {
        /**
         * FormDataオブジェクトに対応していない場合、
         * 送信できない事をアラート
         */
        alert('canvasの内容を送信できませんでした。\nお使いのブラウザは、FormDataオブジェクトに対応していません。');
    }
}

/**
 * フォームが送信される時に実行する処理
 */
document.getElementById('form').addEventListener('submit', function (e) {
    /**
     * フォームの要素を取得
     */
    var formElem = this;

    /**
     * フォームの送信をキャンセル
     */
    e.preventDefault();

    /**
     * フォームをAjax送信
     */
    send(formElem);
}, false);