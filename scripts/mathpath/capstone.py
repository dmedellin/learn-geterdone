"""Theme tokens for the two authored capstone layouts.

The Trading patcher owns the migration and this renewable palette. Component
rules keep their authored layout and hierarchy and consume the same tokens in
both light paths.
"""
import re
from html import escape, unescape

BEGIN = '/* capstone-palette:begin */'
END = '/* capstone-palette:end */'
LIGHT = '--capstone-accent: #08616e; --capstone-muted: #425767; --on-accent: #ffffff;'
PALETTE = '''%s
:root { --capstone-accent: #98f5ff; --capstone-muted: #aec1d2; --on-accent: #041116; }
body { --muted: var(--capstone-muted); }
/* Each wrapped gradient fragment owns enough paint area for glyph overhang. */
body[data-page-kind="supplemental"] .gradient { padding: .1em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
%s
''' % (BEGIN, END)


def normalize_palette(text):
    text = re.sub(r'[ \t]*' + re.escape(BEGIN) + r'.*?' + re.escape(END) + r'\n?', '', text, flags=re.S)
    # Only authored stylesheet declarations: never script colors, data or copy.
    start = text.index('<style>') + len('<style>')
    marker = text.index('/* progress-marks:begin */', start)
    end = text.rfind('\n', start, marker) + 1
    authored = text[start:end]
    authored = re.sub(r'--cyan2\s*:[^;}]+', '--cyan2:var(--capstone-accent)', authored)
    authored = re.sub(r'(?<![-\w])color\s*:\s*#041116\b', 'color:var(--on-accent)', authored)
    authored = authored.replace('color:var(--capstone-muted)', 'color:var(--muted)')
    def light(match):
        body = re.sub(r'[ \t]*(?:--capstone-(?:accent|muted)|--on-accent)\s*:[^;]+;', '', match[2]).rstrip()
        return match[1] + body + '\n    ' + LIGHT + '\n  }'
    authored = re.sub(r'((?::root:not\(\[data-theme="dark"\]\)|\[data-theme="light"\])\s*\{)([^}]*)\}', light, authored)
    return text[:start] + PALETTE + authored + text[end:]


# These regions own navigation and accessible scroll owners. The authored chart
# functions, slide content, DATA and print layout remain in the document.
DECK_SCROLLBAR = '''/* deck-scrollbar:begin */
@media screen {
  body[data-page-kind="slides"] .slide { scrollbar-gutter: stable; }
  body[data-page-kind="slides"] .slide::-webkit-scrollbar { width: 15px; height: 15px; background: var(--panel-2); }
  body[data-page-kind="slides"] .slide::-webkit-scrollbar-thumb { background: var(--muted); border: 2px solid var(--panel-2); border-radius: 8px; }
}
/* deck-scrollbar:end */'''

DECK_NAVIGATION = '''/* deck-navigation:begin */
function render(){slides.forEach((s,i)=>s.classList.toggle('active',i===index));$('#counter').textContent=`${index+1} / ${slides.length}`;$('#progress').style.width=`${(index+1)/slides.length*100}%`;requestAnimationFrame(drawCurrent)}
function go(n){
  index=Math.max(0,Math.min(slides.length-1,n));render();
  const slide=slides[index];
  // Every user navigation starts at the heading, including revisited slides.
  slide.scrollTo({top:0,left:0,behavior:'instant'});
  for(const chart of slide.querySelectorAll('.chart'))chart.scrollTo({top:0,left:0,behavior:'instant'});
  slide.focus({preventScroll:true});
}
$('#prev').onclick=()=>go(index-1);$('#next').onclick=()=>go(index+1);
document.addEventListener('keydown',e=>{
  // A focused chart keeps its native horizontal scrolling, as do form fields.
  if(e.target.closest('.chart,input,textarea,select,[contenteditable="true"]'))return;
  if(e.key==='ArrowRight'){e.preventDefault();go(index+1)}
  if(e.key==='ArrowLeft'){e.preventDefault();go(index-1)}
});
window.addEventListener('resize',()=>requestAnimationFrame(drawCurrent));
// Initial rendering preserves the masthead and skip link in the focus order.
render();
/* deck-navigation:end */'''


def normalize_deck_accessibility(text):
    """Maintain bounded, named slide owners without taking over authored layout."""
    if not re.search(r'<main\b[^>]*class="deck"', text):
        return text
    layout = re.search(r'<style data-deck-layout>.*?</style>', text, re.S)
    assert layout, 'authored deck screen layout missing'
    block, count = re.subn(
        r'(body\[data-page-kind="slides"\] \.deck \{[^}]*?)overflow:(?:hidden|visible);',
        r'\1overflow:visible;', layout[0])
    assert count == 1, 'exactly one authored deck overflow boundary'
    block = re.sub(r'\n?/\* deck-scrollbar:begin \*/.*?/\* deck-scrollbar:end \*/\n?', '', block, flags=re.S)
    block = block.replace('</style>', '\n' + DECK_SCROLLBAR + '\n</style>')
    text = text[:layout.start()] + block + text[layout.end():]
    sections = list(re.finditer(r'<section\b[^>]*class="slide(?: active)?"[^>]*>.*?</section>', text, re.S))
    assert len(sections) == 16, 'preserved sixteen authored slides'
    for i, section in reversed(list(enumerate(sections, 1))):
        source = section[0]
        heading = re.search(r'<h[12]\b[^>]*>(.*?)</h[12]>', source, re.S)
        assert heading, 'each authored slide has a heading'
        name = ' '.join(unescape(re.sub(r'<[^>]*>', '', heading[1])).split())
        def named(match, label):
            tag = re.sub(r'\s+(?:tabindex|role|aria-label)="[^"]*"', '', match[0])
            return tag[:-1] + ' tabindex="0" role="region" aria-label="' + escape(label, quote=True) + '">'
        source = re.sub(r'<section\b[^>]*>', lambda m: named(m, f'Slide {i} of {len(sections)}: {name}'), source, count=1)
        source = re.sub(r'<div\b[^>]*class="chart"[^>]*>', lambda m: named(m, name + ' chart'), source)
        text = text[:section.start()] + source + text[section.end():]
    if '/* deck-navigation:begin */' in text:
        pattern = r'/\* deck-navigation:begin \*/.*?/\* deck-navigation:end \*/'
    else:
        pattern = r'function render\(\)\{slides\.forEach.*?window\.addEventListener\(\x27resize\x27,\(\)=>requestAnimationFrame\(drawCurrent\)\);render\(\);'
    text, count = re.subn(pattern, lambda _: DECK_NAVIGATION, text, flags=re.S)
    assert count == 1, 'exactly one owned deck navigation region'
    return text
