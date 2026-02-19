```python
import argparse
import subprocess

def main():
 parser = argparse.ArgumentParser(description="Gemini CLI")
 subparsers = parser.add_subparsers(dest="command", help="Available commands")

 # Example command: run
 run_parser = subparsers.add_parser("run", help="Run a Gemini query")
 run_parser.add_argument("query", help="The Gemini query to run")

 # Example command: list
 list_parser = subparsers.add_parser("list", help="List available Gemini models")
 # Add more arguments as needed


 args = parser.parse_args()

 if args.command == "run":
 try:
 # Replace with your actual Gemini API call
 result = subprocess.run(["gemini", args.query], capture_output=True, text=True, check=True)
 print(result.stdout)
 except subprocess.CalledProcessError as e:
 print(f"Error running Gemini query: {e}")
 except FileNotFoundError:
 print("Error: 'gemini' command not found. Make sure Gemini is installed and in your PATH.")

 elif args.command == "list":
 # Replace with your actual Gemini model listing logic
 print("Available Gemini models:")
 print("- model1")
 print("- model2")
 # ...


 else:
 parser.print_help()


if __name__ == "__main__":
 main()

```
