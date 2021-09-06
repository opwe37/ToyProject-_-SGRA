const PORT = "7777";
const COMMENT_CREATE_URL = 'http://127.0.0.1:'+PORT+'/comment/create/';
const COMMENT_UPDATE_URL = 'http://127.0.0.1:'+PORT+'/comment/update/__target__';


// 게시글의 댓글 작성
const comment_cancel_btn = document.querySelector('.comment-cancel');
comment_cancel_btn.addEventListener('click', e => {
  e.target.parentNode.hidden = true;
  document.querySelector('.public-comment-input').innerHTML = '';
});

const textArea = document.querySelector('.public-comment-input');
textArea.addEventListener('focusin', (e) => {
  const btn = document.querySelector('.public-comment-btn');
  btn.hidden = false;
});

// 요거 설정이 되야 button이 동작해요.
function submitComment(article_pk) {
    console.log("test")
    const data = {};
    const input = document.querySelector('.public-comment-input');
    if (input.innerText.trimEnd() == '') {    // 보낼 데이터가 없다면
        input.innerHTML = "";
        input.focus();
        return;
    }

    data['content'] = input.innerHTML;
    data['article_pk'] = article_pk;
    data['secret'] = document.querySelector(".public-comment-btn input[type='checkbox']").checked;

    sendDataPost(COMMENT_CREATE_URL, data);
}


function submitCommentReply(parent_pk, article_pk, target_comment=parent_pk) {
    const data = {};
    console.log(target_comment)
    const input = document.querySelector(`div[data-key="${target_comment}"] .reply-container .comment-reply-input`);
    if (input.innerText.trimEnd() == '') {    // 보낼 데이터가 없다면
        input.innerHTML = "";
        input.focus();
        return;
    }

    data['content'] = input.innerHTML;
    data['parent_pk'] = parent_pk;
    data['secret'] = false;
    data['article_pk'] = article_pk;

    sendDataPost(COMMENT_CREATE_URL, data);
}

function submitCommentUpdate(comment_pk) {
  const data = {};

  const form = document.querySelector(`div[data-key="${comment_pk}"] .edit-dialog`);

  data['content'] = form.querySelector(`.comment-reply-input`).innerHTML;
  data['secret'] = form.querySelector(`input[type='checkbox']`).checked;

  sendDataPost(COMMENT_UPDATE_URL.replace('__target__', comment_pk), data);
}

function createEditDialog(content, commentId, secret) {
  let template = `
    <div>
      <div class="comment-reply-input" contenteditable="True">__content__</div>
      <div>
        <label><input type="checkbox" name="secret" __checked__></input> 비밀 댓글</label>
        <a onclick="commentEditCancel(__commentId__)">취소</a>
        <a onclick="submitCommentUpdate(__commentId__)">저장</a>
      </div>
    </div>
  `;

  const defaultSelector = `div.comment-item[data-key="${commentId}"] `;

  const body = document.querySelector(defaultSelector + '> .comment');
  body.hidden = true;

  const editSelector = document.querySelector(defaultSelector + '.edit-dialog');
  editSelector.innerHTML = '';
  template = template.replace("__content__", content);
  template = template.replaceAll("__commentId__", commentId);
  template = template.replace("__secret__", secret == 'True' ? "checked" : "");
  editSelector.innerHTML = template;
  editSelector.hidden = false;
}

function commentEditCancel(commentId) {
  const defaultSelector = `div.comment-item[data-key="${commentId}"] `;

  const body = document.querySelector(defaultSelector + '> .comment');
  body.hidden = false;

  const editDialog = document.querySelector(defaultSelector + '.edit-dialog');
  editDialog.hidden = true;
}

// 답글 버튼 클릭 시, 댓글 작성 Dialog 활성화
const reply_btns = document.querySelectorAll('.reply-btn');
for (const reply_btn of reply_btns){
    reply_btn.addEventListener('click', e => {
        const btn_parent = e.target.parentNode;
        const dialog = btn_parent.querySelector('.reply-dialog');

        if (dialog.hidden) {
            dialog.hidden = false;
        } else {
            const input = dialog.querySelector('.comment-reply-input');
            input.focus();
        }
    });
}

// 답글 취소 클릭 시, 댓글 작성 Dialog 비활성화
const reply_cancel_btns = document.querySelectorAll('.reply-cancel');
for (const reply_cancel_btn of reply_cancel_btns){
    reply_cancel_btn.addEventListener('click', e => {
        const dialog = e.target.closest('.reply-dialog');

        const input = dialog.querySelector('.comment-reply-input');
        input.innerText = "";

        dialog.hidden = true;
    });
}

// 답글 제출 클릭 시, 작성한 댓글 전송
const reply_submit_btns = document.querySelectorAll('.reply-submit');
for (const reply_submit_btn of reply_submit_btns){
    reply_submit_btn.addEventListener('click', e => {
        const dialog = e.target.closest('.reply-dialog');

        const input = dialog.querySelector('.comment-reply-input');
        if (input.innerText.trimEnd() == '') {
            input.focus();
        } else {
            dialog.hidden = true;
        }
    });
}