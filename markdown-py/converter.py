from utils import convert_formatting, convert_heading, convert_links, convert_code_blocks, convert_lists

def markdown_to_html(markdown_text):
    html_lines = []

    lines = markdown_text.split("\n")
    lines = convert_code_blocks(lines)
    lines = convert_lists(lines)

    for line in lines:
        html_line = convert_heading(line)
        if html_line is None:
            if not line.startswith("<code><pre>") and not line.startswith("</pre></code>"):
                line = convert_formatting(line)
                line = convert_links(line)
                html_line = f'<p>{line}</p>' if line.strip() else ''
            else:
                html_line = line
        html_lines.append(html_line)
        
    return "\n".join(html_lines)