#!/usr/bin/env python3
"""
token_tracker.py — Track and estimate LLM token usage via litellm
Useful for counting tokens before sending, tracking costs, and logging usage.

Usage:
  python3 tools/token_tracker.py count --model claude-sonnet-4-6 --text "your text here"
  python3 tools/token_tracker.py count --model gpt-4o --file path/to/file.txt
  python3 tools/token_tracker.py cost --model claude-sonnet-4-6 --input 1000 --output 500
  python3 tools/token_tracker.py models  # list supported models with pricing

Examples:
  echo "Hello world" | python3 tools/token_tracker.py count --model claude-sonnet-4-6 --stdin
"""

import sys
import os
import argparse
import json

def count_tokens(text, model):
    import litellm
    try:
        count = litellm.token_counter(model=model, text=text)
        return count
    except Exception as e:
        # fallback: rough estimate
        words = len(text.split())
        estimate = int(words * 1.33)
        print(f"[Warning: exact count failed ({e}), using estimate]", file=sys.stderr)
        return estimate

def get_cost(model, input_tokens, output_tokens):
    import litellm
    try:
        cost = litellm.completion_cost(
            model=model,
            prompt_tokens=input_tokens,
            completion_tokens=output_tokens,
        )
        return cost
    except Exception as e:
        return None

def main():
    parser = argparse.ArgumentParser(description="Token counter and cost estimator")
    sub = parser.add_subparsers(dest="command")

    # count
    p_count = sub.add_parser("count", help="Count tokens in text")
    p_count.add_argument("--model", default="claude-sonnet-4-6")
    p_count.add_argument("--text", help="Text to count")
    p_count.add_argument("--file", help="File to count tokens in")
    p_count.add_argument("--stdin", action="store_true", help="Read from stdin")

    # cost
    p_cost = sub.add_parser("cost", help="Estimate cost")
    p_cost.add_argument("--model", required=True)
    p_cost.add_argument("--input", type=int, required=True, help="Input tokens")
    p_cost.add_argument("--output", type=int, default=0, help="Output tokens")

    # models
    p_models = sub.add_parser("models", help="List models with pricing info")
    p_models.add_argument("--filter", help="Filter by name")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "count":
        if args.stdin:
            text = sys.stdin.read()
        elif args.file:
            with open(args.file) as f:
                text = f.read()
        elif args.text:
            text = args.text
        else:
            print("Error: provide --text, --file, or --stdin", file=sys.stderr)
            sys.exit(1)

        count = count_tokens(text, args.model)
        chars = len(text)
        words = len(text.split())

        print(f"Model:      {args.model}")
        print(f"Characters: {chars:,}")
        print(f"Words:      {words:,}")
        print(f"Tokens:     {count:,}")
        print(f"Ratio:      {count/words:.2f} tokens/word" if words else "")

        # estimate cost at typical output size
        cost_in = get_cost(args.model, count, 0)
        if cost_in is not None:
            print(f"\nCost estimate (input only): ${cost_in:.6f}")

    elif args.command == "cost":
        cost = get_cost(args.model, args.input, args.output)
        total_tokens = args.input + args.output
        print(f"Model:         {args.model}")
        print(f"Input tokens:  {args.input:,}")
        print(f"Output tokens: {args.output:,}")
        print(f"Total tokens:  {total_tokens:,}")
        if cost is not None:
            print(f"Estimated cost: ${cost:.6f}")
        else:
            print("Cost: unable to estimate (model not in litellm pricing DB)")

    elif args.command == "models":
        import litellm
        model_list = litellm.model_list if hasattr(litellm, 'model_list') else []
        if args.filter:
            model_list = [m for m in model_list if args.filter.lower() in m.lower()]
        for m in sorted(model_list)[:50]:
            print(m)

if __name__ == "__main__":
    main()
