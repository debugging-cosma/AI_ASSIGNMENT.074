CAPTCHA

Objective

CAPTCHA is used to distinguish between human users and automated bots in online systems.


Architecture Components

1. Challenge Generator
Generates tasks such as distorted text, selecting specific images, or simple puzzles.

2. Display Module
Shows the challenge to the user.

3. Input Module
Accepts the user’s answer.

4. Validation Module
Compares the user’s response with the correct answer.

5. Access Control Module
Allows or blocks access based on validation.


Working Process

1. A user attempts to log in or submit a form.

2. The system generates a CAPTCHA challenge.

3. The user provides a response.

4. The system verifies the answer.

5. If correct, access is granted; otherwise, access is denied.


Implementation Idea

The system can generate CAPTCHA challenges by randomly selecting distorted text images or simple image-based questions from a dataset. When the challenge is generated, the correct answer is stored temporarily on the server. After the user submits a response, the system compares it with the stored answer. If it matches, access is allowed; otherwise, it is rejected.