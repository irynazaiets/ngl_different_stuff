import tabula

dfs = tabula.read_pdf(("new.pdf"), stream=True)
print(dfs)