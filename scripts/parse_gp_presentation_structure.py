from pathlib import Path

src = Path('/workspace/research/beal/data/fdom_level35721_tuned.txt').read_text()
start = src.index('PRESENTATION=') + len('PRESENTATION=')
expr = src[start:].strip()

# Trim to the first complete top-level bracketed expression.
if not expr.startswith('['):
    raise SystemExit('PRESENTATION is not a GP vector')

def matching_end(s: str, pos: int = 0) -> int:
    pairs = {'[': ']', '(': ')', '{': '}'}
    stack = []
    quote = None
    escaped = False
    for i in range(pos, len(s)):
        ch = s[i]
        if quote:
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == quote:
                quote = None
            continue
        if ch in "'\"":
            quote = ch
        elif ch in pairs:
            stack.append(pairs[ch])
        elif ch in ']})':
            if not stack or ch != stack.pop():
                raise ValueError(f'unbalanced at {i}')
            if not stack:
                return i
    raise ValueError('unterminated expression')

end = matching_end(expr)
expr = expr[:end+1]

def split_top(s: str):
    assert s[0] == '[' and s[-1] == ']'
    out, stack, quote, escaped, begin = [], [], None, False, 1
    pairs = {'[': ']', '(': ')', '{': '}'}
    for i in range(1, len(s)-1):
        ch = s[i]
        if quote:
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == quote:
                quote = None
            continue
        if ch in "'\"":
            quote = ch
        elif ch in pairs:
            stack.append(pairs[ch])
        elif ch in ']})':
            if stack and ch == stack[-1]:
                stack.pop()
        elif ch == ',' and not stack:
            out.append(s[begin:i].strip())
            begin = i + 1
    out.append(s[begin:-1].strip())
    return out

parts = split_top(expr)
lines = [f'P_LEN={len(parts)}', f'P_CHARS={len(expr)}']
for idx, part in enumerate(parts, 1):
    lines.append(f'P{idx}_CHARS={len(part)}')
    lines.append(f'P{idx}_PREFIX={part[:300]!r}')
    lines.append(f'P{idx}_SUFFIX={part[-300:]!r}')
    if part.startswith('[') and part.endswith(']'):
        try:
            sub = split_top(part)
            lines.append(f'P{idx}_TOP_LEVEL_LEN={len(sub)}')
            for j, x in enumerate(sub[:5], 1):
                lines.append(f'P{idx}_{j}_PREFIX={x[:160]!r}')
        except Exception as exc:
            lines.append(f'P{idx}_PARSE_ERROR={exc!r}')
Path('/workspace/research/beal/data/tuned_presentation_structure_py.txt').write_text('\n'.join(lines))
print('ok')