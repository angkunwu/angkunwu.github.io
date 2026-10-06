'use strict';
const controls = document.querySelector('.publication-controls');
const papers = [...document.querySelectorAll('.publication')];
const search = document.querySelector('#publication-search');
const filters = [...document.querySelectorAll('[data-filter]')];
let selectedType = 'all';
function filterPapers() {
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  papers.forEach(paper => {
    const matches = (selectedType === 'all' || paper.dataset.type === selectedType) && paper.textContent.toLocaleLowerCase().includes(query);
    paper.hidden = !matches;
    if (matches) count++;
  });
  document.querySelector('#publication-count').textContent = `${count} of ${papers.length} publications`;
  document.querySelector('#publication-empty').hidden = count !== 0;
}
if (controls && search) {
  controls.hidden = false;
  filters.forEach(button => button.addEventListener('click', () => {
    selectedType = button.dataset.filter;
    filters.forEach(filter => {
      const active = filter === button;
      filter.classList.toggle('active', active);
      filter.setAttribute('aria-pressed', String(active));
    });
    filterPapers();
  }));
  search.addEventListener('input', filterPapers);
  filterPapers();
}
