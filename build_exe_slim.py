import subprocess
import sys

# Define your exclusions here
EXCLUDES = [
    # --- THE HEAVY QT BINDINGS ---
    'PyQt5', 'PyQt6', 'PySide2', 
    
    # ---- matplotlib exclusions ----
    'matplotlib.tests', 'matplotlib.testing', 'matplotlib.animation',
    'matplotlib.backends.backend_gtk3', 'matplotlib.backends.backend_gtk4',
    'matplotlib.backends.backend_wx', 'matplotlib.backends.backend_tkagg',
    'matplotlib.backends.backend_pdf', 'matplotlib.backends.backend_ps',
    'matplotlib.backends.backend_svg', 'matplotlib.backends.backend_webagg',

    # Python GUI library #
    'tkinter', 'tkinter.filedialog', 'turtle', "notebook", "jedi",
    
    # --- PyQt/PySide modules you ARE NOT using ---
    'PySide6.QtWebEngine', 'PySide6.QtWebEngineCore', 'PySide6.QtNetwork', 'PySide6.QtSql', 'PySide6.QtXml', 'PySide6.QtPdf',

    # --- PANDAS/NUMPY BLOAT ---
    'scipy', 'numpy.tests', 'sqlalchemy', 'openpyxl',
    'pyxlsb', 'xlrd', 'tables', 'pyarrow', 'fastparquet', 'jinja2',
    'triton', 'nvidia',

    # ---- AI / Machine Learning ----
    'sklearn', 'tensorflow', 'keras', 'torch', 'torchvision', 'torchaudio',
    'xgboost', 'lightgbm', 'catboost', 'transformers', 'sentencepiece',
    'nltk', 'spacy', 'gensim', 'onnx', 'onnxruntime', 'openvino', 'jax', 'jaxlib'
]

# Build the command
cmd = [
    sys.executable, "-m", "nuitka",
    "--standalone",
     "--deployment",
    # "--onefile",
    "--onefile-tempdir-spec={PROGRAM_DIR}/_cache",
    "--mingw64",
    
    # PLUGINS & QT CONFIG
    "--plugin-enable=pyside6",
    "--plugin-enable=anti-bloat",
    "--include-module=PySide6.QtOpenGL",
    "--include-module=PySide6.QtOpenGLWidgets",
    "--windows-console-mode=disable", # Change to 'disable' for final release
    
    # ASSETS & DATA
    "--windows-icon-from-ico=icon.ico",
    
    # COMPILATION STRATEGY
    "--follow-imports",
    "--prefer-source-code",
    "--output-dir=dist",
    "--remove-output", 
    
    "main.py"
]
# Append each exclusion with the correct flag
for module in EXCLUDES:
    cmd.append(f"--nofollow-import-to={module}")

print(f"Starting build for main.py with {len(EXCLUDES)} exclusions...")
print(f"Compiling: main.py + project.py + gui_ui.py")

print(f"Compiling: main.py")

try:
    subprocess.run(cmd, check=True)
    print("\n✅ Build Complete! Your executable is in the 'dist' folder.")
except subprocess.CalledProcessError:
    print("\n❌ Build failed. Check the error messages above.")