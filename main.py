"""
Main entry point for the notebook reader application.

This module provides functionality to read and process .ipynb notebook files.
"""

import json
from pathlib import Path
import nbformat
from typing import List, Dict, Any


def load_notebook(notebook_path: str) -> Dict[str, Any]:
    """
    Load a Jupyter notebook file and return its contents.
    
    Args:
        notebook_path: Path to the .ipynb file
        
    Returns:
        Dictionary containing the notebook data
    """
    path = Path(notebook_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Notebook not found at: {path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    
    return notebook


def extract_cells(notebook: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract all cells from a notebook.
    
    Args:
        notebook: Notebook data from load_notebook()
        
    Returns:
        List of cells with their content and metadata
    """
    cells = []
    for cell in notebook.get('cells', []):
        cell_data = {
            'type': cell.get('cell_type'),
            'source': ''.join(cell.get('source', [])),
            'metadata': cell.get('metadata', {})
        }
        cells.append(cell_data)
    
    return cells


def main():
    """Main function."""
    try:
        notebook_path = 'notebook_reader.ipynb'
        print(f"Loading notebook: {notebook_path}")
        
        notebook = load_notebook(notebook_path)
        cells = extract_cells(notebook)
        
        print(f"\nNotebook loaded successfully!")
        print(f"Total cells: {len(cells)}\n")
        
        for i, cell in enumerate(cells, 1):
            print(f"Cell {i} ({cell['type']}): {cell['source'][:50]}...")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

print("Hello world")
