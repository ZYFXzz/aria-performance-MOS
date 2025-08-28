# Convert your MIDI files to the expected jsonl format
import json
import os
from pathlib import Path
from ariautils.midi import MidiDict

def convert_midis_to_jsonl(midi_dir, output_file, max_files=100):
    """Convert MIDI files to jsonl format for testing"""
    with open(output_file, 'w') as f:
        count = 0
        for midi_file in Path(midi_dir).glob("**/*.mid*"):
            if count >= max_files:
                break
            try:
                midi_dict = MidiDict.from_midi(str(midi_file))
                json.dump(midi_dict.get_msg_dict(), f)
                f.write('\n')
                count += 1
            except Exception as e:
                print(f"Skipping {midi_file}: {e}")
    print(f"Converted {count} files")
    
    
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MIDI files to jsonl format")
    parser.add_argument("--input_dir", type=str, required=True, help="Directory containing MIDI files")
    parser.add_argument("--output_train", type=str, required=True, help="Output jsonl file path")
    parser.add_argument("--max_files", type=int, default=100, help="Maximum number of files to process")

    args = parser.parse_args()

    convert_midis_to_jsonl(
        midi_dir=args.input_dir,
        output_file=args.output_train,
        max_files=args.max_files
    )
