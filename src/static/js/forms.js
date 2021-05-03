//Post input
const description = document.getElementById("id_description");
description.classList.add("form-control");

const form = document.querySelector("form");

const file = document.getElementById("id_image");
const p = file.parentElement;
p.classList.add("mb-3");
p.children[0].classList.add("custom-file-label");
file.classList.add("custom-file-input");
p.classList.add("custom-file");
