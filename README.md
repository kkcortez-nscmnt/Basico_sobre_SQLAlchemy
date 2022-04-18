# Configuração Ambiente de Trabalho Python Windows - VS Code

**Jamilson do Nascimento**

# Introdução

A configuração do ambiente de desenvolvimento interfere diretamente na produtividade ao se projetar um sistema.

Iniciar o código utilizando Python totalmente “cru” e atender as boas práticas de programação é uma tarefa com um certo grau de esforço, requerendo bastante atenção do desenvolvedor e constantes revisões de código. O que consequentemente gera um tempo maior a ser empregado em seu desenvolvimento e não garante que as principais convenções de boas práticas adotadas pela comunidade serão alcançadas. 

Outro agravante a ser levado em consideração, é a compatibilidade entre as dependências de diferentes projetos em uma mesma máquina e o forte acoplamento que a instalação global dessas dependências acarretam. 

Felizmente, existem algumas bibliotecas que servem de auxílio no momento de desenvolvimento. Essas bibliotecas, quando empregadas em conjunto  nos possibilitam:

- A automatização do o estilo de escrita do código. Pontuando os erros, corrigindo-os automaticamente.
- A customização de acordo com as necessidades do projeto.
- Isolamento de diferentes projetos em ambientes virtuais, de modo a garantir sua independência em relação ao sistema global.

Este artigo tem como finalidade apresentar algumas destas bibliotecas, dando uma breve descrição de suas funcionalidades e auxiliar na configuração de ambiente de desenvolvimento back-end utilizando Python e o editor de código Visual Studio Code.

# Iniciação Git e criação arquivo .gitignore

