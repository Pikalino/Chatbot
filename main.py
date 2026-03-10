import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=args.user_prompt)]
        )
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
            ),
        )

        if not response.usage_metadata:
            raise RuntimeError("Gemini API response appears to be malformed")

        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        if not response.candidates:
            print("No response from model.")
            return

        candidate = response.candidates[0]

        if not candidate.content:
            print("No candidate content returned.")
            return

        # Add the model's response to conversation history
        messages.append(candidate.content)

        # If there are no function calls, this is the final answer
        if not response.function_calls:
            print(response.text)
            return

        function_response_parts = []

        for function_call in response.function_calls:
            result = call_function(function_call, verbose)

            if (
                not result.parts
                or not result.parts[0].function_response
                or not result.parts[0].function_response.response
            ):
                raise RuntimeError(f"Empty function response for {function_call.name}")

            if verbose:
                print(f"-> {result.parts[0].function_response.response}")

            function_response_parts.append(result.parts[0])

        # Add tool responses as a single tool message
        messages.append(
            types.Content(
                role="tool",
                parts=function_response_parts,
            )
        )

    print("Max iterations reached.")
    sys.exit(1)


if __name__ == "__main__":
    main()