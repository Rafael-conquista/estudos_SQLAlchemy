from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

repo.insert('algumFIlme', 'comedia', 2010)
repo.delete('batata')

data = repo.select()

print(data)