O primeiro passo para a preparação do ambiente é a inicialização do [git](https://git-scm.com) no diretório do projeto e a criação do arquivo .gitignore que ficara responsável pelos arquivos que serão ignorados ao serem postados no repositório do github.

```bash
git init
```

# Criação de ambientes virtuais com virtualenv

A biblioteca [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#) tem por objetivo a criação de ambientes virtuais isolados, empacotando as dependências do projeto em um diretório, fazendo com que desta forma nenhum pacote seja instalado de modo global no sistema operacional. Obviamente, a biblioteca virtualenv em si é instalada no sistema operacional no modo global.

Desta forma há ganho de tempo, organização e facilidade de manutenção e soluções de compatibilidade em múltiplos projetos sendo desenvolvidos em uma mesma máquina.

![Slide1.PNG](Configurac%206bc77/Slide1.png)

```bash
pip install virtualenv
```

Para criação do ambiente virtual utilizar o seguinte comando:

```bash
virtualenv venv
```

Por padrão, a comunidade de desenvolvedores Python utiliza o nome “env”, mas nada impede de se adotar outros nomes.

Para a ativação do ambiente virtual, estando localizado na pasta raiz do projeto,  utilizar o seguinte comando:

```bash
venv\Scripts\activate
```

Após ativação, o nome adotado para o ambiente virtual estará disposto no canto inferior to terminal.

![venv.png](Configurac%206bc77/venv.png)

Para configurar o ambiente virtual no vscode utilizar os comando Ctrl+Shift+P , digitar Python: Select Interpreter.

![venv.png](Configurac%206bc77/venv%201.png)

Escolher a opção associada ao ambiente virtual recém criado.

![venv.png](Configurac%206bc77/venv%202.png)

# Instalação do Pylint

O [pylint](https://pypi.org/project/pylint/) é uma biblioteca responsável pela verificação da qualidade do código, tendo como base a convenção adotada pela comunidade de desenvolvedores, o guia de estilo [Pep8](https://www.python.org/dev/peps/pep-0008/). 

![pylint.png](Configurac%206bc77/pylint.png)

```bash
pip install pylint
```

É possivel gerar um arquivo para a customização das convenções a serem consideradas pela revisão do pylint, através do comando:

```bash
pylint --generate-rcfile > .pylintrc
```

Para customizar as convenções inclua no arquivo .pylintrc o comando ‘disable’ e logo em seguida informe a convenção a ser ignorada, por exemplo:

```python
#  arquivo .pylintrc
disable =
				C0144 # missing-module-docstring, consider-using-f-string
```

Ao executarmos o comando “pylint file_name.py” no terminal, será retornado uma nota de 0 a 10 como avaliação do código.

# Instalação do Black

[Black](https://pypi.org/project/black/) e uma biblioteca que tem como reponsabilidade a formatação de código, de acordo com as convenções do Pep8 e deixando-o mais “legível e bonito”.  Não importa quem escreveu o código, o black irá analisá-lo e formata-lo de uma maneira semelhante, facilitando assim a leitura de um código feito por uma equipe.

![black.png](Configurac%206bc77/black.png)

```bash
pip install black
```

**Configurando o Black no VS Code**

Para o black rodar corretamente no VS Code, é necessário fazer algumas configurações em seu arquivo settings.json. Para isso aperte as teclas Ctrl+Shift+P e digite “settings json”, e escolha a opção Open settings json. Adicionar a seguinte configuração no arquivo:

```json
{

// outras configurações estarão aqui

// configurações do black e organizar imports
    "python.formatting.provider" :"black",
    "python.formatting.blackArgs": ["--line-length", "88"],
    "[python]": {
        "editor.formatOnSave":true,
        "editor.codeActionsOnSave":{
            "source.organizeImports": true
        }
    },

// configurações de compatibilidade black -isort
    "python.sortImports.args":["-m3", "--tc", "-fgw 0", "--up", "-n", "-l 88"],

// configuração compatibilidade flake8
    "python.linting.flake8Enabled":true,
    "python.linting.flake8Args": ["--ignore=E203, E722, W503, E501","--max-line-length=88"],

// configurações compatibilidade black e pylint
    "python.linting.pylintEnabled": true,
    
}
```

A configuração “python.formatting.provider” é responsável pela determinação de qual ferramenta irá ser usada para a formatação de código, sendo possível as seguintes opções: autopep8, black  e  yapf.

A configuração “python.formatting.blackArgs”  executam as opções que serão repassadas no momento da execução do black. Para visualizar as opções disponíveis podem digite o seguinte comando no terminal:

```json
black - h
```

O bloco “[python]”  indica que as configurações  determinadas em seu escopo, só terão validade em arquivos .py. A configuração “editor.formatOnSave” indica que o arquivo seve ser formatado toda vez que for salvo.

A configuração “editor.codeActionOnSave”: { “source.organizedImports”:true } é responsável pela organização dos imports de modo que não causem conflitos de funcionais em relação a ordem de importação dos módulos.

A configuração “python.sortImport.args” garante a compatibilidade entre a biblioteca [isort](https://pypi.org/project/isort/). O comando “Sort Imports” (click botão direito), organiza a formatação quando as importações possuem nomes extensos.

Ao executarmos o comando “black file_name.py” no terminal, código será formatado.

# Instalação Flake8

[Flake8](https://flake8.pycqa.org/en/latest/#) é uma biblioteca que empacota três “conceitos” de funcionalidade: PEP8, [PyFlakes](https://pypi.org/project/pyflakes/) e [Codepaths](https://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html).

A configuração “python.linting.flake8Enable”: true, permite o uso do flake8 no Vs code.

```python
pip install flake8
```

![flake8.png](Configurac%206bc77/flake8.png)

Criar um arquivo de configuração .flake8

```python
[flake8]
ignore = E722, W503
max-line-length = 120
per-file-ignores =
    __init__.py: F401
```

# Instalação do Pytest

O [pytest](https://docs.pytest.org/en/7.0.x/) é o um framework de testes do python. Ao rodar o pytest, dentro do ambiente virtual, ele procura por arquivos que respeitem sua convenção de nomenclatura, ou seja, arquivos que tenham o nome nos seguintes formatos: test_file_name.py ou file_name_test.py. Para evitar conflitos, recomenda-se a utilização de arquivos __init__.py em casa um dos diretórios. 

```bash
pip install pytest
```

![pytest.png](Configurac%206bc77/pytest.png)

Um exemplo de organização  de projeto utilizando o pytest:

```bash
root/
	env
	src/
		domain
		infra/
			config/
			entities/
			repositories/
				entity_repository_test.py
   
```

A estrutura dos arquivos de teste seguem o seguinte padrão:

```python
# soma.py
def soma(num_1: int, num_2: int) -> int:
""" Soma de dois numeros
:param - num1: primeiro argumento da soma
       - num2: segundo argumento da soma.
:return - Soma entre dois numeros.
"""
soma_entre_dois numeros = num_1 + num_2
return soma_entre_dois_numeros
```

```python
# test_soma.py

def test_soma(): # o nome deve sempre iniciar com test
	""" testando a função soma """
	result = soma(2,4)
	assert result == 6 # aqui sempre será um teste lógico
```

O comando pytest roda os teste no ambiente virtual. Em caso de falha ao se rodar o pytest, será indicado um *[exit code.](https://elinux.org/Test_Result_Codes)* 

- Exit code 0: All tests were collected and passed successfully
- Exit code 1: Tests were collected and run but some of the tests failed
- Exit code 2: Test execution was interrupted by the user
- Exit code 3: Internal error happened while executing tests
- Exit code 4: pytest command line usage error
- Exit code 5: No tests were collected

# **Instalação pre-commit**

Todos os passos realizados até agora serão configurados em *hooks*  e serão executados antes da validação de um commit com o uso do framework [pre-commit](https://pre-commit.com/#install).

![precommit.png](Configurac%206bc77/precommit.png)

```bash
pip install pre-commit
```

Após a instalação utilizar o seguinte comando para configurações internas entre o framework e o git:

```bash
pre-commit install
```

![pre-commit install.png](Configurac%206bc77/pre-commit_install.png)

Criar arquivo .pre-commit-config.yaml

```yaml
repos:
-   repo: https://github.com/ambv/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.9.8
      stages: [commit]
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.7.9
    hooks:
    - id: flake8
      stages: [commit]
-   repo: local
    hooks:
    - id: pytest
      name: pytest
      language: system
      entry: pytest -v -s
      always_run: true
      pass_filenames: false
      stages: [commit]
-   repo: local
    hooks:
      - id: requirements
        name: requirements
        entry: cmd /c 'pip freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]
```

Sem hook para pytest

```yaml
repos:
-   repo: https://github.com/ambv/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.9.8
      stages: [commit]
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.7.9
    hooks:
    - id: flake8
      stages: [commit]
-   repo: local
    hooks:
      - id: requirements
        name: requirements
        entry: cmd /c 'pip freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]
```

# Dependências de projeto

Para finalizar, criar arquivo requirements.txt. Este arquivo armazena o nome e a versão de todas as bibliotecas da qual o projeto sustenta, e serve como um gatilho para a instalação dos mesmos. A motivação para sua criação se da ao trabalharmos com repositórios remotos, como o *github,* para o compartilhamento de código com a equipe de desenvolvimento.

Para criação do arquivo requirements.txt executar o comando:

```python
pip freeze > requirements.txt
```

Para instalar as bibliotecas registradas em requirements.txt

```python
pip install -r requirements.txt
```

# Conclusão

A utilização das bibliotecas apresentadas proporcionam compatibilidade com convenções adotadas pela comunidade de desenvolvedores Python, priorizando a legibilidade de código por terceiros e funcionam como uma ferramenta a ser utilizada em equipe.

# Referências

**Artigos**

[https://joachim8675309.medium.com/python-virtualenv-c77e22bf5243](https://joachim8675309.medium.com/python-virtualenv-c77e22bf5243)

[https://henriquebastos.net/mantenha-seu-codigo-em-ordem-com-flake8-e-coverage/](https://henriquebastos.net/mantenha-seu-codigo-em-ordem-com-flake8-e-coverage/)

[https://www.fabioruicci.com.br/artigos/python-vs-code-black-como-formatar-o-seu-codigo-python-no-vs-code-automaticamente-usando-black/](https://www.fabioruicci.com.br/artigos/python-vs-code-black-como-formatar-o-seu-codigo-python-no-vs-code-automaticamente-usando-black/)

[https://elinux.org/Test_Result_Codes](https://elinux.org/Test_Result_Codes)

**Documentações Oficiais**

[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

[https://git-scm.com](https://git-scm.com/)

[https://virtualenv.pypa.io/en/latest/installation.html#](https://virtualenv.pypa.io/en/latest/installation.html#)

[https://pypi.org/project/pylint/](https://pypi.org/project/pylint/)

[https://pypi.org/project/black/](https://pypi.org/project/black/)

[https://pypi.org/project/flake8/](https://pypi.org/project/flake8/)

[https://pypi.org/project/pyflakes/](https://pypi.org/project/pyflakes/)

[https://docs.pytest.org/en/7.0.x/](https://docs.pytest.org/en/7.0.x/)

[https://pre-commit.com/](https://pre-commit.com/#install)

**Imagens e ícones**

[https://www.flaticon.com/free-icons/pokemon](https://www.flaticon.com/free-icons/pokemon) 

[https://www.flaticon.com/br/icones-gratis/arquivo-python](https://www.flaticon.com/br/icones-gratis/arquivo-python) 

[https://www.flaticon.com/free-icons/gear](https://www.flaticon.com/free-icons/gear)
