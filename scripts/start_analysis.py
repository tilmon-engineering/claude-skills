#!/usr/bin/env python3
import sys
import shutil
from pathlib import Path
from datetime import datetime

def main():
    if len(sys.argv) != 3:
        print("Usage: start-analysis <process> <name>")
        sys.exit(1)

    process = sys.argv[1]
    name = sys.argv[2]

    # Create dated directory name
    today = datetime.now().strftime("%Y-%m-%d")
    analysis_dir = Path(f"analysis/{process}/{today}-{name}")

    # Check if directory already exists
    if analysis_dir.exists():
        response = input(f"Directory {analysis_dir} already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)
        shutil.rmtree(analysis_dir)

    # Create directory
    analysis_dir.mkdir(parents=True, exist_ok=True)

    # Copy template
    template_dir = Path("analysis/_template")
    if template_dir.exists():
        for item in template_dir.iterdir():
            if item.is_file():
                shutil.copy(item, analysis_dir)
            elif item.is_dir():
                shutil.copytree(item, analysis_dir / item.name)

    print(f"✓ Analysis workspace created at: {analysis_dir}")
    print(f"\nNext steps:")
    print(f"1. Invoke the {process} skill with your analytical goal")
    print(f"2. Claude will guide you through the analysis process")

if __name__ == "__main__":
    main()
