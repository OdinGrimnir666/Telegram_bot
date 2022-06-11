






def Html():
    text='<b>bold</b>, <strong>bold</strong> ' \
         '<i>italic</i>, <em>italic</em>' \
         '<u>underline</u>, <ins>underline</ins>' \
         '<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>' \
         '<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>' \
         '<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>' \
         '<a href="http://www.example.com/">inline URL</a>' \
         '<a href="tg://user?id=123456789">inline mention of a user</a>' \
         '<code>inline fixed-width code</code>' \
         '<pre>pre-formatted fixed-width code block</pre>' \
         '<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>'
    return text


def ProductHtml(product):
    text=\
    f'<b>{product.name}</b>\n' \
    f'<i align="left">{product.description}</i>\n' \
    f'\n' \
    f'\n' \
    f'\n'
    return text