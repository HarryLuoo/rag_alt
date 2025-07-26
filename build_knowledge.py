#!/usr/bin/env python3
"""
Knowledge Directory Builder
===========================

This script loads the fictional knowledge documents and builds the knowledge directory
without requiring an API key. It's useful for testing the knowledge parsing functionality.
"""

import sys
import os
import json
import re
from pathlib import Path

# Add the current directory to the path so we can import from the main script
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the necessary functions from the main script
from two_layer_agentic_system import (
    ensure_directories, 
    load_directory, 
    save_directory, 
    parse_markdown_document
)

def build_knowledge_directory():
    """Build the knowledge directory from all markdown files in the knowledge folder."""
    print("=" * 60)
    print("Building Knowledge Directory")
    print("=" * 60)
    
    # Ensure directories exist
    ensure_directories()
    
    # Define knowledge folder
    knowledge_folder = "knowledge"
    
    # Create knowledge folder if it doesn't exist
    if not os.path.exists(knowledge_folder):
        print(f"📁 Creating knowledge folder: {knowledge_folder}/")
        os.makedirs(knowledge_folder)
        print(f"ℹ️  Please place your .md files in the '{knowledge_folder}/' folder and run this script again.")
        return
    
    # Find all markdown files in the knowledge folder
    knowledge_files = []
    for file_path in Path(knowledge_folder).glob("*.md"):
        knowledge_files.append(str(file_path))
    
    if not knowledge_files:
        print(f"⚠️  No .md files found in '{knowledge_folder}/' folder.")
        print(f"ℹ️  Please place your markdown files in the '{knowledge_folder}/' folder and run this script again.")
        return
    
    print(f"🔍 Found {len(knowledge_files)} markdown files in '{knowledge_folder}/' folder:")
    for file_path in knowledge_files:
        print(f"   📄 {file_path}")
    print()
    
    # Load existing directory (if any)
    directory = load_directory()
    total_sections = 0
    
    for file_path in knowledge_files:
        if not os.path.exists(file_path):
            print(f"⚠️  Warning: File '{file_path}' not found, skipping...")
            continue
            
        print(f"\n📄 Processing: {file_path}")
        
        # Parse the document
        new_entries, chunk_count = parse_markdown_document(file_path)
        
        if chunk_count > 0:
            # Merge with existing directory
            directory.update(new_entries)
            total_sections += chunk_count
            print(f"   ✅ Added {chunk_count} sections")
            
            # Show the sections that were added
            for section_id, details in new_entries.items():
                print(f"      - {section_id}: {details['description']}")
        else:
            print(f"   ❌ No sections found in {file_path}")
    
    # Save the updated directory
    save_directory(directory)
    
    print(f"\n🎉 Knowledge directory built successfully!")
    print(f"📁 Total sections: {total_sections}")
    print(f"💾 Directory saved to: directory.json")
    print(f"📂 Chunks saved to: chunks/ folder")
    
    # Display the final directory structure
    print(f"\n📋 Knowledge Directory Contents:")
    print("=" * 40)
    
    for section_id, details in directory.items():
        print(f"🔹 {section_id}")
        print(f"   Description: {details['description']}")
        print(f"   File: {details['chunk_file']}")
        print()
    
    # Create a summary for display
    directory_summary = {}
    for section_id, details in directory.items():
        directory_summary[section_id] = {"description": details["description"]}
    
    print("📝 Directory Summary (for Agent A):")
    print(json.dumps(directory_summary, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    try:
        build_knowledge_directory()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
