import os

wiki_folder = 'wiki'

def generate_index():
    with open("README.md", "w") as readme:
        readme.write("# Galaxy M52 Wiki\n\n")
        readme.write("Bem-vindo à Wiki do Galaxy M52! Aqui você encontrará todos os artigos, tutoriais e informações sobre o dispositivo.\n\n")
        
        if os.path.exists(wiki_folder):
            for file_name in os.listdir(wiki_folder):
                if file_name.endswith(".md"):
                    # Criando o link para o arquivo no índice
                    file_path = f"{wiki_folder}/{file_name}"
                    file_title = file_name.replace(".md", "").replace("_", " ").capitalize()
                    readme.write(f"- [{file_title}]({file_path})\n")
            readme.write("\n")
        else:
            readme.write("Nenhum artigo encontrado. Adicione arquivos .md na pasta `wiki/` para começar.\n")

if __name__ == "__main__":
    generate_index()
  
