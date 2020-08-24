## Contribuindo para o nosso projeto

O miguezômetro sempre tem algo a ser melhorado, se você quer contribuir com o nosso projeto, 
comece por aqui. No entanto, tenha em mente algumas coisas:

* Mesmo que sua alteração seja simples, crie um *issue* antes descrevendo-a, isso nos ajuda a 
documentá-la de forma mais eficiente, além de conscientizar todos os participantes do projeto.

* Tenha certeza de que sua alteração não sai do escopo do nosso projeto, alterações grandes e 
pequenas são igualmente válidas, porém elas devem estar no tema do nosso trabalho. Leia nossa
Wiki para saber mais a respeito do tema.

* Se você quer contribuir, mas não tem ideia de com o quê, olhe nossa página da Wiki sobre
[perspectivas futuras](https://github.com/No-Budget-Science-Hack-Week-2020/miguezometro/wiki#perspectivas-futuras),
que talvez apareça alguma ideia.

* Se você quer uma referência geral de como contribuir, leia o guia abaixo. Se você não tem experiência com git e
linha de comando, recomendamos buscar recursos que te ajudem a compreendê-lo melhor.

### O básico para contribuir

**1. Faça um *fork* desse repositório**

Tem um botão no canto superior direito que você pode clicar para fazer isso.

**2. Clone seu *fork* localmente**

```console
$ git clone --recurse-submodules http://github.com/SEU_NOME_AQUI/miguezometro.git
```

**3. Crie uma *branch* para a alteração que você irá realizar**

```console
$ git checkout -b SEUNOME_DESCRICAO_DA_ALTERACAO
```

Por exemplo, algo como "jvfe_conserta_scraping" seria ideal.
Esse "template" de branch nos ajuda a visualizar rapidamente no nosso histórico que 
alterações fazem o que e de onde elas vieram.


**4. Faça sua alteração**

Agora é tua hora de brilhar, faz a alteração que você tinha em mente e commita ela:

```console
$ git commit -am "Melhora significativamente o nosso projeto"'
```

***(tenha em mente que sua mensagem de commit tem que ser um pouco mais descritiva que essa)***

**5. Faça o *push* de sua *branch* para seu *fork***

```consle
$ git push origin SEUNOME_DESCRICAO_DA_ALTERACAO
```

**6. Crie um *pull request***

Da página de seu fork, deve haver um botão sinalizando a possibilidade de fazer um pull request.
No pull request, seja sucinto, descreva brevemente suas intenções ou então referencie o issue que criou.

**7. Relaxe**

Pois agora você fez uma contribuição para um projeto livre e *open source*!
