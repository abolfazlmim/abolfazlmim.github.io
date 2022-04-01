const modal = document.querySelector('#modal')
const openBtn = document.querySelector('#open-btn');
const closeBtn = document.querySelector('#close-btn');

openBtn.addEventListener('click', () => {
  modal.showModal();
})
closeBtn.addEventListener('click', () => {
  modal.close();
})
