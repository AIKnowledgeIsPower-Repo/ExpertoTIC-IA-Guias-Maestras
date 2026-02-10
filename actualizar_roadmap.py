import os

def generar_roadmap():
    carpeta = './guias/'  # Nombre de la carpeta para el repo en español
    archivo_readme = 'README.md'
    
    if not os.path.exists(carpeta):
        print(f"[ERROR] La carpeta {carpeta} no existe. Por favor créala.")
        return
            
    # Obtener archivos .md ordenados
    guias = sorted([f for f in os.listdir(carpeta) if f.endswith('.md')])
    
    print(f"--- Roadmap Actualizado para el Repo en Español ---")
    print("| Sem. | Título de la Guía | Categoría | Estado |")
    print("| :--- | :--- | :--- | :--- |")
    
    for i, guia in enumerate(guias, 1):
        semana = f"{i:02d}"
        # Formatear título: quitar extensión, guiones y poner en mayúsculas
        titulo = guia.replace('.md', '').replace('-', ' ').capitalize()
        enlace = f"{carpeta}{guia}"
        estado = "✅ Listo"
        
        print(f"| {semana} | [{titulo}]({enlace}) | IA y Tecnología | {estado} |")

if __name__ == "__main__":
    generar_roadmap()
