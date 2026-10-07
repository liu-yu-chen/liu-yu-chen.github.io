/* Navigation and gallery enhancements. All primary content works without JS. */
document.documentElement.classList.add('js');
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-nav');
function closeMenu() {
  menuButton?.setAttribute('aria-expanded', 'false');
  navigation?.classList.remove('is-open');
}
menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('is-open', open);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuButton?.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menuButton.focus();
  }
});
document.addEventListener('click', event => {
  if (!event.target.closest('.site-header')) closeMenu();
});
window.matchMedia('(min-width: 901px)').addEventListener('change', closeMenu);
if (document.querySelector('.splide') && window.Splide) {
  const labels = document.querySelector('script[data-prev]').dataset;
  new Splide('.splide', {
    type: 'fade', rewind: true, autoplay: false, arrows: true,
    pagination: true, speed: 650, keyboard: 'focused',
    reducedMotion: { speed: 0, autoplay: false },
    i18n: { prev: labels.prev, next: labels.next, slideX: labels.slide, pageX: labels.page }
  }).mount();
}
const lightbox = document.querySelector('#photo-lightbox');
if (lightbox) {
  let previousFocus;
  document.querySelectorAll('[data-photo]').forEach(button => {
    button.addEventListener('click', () => {
      previousFocus = button;
      const photo = lightbox.querySelector('img');
      photo.src = button.dataset.photo;
      photo.alt = button.dataset.caption || '';
      lightbox.querySelector('figcaption').textContent = button.dataset.caption || '';
      lightbox.showModal();
    });
  });
  lightbox.querySelector('button').addEventListener('click', () => lightbox.close());
  lightbox.addEventListener('click', event => { if (event.target === lightbox) lightbox.close(); });
  lightbox.addEventListener('close', () => previousFocus?.focus());
}
