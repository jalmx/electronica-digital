import argparse
import re
from pathlib import Path

# Extensiones de imagen soportadas
IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".bmp",
    ".tiff",
    ".ico",
}

# Expresiones regulares para capturar imágenes en Markdown y HTML
MARKDOWN_IMAGE_REGEX = re.compile(r"!\[.*?\]\((.*?)\)")
HTML_IMAGE_REGEX = re.compile(
    r'<img\s+[^>]*src=["\'](.*?)["\']', re.IGNORECASE
)


def collect_physical_images(image_paths: list[Path]) -> dict[str, Path]:
    """Escanea las rutas indicadas y devuelve un diccionario de rutas de imágenes."""
    images = {}
    for img_dir in image_paths:
        if not img_dir.exists():
            print(f"Advertencia: La ruta de imágenes '{img_dir}' no existe. Omitiendo...")
            continue

        for path in img_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
                try:
                    normalized_path = (
                        path.resolve().relative_to(Path.cwd().resolve()).as_posix()
                    )
                except ValueError:
                    normalized_path = path.resolve().as_posix()

                images[normalized_path] = path
    return images


def extract_referenced_images(
    docs_path: Path, all_images: dict[str, Path]
) -> set[Path]:
    """Escanea todos los archivos .md y resuelve las rutas de imágenes referenciadas."""
    used_images = set()

    for md_file in docs_path.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        # Extraer enlaces de imágenes en Markdown y HTML
        matches = MARKDOWN_IMAGE_REGEX.findall(
            content
        ) + HTML_IMAGE_REGEX.findall(content)

        for match in matches:
            # Limpiar parámetros de consulta o anclas (ej. image.png#only-light)
            clean_match = match.split("#")[0].split("?")[0].strip()

            if not clean_match or clean_match.startswith(
                ("http://", "https://", "data:")
            ):
                continue

            resolved_path = None

            if clean_match.startswith("/"):
                # Ruta absoluta respecto a la carpeta docs_path
                target = docs_path / clean_match.lstrip("/")
                resolved_path = target.resolve()
            else:
                # Ruta relativa al archivo Markdown actual
                target = md_file.parent / clean_match
                resolved_path = target.resolve()

            # Comparar con la lista de imágenes físicas indexadas
            for _, img_path in all_images.items():
                if img_path.resolve() == resolved_path:
                    used_images.add(img_path.resolve())
                    break

    return used_images


def main():
    parser = argparse.ArgumentParser(
        description="Encuentra imágenes no utilizadas en un proyecto MkDocs."
    )
    parser.add_argument(
        "-i",
        "--images-dir",
        nargs="+",
        required=True,
        help="Ruta(s) de la(s) carpeta(s) donde están almacenadas las imágenes a verificar.",
    )
    parser.add_argument(
        "-d",
        "--docs-dir",
        default="docs",
        help="Ruta donde están los archivos .md (Por defecto: 'docs').",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="imagenes_no_usadas.txt",
        help="Nombre del archivo TXT de salida (Por defecto: 'imagenes_no_usadas.txt').",
    )

    args = parser.parse_args()

    docs_dir = Path(args.docs_dir)
    image_dirs = [Path(p) for p in args.images_dir]
    output_file = Path(args.output)

    if not docs_dir.exists():
        print(f"Error: La carpeta de documentación '{docs_dir}' no existe.")
        return

    print(f"Indexando archivos Markdown en: '{docs_dir}'...")
    print(f"Buscando imágenes físicas en: {[str(p) for p in image_dirs]}...")

    physical_images = collect_physical_images(image_dirs)

    if not physical_images:
        print("No se encontraron imágenes en la(s) ruta(s) especificada(s).")
        return

    print(f"Se encontraron {len(physical_images)} imágenes físicas.")
    print("Analizando referencias en los archivos .md...")

    used_images = extract_referenced_images(docs_dir, physical_images)

    # Identificar imágenes huérfanas
    unused_images = [
        path
        for path in physical_images.values()
        if path.resolve() not in used_images
    ]

    # Guardar resultados en el archivo TXT
    with open(output_file, "w", encoding="utf-8") as f:
        for img in sorted(unused_images):
            f.write(f"{img.as_posix()}\n")

    print("\n--- Resultados ---")
    print(f"Imágenes totales indexadas: {len(physical_images)}")
    print(f"Imágenes en uso: {len(used_images)}")
    print(f"Imágenes sin usar: {len(unused_images)}")
    print(f"Lista guardada en: '{output_file.resolve()}'")


if __name__ == "__main__":
    main()