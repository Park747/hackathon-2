// π modal.js
// λͺ¨λ¬ κ΄λ ¨ ν¨μλ€μ μ μνκ³  λ΄λ³΄λΈλ€.

const $ = (selector) => document.querySelector(selector);
const body = $("body");
const modal = $(".modal-container");

const openModal = () => {
    modal.classList.add("open");
    body.style.overflow = "hidden";
};

const closeModal = () => {
    modal.classList.remove("open");
    body.style.overflow = "auto";
};

export { openModal, closeModal };
