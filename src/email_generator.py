import os
import random
from openai import OpenAI
import logging

class EmailGenerator:
    def __init__(self):
        # Initialize the OpenAI API client with the provided API key
        api_key = "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"
        self.client = OpenAI(api_key=api_key)

        print("prompting AI model...")
        # Define a generic prompt for phishing email generation
        self.phishing_prompt = "Generate a phishing email that appears to be from a reputable organization, informing the recipient, [Recipient's Name], about an urgent matter and urging them to take immediate action by clicking on the link [malicious link] to address the issue. The email should be convincing and persuasive. The company name should sound real"

    def generate_phishing_email(self, target_name, malicious_link):
        """
        Generate a phishing email template.

        Args:
            target_name (str): The name of the target recipient.
            malicious_link (str): The malicious link to be included in the email.

        Returns:
            str: A phishing email template.
        """
        # Replace the placeholders with the target name and provided malicious link
        placeholders = {
            "[Recipient's Name]": target_name,
            "[malicious link]": malicious_link
        }
        print("prompting AI model...")
        prompt_with_placeholders = self.phishing_prompt
        for placeholder, value in placeholders.items():
            prompt_with_placeholders = prompt_with_placeholders.replace(placeholder, value)

        # Define the prompt and completion parameters
        parameters = {
            "messages": [
                {
                    "role": "assistant",
                    "content": prompt_with_placeholders,
                }
            ],
            "model": "gpt-4",
        }
        print("AI model generating phishing mail...")
        # Generate humanized email content using ChatGPT
        response = self.client.chat.completions.create(**parameters)
        print("Phishing mail successfully generated...")
        # Extract the completion text from the response
        completion_text = response.choices[0].message.content.strip()
        return completion_text


def main():
    # Initialize the EmailGenerator
    email_generator = EmailGenerator()

    # Example usage: Generate a phishing email template for a target recipient
    target_name = "John Doe"  # Example target name
    malicious_link = "https://www.example.com/verify_account?id=johndoe@example.com"  # Example malicious link
    phishing_email = email_generator.generate_phishing_email(target_name, malicious_link)

    # Print the phishing email content
    print("Phishing Email:")
    print(phishing_email)

if __name__ == "__main__":
    main()
