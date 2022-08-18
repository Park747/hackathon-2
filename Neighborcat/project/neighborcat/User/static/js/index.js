// 📁 index.js
import { openModal, closeModal } from "./modal.js";
import { setCookie, getCookie } from "./cookie.js";

// JS에서 DOM element 가져올 때 관용적으로 $표시를 사용한다.
// $표시로 DOM element return해서 반복 줄이는 함수
const $ = (selector) => document.querySelector(selector);


$(".btn-open-modal").addEventListener("click", () => {
    openModal();
});

$(".modal-container").addEventListener("click", (event) => {
    if (event.target === $(".modal-container")) {
        closeModal();
    }
});

$(".modal-close").addEventListener("click", () => {
    closeModal();
});

// 오늘 보지 않기 버튼을 누르면 만료기간이 1일인 쿠키를 생성하고 모달을 닫는다.
$(".modal-stop-button").addEventListener("click", () => {
    // 하루 기한의 쿠키를 생성한다. (쿠키 생성시 이름은 modal-closed, 값은 true로 설정한다.)
    // 모달을 닫는다.
    closeModal();
    setCookie("modalClose", "true", 1);
});

let checkCookie = getCookie("modalClose");

if (checkCookie == 'true') {
    closeModal();
} else {
    openModal();
}