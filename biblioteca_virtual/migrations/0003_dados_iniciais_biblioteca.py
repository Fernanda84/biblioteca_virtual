# biblioteca_virtual/migrations/0003_dados_iniciais_biblioteca.py
# (O nome do arquivo pode variar ligeiramente, não altere o cabeçalho gerado pelo Django)

from django.db import migrations


def popular_dados_iniciais(apps, schema_editor):
   
    Livro = apps.get_model('biblioteca_virtual', 'Livro')
    Genero = apps.get_model('biblioteca_virtual', 'Genero')
    
    
    gen_fantasia = Genero.objects.create(nome='Fantasia')
    gen_terror = Genero.objects.create(nome='Terror')
    gen_romance = Genero.objects.create(nome='Romance')
    gen_ficcao = Genero.objects.create(nome='Ficção Científica')

    # --- POPULAR LIVROS (Apenas para testes/estoque inicial) ---
    
    # Exemplo 1: Tolkien (Fantasia)
    Livro.objects.create(
        titulo='O Senhor dos Anéis: A Sociedade do Anel',
        autor='J.R.R. Tolkien', # Exemplo como campo de texto simples
        editora='Allen & Unwin',
        genero=gen_fantasia,  # Exemplo como ForeignKey
        publicacao=1954,
        isbn='978-00-00',
        sinopse='Primeira parte da lendária trilogia de fantasia.',
        quantidade=10
    )

    # Exemplo 2: Stoker (Terror)
    Livro.objects.create(
        titulo='Drácula',
        autor='Bram Stoker',
        editora='Constable',
        genero=gen_terror,
        publicacao=1897,
        isbn='978-00-01',
        sinopse='O clássico romance epistolar que definiu o mito do vampiro.',
        quantidade=5
    )
    
    # Exemplo 3: Machado de Assis (Romance)
    Livro.objects.create(
        titulo='Dom Casmurro',
        autor='Machado de Assis',
        editora='Livraria Garnier',
        genero=gen_romance,
        publicacao=1899,
        isbn='978-85-01', # Exemplo fictício
        sinopse='A clássica dúvida sobre a fidelidade de Capitu.',
        quantidade=3
    )

class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_virtual', '0002_auto_20260527_0927'),
    ]

    operations = [
        migrations.RunPython(popular_dados_iniciais),
    ]