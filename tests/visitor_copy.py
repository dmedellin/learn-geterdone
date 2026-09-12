"""Conservative visitor-copy inventory; no route-specific exceptions.

DOM text includes inactive and noscript fallbacks. JavaScript literal strings are
an overapproximation of dynamic copy, including search data and export templates.
URLs and identifiers are not prose. Every vocabulary exception states a domain
meaning, never a page name. The CLI emits findings and those classifications.
"""
import argparse
from collections import Counter
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin


def words(text):
    return ' '.join(unescape(text).split())


class Document(HTMLParser):
    BLOCKS = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'li', 'button',
              'label', 'option', 'text', 'title', 'pre', 'td', 'th', 'dt', 'dd',
              'div', 'section', 'article', 'nav', 'footer', 'header', 'body'}
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
            'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, source, route='fixture'):
        super().__init__(convert_charrefs=True)
        self.route = route
        self.family = None
        self.records = []
        self.stack = []
        self.anchors = []
        self.feed(source)
        self.close()

    def record(self, boundary, text, **context):
        if words(text):
            self.records.append(dict(route=self.route, family=self.family,
                                     boundary=boundary, text=words(text), **context))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'body':
            self.family = attrs.get('data-page-kind')
        node = dict(tag=tag, attrs=attrs, text='', copy='', line=self.getpos()[0])
        if tag in self.BLOCKS:
            self.flush()
        self.stack.append(node)
        for key in ('aria-label', 'title', 'alt', 'value', 'placeholder', 'data-why'):
            if key in attrs:
                self.record('attribute:' + key, attrs[key], tag=tag, line=node['line'])
        if tag == 'meta' and attrs.get('content') and (
                attrs.get('name') in ('description', 'twitter:description', 'twitter:title')
                or attrs.get('property') in ('og:description', 'og:title', 'twitter:description', 'twitter:title')):
            self.record('metadata:' + attrs.get('name', attrs.get('property', '')),
                        attrs['content'], tag=tag, line=node['line'])
        if tag in self.VOID:
            self.stack.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def flush(self):
        node = next((n for n in reversed(self.stack) if n['tag'] in self.BLOCKS), None)
        if node and node['copy']:
            self.record('text', node['copy'], tag=node['tag'], line=node['line'])
            node['copy'] = ''

    def handle_endtag(self, tag):
        if not any(n['tag'] == tag for n in self.stack):
            return
        node = next(n for n in reversed(self.stack) if n['tag'] == tag)
        if tag in self.BLOCKS:
            self.flush()
        if tag == 'script':
            if node['attrs'].get('type', '').endswith('json'):
                self.json_records(node['text'], 'structured-json')
            else:
                for literal in js_literals(node['text']):
                    self.record('dynamic-string', literal, tag='script', line=node['line'])
                for match in re.finditer(r'([\'"`])((?:Lesson|Course)\s+)\1\s*\+', node['text'], re.I):
                    self.record('dynamic-string', match[2] + '{dynamic}', tag='script', line=node['line'])
        if tag == 'a':
            self.anchors.append(dict(href=node['attrs'].get('href', ''),
                                     text=words(node['text']), attrs=node['attrs']))
        while self.stack:
            popped = self.stack.pop()
            if popped is node:
                break
        if tag == 'body':
            for record in self.records:
                record['family'] = self.family

    def handle_data(self, data):
        for n in self.stack:
            n['text'] += data
        if any(n['tag'] in ('style', 'script') for n in self.stack):
            return
        n = next((n for n in reversed(self.stack) if n['tag'] in self.BLOCKS), None)
        if n:
            n['copy'] += data

    def json_records(self, source, boundary):
        def walk(value, key=''):
            if isinstance(value, dict):
                for k, v in value.items():
                    walk(v, k)
            elif isinstance(value, list):
                for v in value:
                    walk(v, key)
            elif isinstance(value, str):
                self.record(boundary, value, field=key)
        walk(json.loads(source))


