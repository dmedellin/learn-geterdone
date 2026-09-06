"""Theme tokens for the two authored capstone layouts.

The Trading patcher owns the migration and this renewable palette. Component
rules keep their authored layout and hierarchy and consume the same tokens in
both light paths.
"""
import re

BEGIN = '/* capstone-palette:begin */'
END = '/* capstone-palette:end */'
LIGHT = '--capstone-accent: #08616e; --capstone-muted: #425767; --on-accent: #ffffff;'
PALETTE = '''%s
:root { --capstone-accent: #98f5ff; --capstone-muted: #aec1d2; --on-accent: #041116; }
body { --muted: var(--capstone-muted); }
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
