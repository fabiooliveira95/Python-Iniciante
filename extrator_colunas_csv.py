import venn
import libarchive
import pydot
import cartopy

import sys


class ArquivoTexto:
    pass


class ArquivoCSV(ArquivoTexto):
    def __init__(self, arquivo: str):
        super().__init__(arquivo=arquivo)
        self.colunas = self.extrair_nome_colunas()

    def extrair_nome_colunas(self):
        with open(self.arquivo, mode='r', encoding='utf8') as arquivo:
            linhas = arquivo.readlines()
            if linhas:
                primeira_linha = linhas[0].strip()
                return primeira_linha.split(",")
            return []

    def extrair_coluna(self, indice_coluna: int):
        valores_coluna = []
        if self.arquivo and indice_coluna >= 0:
            with open(self.arquivo, 'r', encoding='utf8') as arquivo:
                linhas = arquivo.readlines()[1:]  # Skip header
                for linha in linhas:
                    valores = linha.split(",")
                    if len(valores) > indice_coluna:
                        valores_coluna.append(valores[indice_coluna])
        return valores_coluna