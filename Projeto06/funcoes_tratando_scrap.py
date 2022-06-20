
def byte_string_completa(html: bytes):

    html_tratado = html.decode('utf-8')
    html_tratado = ' '.join(html_tratado.split()).replace('> <', '><')

    return html_tratado

def byte_string_parcial(html: bytes):

    html_tratado = html.decode('utf-8')

    return html_tratado
