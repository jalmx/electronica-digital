import os
import yaml
from pathlib import Path
import re

def extract_metadata_and_title(file_path: Path) -> tuple[dict, str | None]:
    """
    Abre el archivo Markdown y extrae:
    1. El diccionario de metadatos en el Frontmatter YAML (si existe).
    2. El primer título `# Header` dentro del documento (si existe).
    """
    metadata = {}
    h1_title = None
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extract Frontmatter
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                metadata = yaml.safe_load(parts[1]) or {}
                body = parts[2]
                
        # Buscar el primer título H1 (# Título) en el cuerpo del archivo
        match = re.search(r"^\s*#\s+(.+)$", body, re.MULTILINE)
        if match:
            h1_title = match.group(1).strip()
            
    except Exception as e:
        print(f"[Hook Error] Error procesando {file_path.name}: {e}")
        
    return metadata, h1_title


def on_pre_build(config):
    docs_dir = Path(config["docs_dir"])
    
    # Escaneamos todas las subcarpetas dentro de docs/
    for current_dir, dirs, files in os.walk(docs_dir):
        folder_path = Path(current_dir)
        md_files = [f for f in files if f.endswith(".md")]
        
        if not md_files:
            continue
            
        should_create_index = False
        files_info = {}

        # 1. Analizar todos los archivos de la carpeta
        for file_name in md_files:
            file_path = folder_path / file_name
            meta, h1_title = extract_metadata_and_title(file_path)
            files_info[file_name] = {"meta": meta, "h1": h1_title}
            
            # Verificar si algún archivo activa la bandera
            if meta.get("create_index") is True:
                should_create_index = True

        # 2. Generar el index.md si corresponde
        if should_create_index:
            index_path = folder_path / "index.md"
            
            # Nombre de la carpeta formateado para el título del índice
            folder_title = folder_path.name.replace("-", " ").replace("_", " ").title()
            
            lines = [
                "---",
                f"title: {folder_title}",
                "---\n",
                "![banner](../assets/banner_class_85.png)\n",
                "<!-- GENENRATED AUTOMATIC - NO CHANGE -->\n",
                f"# {folder_title}",
                
            ]

            for file_name in sorted(md_files):
                if file_name == "index.md":
                    continue  # Evitar autolinkear el propio índice
                
                info = files_info.get(file_name, {})
                meta = info.get("meta", {})
                h1 = info.get("h1")
                
                # Respetar si el archivo especifica que no quiere ser indexado
                if meta.get("index") is False:
                    continue
                
                # --- Jerarquía de Selección del Título del Enlace ---
                # 1. Metadato 'title' del Frontmatter
                # 2. Encabezado '# Título' dentro del archivo
                # 3. Formato derivado del nombre del archivo (Fallback)
                if meta.get("title"):
                    link_title = meta["title"]
                elif h1:
                    link_title = h1
                else:
                    link_title = Path(file_name).stem.replace("-", " ").replace("_", " ").title()
                
                lines.append(f"- [{link_title}]({file_name})")

            # Escribir físicamente en disco
            with open(index_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines) + "\n\n<!-- GENENRATED AUTOMATIC - NO CHANGE -->")
                
            print(f"[Hook] ÍNDICE GENERADO -> {index_path.relative_to(docs_dir)}")