# imports

from rich import progress
from rich import layout
from rich.console import Console
from rich.progress import track
from rich.table import Table
from time import sleep
from rich.layout import Layout
from rich.panel import Panel

# instância do console
console = Console()

console.print('[red]testando[/] 1 2 3')
console.print('[underline]Sublinhado[/], [bold]negrito[/], [on green]fundo[/], emojis :smile:')
console.print(':warning: ISTO É UM AVISO', style='bold on red')

# progress bar 1
for tarefa in track(range(10), 'Processando...'):
	sleep(0.5)


# logs and loadings
def processos():
	for i in range(1, 5):
		sleep(1)
		console.log(f'Processo {i} encerrado')


with console.status('[green]Analisando valor do processo...[/]') as processo:
	processos()

# tables
table = Table(title='Pessoas')

# creating columns / justify, style
table.add_column('Nome')
table.add_column('Idade')
table.add_column('Emprego')

# adding rows
table.add_row('Carlos', '23', 'Engenheiro Civil')
table.add_row('Mariana', '32', 'Cientista de Dados')
table.add_row('Leonardo', '13', 'Estudante')

console.print(table)

# layouts
layout = Layout()
layout.split_column(
	Layout(name='topo'),
	Layout(name='baixo')
)

console.print(layout)
