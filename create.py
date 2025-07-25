#!/usr/bin/env python3
"""
Python program to create folder structure and corresponding files
based on the provided file tree structure.
"""

import os
import sys

def create_directory_structure():
    """
    Create the complete directory structure and files for the Jekyll blog theme
    """
    
    # Define the directory structure
    directories = [
        "_layouts",
        "_includes",
        "_posts",
        "assets",
        "assets/css",
        "assets/js"
    ]
    
    # Define the files to create (empty files)
    files = [
        "_config.yml",
        "_layouts/default.html",
        "_layouts/post.html",
        "_layouts/page.html",
        "_includes/header.html",
        "_includes/footer.html",
        "_includes/nav.html",
        "_includes/post-card.html",
        "_posts/2025-07-24-welcome.md",
        "assets/css/style.css",
        "assets/js/main.js",
        "index.md",
        "demo_index.html",
        "Instruction.html"
    ]
    
    # Create directories
    print("Creating directories...")
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"  Created directory: {directory}")
        except Exception as e:
            print(f"  Error creating directory {directory}: {e}")
    
    # Create empty files
    print("\nCreating files...")
    for file_path in files:
        try:
            # Ensure parent directory exists
            parent_dir = os.path.dirname(file_path)
            if parent_dir:
                os.makedirs(parent_dir, exist_ok=True)
            
            # Create empty file
            with open(file_path, 'w') as f:
                pass  # Create empty file
            print(f"  Created file: {file_path}")
        except Exception as e:
            print(f"  Error creating file {file_path}: {e}")
    
    print("\nDirectory structure creation completed!")

def main():
    """
    Main function to execute the directory structure creation
    """
    print("Jekyll Blog Theme Directory Structure Creator")
    print("=" * 50)
    
    # Check if running in the correct directory
    current_dir = os.getcwd()
    print(f"Creating structure in: {current_dir}")
    
    # Ask for confirmation
    response = input("\nDo you want to create the directory structure in this location? (y/N): ")
    
    if response.lower() in ['y', 'yes']:
        create_directory_structure()
    else:
        print("Operation cancelled.")
        sys.exit(0)

if __name__ == "__main__":
    main()