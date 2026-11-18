/* Markeer de zoekwoorden op de bestemmingspagina, zonder bron-Markdown te wijzigen. */
(function () {
  function markSearch() {
    const raw = new URLSearchParams(location.search).get('highlight') || '';
    const terms = [...new Set(raw.trim().split(/\s+/).filter(Boolean))];
    if (!terms.length) return;
    const root = document.querySelector('article.md-content__inner');
    if (!root) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        const el = node.parentElement;
        if (!el || !node.nodeValue.trim() || el.closest('a,code,pre,script,style,mark'))
          return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    const nodes = []; while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const node of nodes) {
      const original = node.nodeValue, lower = original.toLocaleLowerCase();
      let pos = 0, changed = false;
      const frag = document.createDocumentFragment();
      while (pos < original.length) {
        let at = -1, match = '';
        for (const term of terms) {
          const found = lower.indexOf(term.toLocaleLowerCase(), pos);
          if (found >= 0 && (at < 0 || found < at || (found === at && term.length > match.length))) {
            at = found; match = term;
          }
        }
        if (at < 0) { frag.append(document.createTextNode(original.slice(pos))); break; }
        frag.append(document.createTextNode(original.slice(pos, at)));
        const mark = document.createElement('mark');
        mark.textContent = original.slice(at, at + match.length);
        frag.append(mark); pos = at + match.length; changed = true;
      }
      if (changed) node.replaceWith(frag);
    }
  }
  function enableImageLightbox() {
    const root = document.querySelector('article.md-content__inner');
    if (!root || document.querySelector('.rm-lightbox')) return;
    const overlay = document.createElement('div');
    overlay.className = 'rm-lightbox';
    overlay.hidden = true;
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-label', 'Afbeelding vergroot');
    overlay.setAttribute('aria-modal', 'true');
    const image = document.createElement('img');
    image.className = 'rm-lightbox-image';
    const close = document.createElement('button');
    close.type = 'button';
    close.className = 'rm-lightbox-close';
    close.setAttribute('aria-label', 'Sluiten');
    close.textContent = '×';
    overlay.append(image, close);
    document.body.appendChild(overlay);
    let previousFocus = null;
    function hide() {
      overlay.hidden = true;
      image.removeAttribute('src');
      if (previousFocus) previousFocus.focus();
    }
    close.addEventListener('click', hide);
    overlay.addEventListener('click', event => {
      if (event.target === overlay) hide();
    });
    document.addEventListener('keydown', event => {
      if (!overlay.hidden && event.key === 'Escape') hide();
    });
    root.querySelectorAll('img').forEach(img => {
      if (!img.getAttribute('src') || img.closest('a')) return;
      img.tabIndex = 0;
      img.setAttribute('role', 'button');
      img.setAttribute('aria-label', 'Vergroot afbeelding: ' + (img.alt || 'afbeelding'));
      function open() {
        previousFocus = document.activeElement;
        image.src = img.currentSrc || img.src;
        image.alt = img.alt || '';
        overlay.hidden = false;
        close.focus();
      }
      img.addEventListener('click', open);
      img.addEventListener('keydown', event => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault(); open();
        }
      });
    });
  }
  function init() { markSearch(); enableImageLightbox(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
