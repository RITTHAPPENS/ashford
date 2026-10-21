// Header: Schatten erst nach dem ersten Scrollen (IntersectionObserver statt Scroll-Listener)
const header = document.getElementById('header');
const sentinel = document.createElement('div');
sentinel.style.cssText = 'position:absolute;top:0;height:1px;width:1px';
document.body.prepend(sentinel);
new IntersectionObserver(([e]) => header.classList.toggle('is-scrolled', !e.isIntersecting)).observe(sentinel);

// Mobiles Menü
const burger = document.getElementById('burger'), nav = document.getElementById('nav');
const setMenu = open => { nav.classList.toggle('is-open', open); burger.classList.toggle('is-open', open); burger.setAttribute('aria-expanded', open); };
burger.addEventListener('click', () => setMenu(!nav.classList.contains('is-open')));
nav.querySelectorAll('a:not(.dd__toggle)').forEach(a => a.addEventListener('click', () => setMenu(false)));
document.querySelector('.dd__toggle')?.addEventListener('click', e => {
  if (innerWidth <= 1100) { e.preventDefault(); e.currentTarget.parentElement.classList.toggle('is-open'); }
});

// Einblenden beim Scrollen
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { threshold: .12, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Zähler bei den Kennzahlen
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const co = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  const el = e.target, end = +el.dataset.count, t0 = performance.now(), d = 1400;
  co.unobserve(el);
  if (reduce) return;
  const tick = t => { const p = Math.min((t - t0) / d, 1); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 4))).toLocaleString('de-DE'); if (p < 1) requestAnimationFrame(tick); };
  requestAnimationFrame(tick);
}), { threshold: .6 });
document.querySelectorAll('[data-count]').forEach(el => co.observe(el));

// Lightbox
const lb = document.getElementById('lightbox');
if (lb) {
  const img = document.createElement('img'); lb.appendChild(img);
  document.querySelectorAll('.gallery a').forEach(a => a.addEventListener('click', e => {
    e.preventDefault(); img.src = a.href; img.alt = a.querySelector('img')?.alt || ''; lb.classList.add('is-open'); lb.querySelector('button').focus();
  }));
  lb.addEventListener('click', () => lb.classList.remove('is-open'));
  addEventListener('keydown', e => { if (e.key === 'Escape') lb.classList.remove('is-open'); });
}

// Hinweis-Toast
const toast = document.getElementById('toast');
const show = msg => { toast.textContent = msg; toast.classList.add('is-on'); clearTimeout(show.t); show.t = setTimeout(() => toast.classList.remove('is-on'), 3600); };

// Formular (Prototyp)
const form = document.getElementById('form');
form?.addEventListener('submit', e => {
  e.preventDefault();
  if (!form.checkValidity()) { form.reportValidity(); return; }
  show('Prototyp: Das Formular wird bei der Umsetzung in WordPress angebunden.');
});

// Video erst nach Klick von YouTube laden
const vid = document.getElementById('video');
if (vid) {
  const load = () => {
    if (vid.querySelector('iframe')) return;
    const f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + vid.dataset.yt + '?autoplay=1&rel=0';
    f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; f.allowFullscreen = true; f.title = 'Anwendungsvideo Ashford Formula';
    vid.appendChild(f); vid.style.cursor = 'default';
  };
  vid.addEventListener('click', load);
  vid.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); load(); } });
}
