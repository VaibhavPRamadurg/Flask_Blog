import os
import re
import tokenize
import io

def remove_html_comments(content):
    content = re.sub(r'<!--.*?-->\n?', '', content, flags=re.DOTALL)
    


    content = re.sub(r'{#.*?#}\n?', '', content, flags=re.DOTALL)
    return content

def remove_js_css_comments(content):

    content = re.sub(r'/\*.*?\*/\n?', '', content, flags=re.DOTALL)
    
    content = re.sub(r'(?<!:)//.*?\n', '\n', content)
    return content

def remove_python_comments(source):
    io_obj = io.StringIO(source)
    out = ""
    last_lineno = -1
    last_col = 0
    try:
        for tok in tokenize.generate_tokens(io_obj.readline):
            token_type = tok[0]
            token_string = tok[1]
            start_line, start_col = tok[2]
            end_line, end_col = tok[3]
            
            if start_line > last_lineno:
                last_col = 0
            if start_col > last_col:
                out += (" " * (start_col - last_col))
            
            if token_type == tokenize.COMMENT:
                pass
            else:
                out += token_string
                
            last_lineno = end_line
            last_col = end_col
    except Exception:
        return source
    return out

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    if filepath.endswith('.html'):
        content = remove_html_comments(content)
    elif filepath.endswith('.css') or filepath.endswith('.js'):
        content = remove_js_css_comments(content)
    elif filepath.endswith('.py'):
        content = remove_python_comments(content)
        
    # Remove consecutive blank lines left behind (more than 2)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {filepath}")

def main():
    target_dir = '/Users/vaibhav/Desktop/Flask_NewBlog/flaskblog'
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            if f.endswith(('.html', '.js', '.css', '.py')):
                clean_file(os.path.join(root, f))

if __name__ == "__main__":
    main()
