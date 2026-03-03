# -*- coding: utf-8 -*-

def formatar_texto(texto):
    linhas = [l.strip() for l in texto.split("\n") if l.strip()]
    html_final = ""
    
    # Configurações de comando centralizado (Alterando aqui, muda em todos os robôs)
    COR_MD = "rgb(7, 55, 99)"
    TAMANHO_H2 = "22px"
    TAMANHO_TEXTO = "16px"

    for linha in linhas:
        e_titulo_markdown = linha.startswith("#")
        linha_limpa = linha.strip("#* ").strip()

        # Lógica para detectar se a linha é um título
        if e_titulo_markdown or (len(linha_limpa.split()) <= 18 and not linha_limpa.endswith(".")):
            if "considerações finais" in linha_limpa.lower():
                titulo_texto = "Considerações Finais"
            else:
                titulo_texto = linha_limpa

            # --- AQUI VOCÊ CONTROLA O H2 ---
            html_final += f"""
            <h2 style="
                text-align:left !important;
                font-family:Arial, Helvetica, sans-serif !important;
                color:{COR_MD} !important;
                font-size:{TAMANHO_H2} !important;
                font-weight:bold !important;
                margin-top:30px !important;
                margin-bottom:10px !important;
                display:block !important;
                line-height:1.3 !important;
            ">
                {titulo_texto}
            </h2>
            """
        else:
            # --- AQUI VOCÊ CONTROLA O TEXTO DA POSTAGEM ---
            html_final += f"""
            <p style="
                text-align:justify !important;
                font-family:Arial, Helvetica, sans-serif !important;
                color:{COR_MD} !important;
                font-size:{TAMANHO_TEXTO} !important;
                font-weight:normal !important;
                margin-top:0px !important;
                margin-bottom:15px !important;
                line-height:1.7 !important;
                display:block !important;
            ">
                {linha_limpa}
            </p>
            """

    return html_final


def obter_esqueleto_html(dados):
    titulo = dados.get("titulo", "")
    imagem = dados.get("imagem", "")
    texto_completo = dados.get("texto_completo", "")
    assinatura = dados.get("assinatura", "")

    # Chama a função acima que agora já vem com os tamanhos definidos
    conteudo_formatado = formatar_texto(texto_completo)

    FONTE_GERAL = "Arial, Helvetica, sans-serif"
    COR_MD = "rgb(7, 55, 99)"

    html = f"""
    <div style="
        font-family:{FONTE_GERAL} !important;
        color:{COR_MD} !important;
        font-size:16px !important;
        font-weight:normal !important;
        text-align:justify !important;
        line-height:1.7 !important;
        margin:0px !important;
        padding:0px !important;
        display:block !important;
    ">

        <h1 style="
            text-align:left !important;
            font-family:{FONTE_GERAL} !important;
            color:{COR_MD} !important;
            font-size:26px !important;
            font-weight:bold !important;
            margin-top:0px !important;
            margin-bottom:20px !important;
            line-height:1.3 !important;
            display:block !important;
        ">
            {titulo}
        </h1>

        <div style="
            text-align:center !important;
            margin-bottom:20px !important;
            display:block !important;
        ">
            <img src="{imagem}" style="
                max-width:100% !important;
                height:auto !important;
                display:block !important;
                margin-left:auto !important;
                margin-right:auto !important;
                border-radius:8px !important;
            ">
        </div>

        {conteudo_formatado}

        {assinatura}

    </div>
    """

    return html
