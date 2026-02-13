import os
import time
from pypdf import PdfWriter
import re

def natural_sort_key(s):
    """Sort strings with numbers in human order (1,2,3...10)."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

def get_creation_time(filepath):
    """Returns the creation time of a file."""
    return os.path.getctime(filepath)

def merge_pdfs():
    # 1. Setup
    writer = PdfWriter()
    
while True:
    output_filename = input("What do you want your combined file to be named? ").strip()

    if not output_filename:
        output_filename = "merged.pdf"

    if not output_filename.lower().endswith(".pdf"):
        output_filename += ".pdf"

    if not os.path.exists(output_filename):
        break

    print("That file already exists. Choose another name.")

    
    # 2. Get all PDF files
    # We exclude the output file so we don't try to merge it into itself if re-run
    all_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf') and f != output_filename]
    
    if not all_files:
        print("No PDF files found in this directory!")
        return

    print(f"Found {len(all_files)} PDFs.")
    
    # 3. Interactive Sorting Menu
    print("\nHow should the files be sorted?")
    print("1: Alphabetical (A-Z)")
    print("2: By Date Created")
    
    sort_choice = input("Enter choice (1 or 2): ").strip()
    
    if sort_choice == '1':
        # Alphabetical
        all_files.sort(key=natural_sort_key)
        print("\n--> Sorting Alphabetically (A-Z)...")
        
    elif sort_choice == '2':
        # Date Logic
        print("\nSort by Date:")
        print("1: Oldest to Newest (Standard)")
        print("2: Newest to Oldest (Reverse)")
        date_choice = input("Enter choice (1 or 2): ").strip()
        
        if date_choice == '1':
            all_files.sort(key=get_creation_time)
            print("\n--> Sorting by Date (Oldest -> Newest)...")
        elif date_choice == '2':
            all_files.sort(key=get_creation_time, reverse=True)
            print("\n--> Sorting by Date (Newest -> Oldest)...")
        else:
            print("Invalid choice. Defaulting to Oldest -> Newest.")
            all_files.sort(key=get_creation_time)
    else:
        print("Invalid choice. Defaulting to Alphabetical.")
        all_files.sort()

    # 4. Preview
    print("\nFirst 3 files in order:")
    for f in all_files[:3]:
        print(f" - {f}")
    
    confirm = input("\nDoes this look right? (y/n): ").lower()
    if confirm != 'y':
        print("Aborting.")
        return

    # 5. Merge
    print("\nMerging files...")
    for filename in all_files:
        try:
            print(f"Processing: {filename}") # Uncomment if you want to see every file
            writer.append(filename)
        except Exception as e:
            print(f"Skipping {filename} due to error: {e}")

    # 6. Save
    print(f"Writing final file to {output_filename}...")
    with open(output_filename, "wb") as out_file:
        writer.write(out_file)
    
    print("\nSuccess!")

if __name__ == "__main__":

    merge_pdfs()