def js_literals(source):
    # Lex comments before strings. Template expressions remain in the inventory:
    # a fragmented label is also checked by the real-browser adjacency probe.
    token = re.compile(r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`')
    for match in token.finditer(source):
        raw = match[0]
        if raw[0] not in "\"'`":
            continue
        text = re.sub(r'\\u([\da-fA-F]{4})', lambda m: chr(int(m[1], 16)), raw[1:-1])
        text = re.sub(r'\\([\'"`/])', r'\1', text).replace('\\n', '\n')
        yield text


NUMERIC = re.compile(r'\b(?:lessons?|courses?)[\s-]+(?:\d+(?:st|nd|rd|th)?\b|(?:one|two|three|four|five|six|seven|eight|nine|ten)\b|\$\{[^}]+\}|\{dynamic\})', re.I)
ORDINAL = re.compile(r'\b(?:(?:the\s+)?(?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|previous|next|last|final|earlier|later|preceding|following|remaining)(?:\s+(?:few|two|three|four))?\s+(?:lessons?|courses?)|(?:lessons?|courses?)\s+(?:before|after)\s+this)\b', re.I)
RANGE = re.compile(r'\(\s*0?\d{1,2}\s*[–—-]\s*0?\d{1,2}\s*\)')
FRAMING = re.compile(r'\b(?:learning\s+(?:paths?|tracks?)|(?:trading|algebra|discrete mathematics)\s+(?:paths?|tracks?)|open a path|start here|(?:learn|study|take|work through|read)\b[^.!?]{0,45}\bin order|(?:course|lesson|curriculum)\s+(?:progression|sequence|stages?|modules?|tracks?)|(?:first|next|final)\s+stage|front[- ]to[- ]back|learning journey|learning roadmap|strict dependency order)\b', re.I)
IMPLICIT = re.compile(
    r'\b(?:(?:first|second|last)\s+(?:half|third|quarter)\s+of\s+(?:this|the)\s+course'
    r'|(?:before|after)\s+(?:this|the)\s+(?:course|lesson)'
    r'|(?:later|earlier)\s+in\s+(?:this|the)\s+course'
    r'|from here on(?:wards?)?'
    r'|every later solution set|every method later on|every notation you meet later'
    r'|(?:nothing|anything|every function|formulas available) so far'
    r'|every technique in the first half'
    r'|(?:every|each)\s+(?:later|earlier)\s+(?:tool|topic)'
    r'|(?:parts|material|concepts)\s+(?:above|below)'
    r'|later\s+(?:supplies|introduces|covers|teaches)'
    r'|(?:formula|method)\b[^.!?]{0,160}\bcomes next)\b', re.I)


def domain_reason(record, rule, match):
    text = record['text']
    if rule == 'catalog-range' and '-' in match[0]:
        before, after = text[:match.start()], text[match.end():]
        if re.search(r'(?:lessons?|courses?)\s*$', before, re.I) or re.search(r'\b0\d', match[0]):
            return None
        if (record.get('tag') == 'pre' or '<span class="math">' in text
                or re.search(r'[=×·÷^+]|\bsqrt\(', before[-60:] + after[:60])):
            return 'Parenthesised subtraction inside an arithmetic expression; the hyphen is a binary minus, not a catalog range.'
        if record['boundary'] == 'attribute:value' and '|' in text and re.search(r'[*/]', text):
            return 'A worked-expression preset encodes alternatives separated by pipes; the parenthesised difference is a denominator.'
    if rule == 'prescriptive-framing':
        if text == 'Take each edge in order if it joins two components':
            return 'Kruskal edge-processing instruction: the ordering applies to weighted edges, not Courses or Lessons.'
        if text == 'Read the pair in order':
            return 'Ordered-pair reading instruction: horizontal coordinate then vertical coordinate, not catalog ordering.'
        if 'acceptable to g' in text and 'acceptable to f' in text and 'first stage' in match[0]:
            return 'Function composition applies g then f; the first stage is evaluation of g, not a curriculum stage.'
    return None


def classify(record):
    text = record['text']
    # Route bytes and machine field names are inventoried but not visitor copy.
    if re.fullmatch(r'(?:https?://|/|\.\.?/)[^\s<>]+', text):
        return [], []
    matches = []
    legitimate = []
    if record.get('named_course_sequence'):
        matches.append(dict(record, rule='named-course-sequencing', match=record['named_course_sequence']))
    if (record.get('tag') == 'nav' or record.get('family') in ('library', 'subject', 'course')) and re.fullmatch(r'(?:paths?|tracks?|modules?|progression|stages?)', text, re.I):
        matches.append(dict(record, rule='taxonomy-label', match=text))
    if record['boundary'] == 'catalog-anchor' and re.match(r'^(?:Lesson\s+|Course\s+)?\d+\b', text, re.I):
        matches.append(dict(record, rule='numbered-link', match=text))
    for name, pattern in [('numeric-reference', NUMERIC), ('ordinal-dependency', ORDINAL),
                          ('catalog-range', RANGE), ('prescriptive-framing', FRAMING),
                          ('implicit-curricular-order', IMPLICIT)]:
        for m in pattern.finditer(text):
            reason = domain_reason(record, name, m)
            if reason:
                legitimate.append(dict(record, rule=name, match=m[0], reason=reason))
            else:
                matches.append(dict(record, rule=name, match=m[0]))
    return matches, legitimate


def findings(record):
    return classify(record)[0]


def scan(site):
    pages = {}
    records = []
    for file in sorted(site.rglob('*.html')):
        route = '/' + file.relative_to(site).as_posix().removesuffix('index.html')
        doc = Document(file.read_text(), route)
        if not doc.family:
            raise ValueError('missing authored page family: ' + route)
        pages[route] = doc
        records.extend(doc.records)
    for route, doc in pages.items():
        for anchor in doc.anchors:
            target = pages.get(urljoin(route, anchor['href']))
            if target and target.family in ('course', 'lesson'):
                records.append(dict(route=route, family=doc.family, boundary='catalog-anchor',
                                    href=anchor['href'], target=urljoin(route, anchor['href']),
                                    text=anchor['text']))
    for file in sorted(site.rglob('*.json')):
        doc = Document('', '/' + file.relative_to(site).as_posix())
        doc.family = 'asset'
        doc.json_records(file.read_text(), 'asset-json')
        records.extend(doc.records)
    # Named Courses can still be presented as a compulsory timeline after
    # their numeric labels disappear. Derive names from the rendered owners.
    titles = {r['text'] for p in pages.values() if p.family == 'course'
              for r in p.records if r.get('tag') == 'h1' and r['boundary'] == 'text'}
    if titles:
        named_order = re.compile(r'\b(' + '|'.join(re.escape(t) for t in sorted(titles))
                                 + r')\s+(?:began|begins|started|starts|ended|ends)\s+with\b', re.I)
        for record in records:
            if match := named_order.search(record['text']):
                record['named_course_sequence'] = match[0]
    return pages, records


def report(site):
    pages, records = scan(site)
    return dict(pages=len(pages), families=dict(Counter(p.family for p in pages.values())),
                scanned_records=dict(Counter(r['boundary'] for r in records)),
                findings=[f for r in records for f in classify(r)[0]],
                legitimate_domain_controls=[f for r in records for f in classify(r)[1]])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('site', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = report(args.site)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: len(v) if k in ('findings', 'legitimate_domain_controls') else v for k, v in result.items()}, indent=2))
    raise SystemExit(bool(result['findings']))
