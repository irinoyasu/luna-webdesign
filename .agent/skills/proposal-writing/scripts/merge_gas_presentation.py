#!/usr/bin/env python3
import os
import re
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Merge slideData JSON into GAS presentation JS")
    parser.add_argument("--proposal-dir", required=True, help="Path to the proposal directory containing the writing-slide folder")
    parser.add_argument("--sample-path", required=True, help="Path to the gas_presentation_sample.js file")
    
    args = parser.parse_args()
    
    writing_dir = os.path.join(args.proposal_dir, "writing-slide")
    if not os.path.exists(writing_dir):
        print(f"Error: Writing-slide directory not found at {writing_dir}")
        sys.exit(1)
        
    if not os.path.exists(args.sample_path):
        print(f"Error: Sample GAS script not found at {args.sample_path}")
        sys.exit(1)
        
    with open(args.sample_path, 'r', encoding='utf-8') as f:
        gas_content = f.read()

    versions_found = False
    
    for version in ['10min']:
        json_path = os.path.join(writing_dir, f'{version}-slideData.json')
        if not os.path.exists(json_path):
            print(f"File not found, skipping: {json_path}")
            continue
            
        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = f.read()
            
        pattern = re.compile(r'const\s+slideData\s*=\s*\[.*?\];', re.DOTALL)
        
        replacement = f"const slideData = {json_data};"
        new_gas = pattern.sub(lambda _: replacement, gas_content)
        
        out_path = os.path.join(writing_dir, f'{version}-gas_presentation.js')
        with open(out_path, 'w', encoding='utf-8') as f:
             f.write(new_gas)
             print(f"Successfully generated: {out_path}")
        versions_found = True

    if not versions_found:
        print("No <version>-slideData.json files were found to process.")
        sys.exit(1)

if __name__ == '__main__':
    main()
