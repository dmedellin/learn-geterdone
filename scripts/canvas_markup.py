"""Renewable canvas infrastructure on the authored Trading/capstone sources."""
import pathlib
import subprocess
from html import escape

def normalize(text, relative, spans_type):
    if '<canvas' not in text.lower():
        return text
    # Existing chart owners remain in place. A standalone canvas gets a single
    # narrow owner, leaving neighboring authored content outside the scroller.
    changes = []
    nodes = spans_type(text).elements
    for canvas in (n for n in nodes if n['tag'] == 'canvas'):
        parents = sorted((n for n in nodes if n['start'] < canvas['start'] and n['end'] > canvas['end']),
                         key=lambda n:n['end']-n['start'])
        parent = parents[0]
        if parent['attrs'].get('data-canvas-scroll') == 'v1':
            continue
        if parent['attrs'].get('class') == 'chart' and 'data-page-kind="slides"' in text:
            # The authored deck already owns a 600px named/focusable chart
            # scroller, including its separate print geometry.
            continue
        label = canvas['attrs'].get('aria-label')
        if not label:
            section = next((n for n in parents if n['tag'] == 'section'), None)
            headings = [n for n in nodes if n['tag'] in ('h2','h3') and section and
                        section['start'] < n['start'] < canvas['start']]
            label = 'Chart'
            if headings:
                from html import unescape
                import re
                h = headings[-1]
                label = unescape(re.sub('<[^>]*>', '', text[h['open_end']:h['close_start']])) + ' chart'
        opening = '<div data-canvas-scroll="v1" tabindex="0" role="region" aria-label="%s">' % escape(label, quote=True)
        changes.extend([(canvas['start'], opening), (canvas['end'], '</div>')])
    for offset, value in sorted(changes, reverse=True):
        text = text[:offset] + value + text[offset:]
    css = '<style data-canvas-scroll="v1">\n[data-canvas-scroll="v1"]{overflow:auto;max-width:100%;min-width:0}[data-canvas-scroll="v1"] canvas{display:block;min-width:520px}.card:has(>[data-canvas-scroll="v1"]){min-width:0}.lab:has([data-canvas-scroll="v1"]),.chart-wrap:has(>[data-canvas-scroll="v1"]){overflow:visible}.chart-wrap:has(>[data-canvas-scroll="v1"])>:is(.chart-badge,.chart-label){position:relative;display:table;left:auto;top:auto;margin:14px}@media print{[data-canvas-scroll="v1"]{overflow:visible}[data-canvas-scroll="v1"] canvas{min-width:0}}\n</style>'
    import re
    if '<style data-canvas-scroll="v1">' in text:
        text = re.sub(r'<style data-canvas-scroll="v1">[\s\S]*?</style>',lambda _:css,text,count=1)
    else:
        text = text.replace('</head>',css+'\n</head>',1)
    result = subprocess.run(['node', str(pathlib.Path(__file__).with_name('canvas_normalize.js')), relative],
                            input=text, text=True, capture_output=True, check=True)
    return result.stdout
