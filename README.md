# Cheating-Detection-in-online-exam

![Django](https://img.shields.io/badge/Django-3.2.4-brightgreen)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-blue)
![scikit-image](https://img.shields.io/badge/scikit_image-0.18.2-orange)

A Django web application for capturing and analyzing images to detect cheating during exams. This project allows users to submit their details and then capture an image, which is compared to a reference image to detect cheating using Mean Squared Error (MSE).

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Features

- User registration and details submission.
- Capture and analyze exam images.
- Cheating detection based on Mean Squared Error (MSE).
- Secure and efficient handling of images.
- User-friendly web interface.

## Tech Stack

- **Django**: A high-level Python web framework.
- **OpenCV**: A powerful library for computer vision and image processing.
- **Mean Squared Error (MSE)**: Used for image comparison and cheating detection.
- **MongoDB**: Database use for storing the details of user and the captured image.

## Usage

1. **Visit the home page and submit your details.**

   - Access the web application in your browser at [http://localhost:8000](http://localhost:8000).
   - Fill in your name, email, and phone number.

2. **Capture an exam image.**

   - Follow the on-screen instructions to capture an exam image.

3. **The system will analyze the image using Mean Squared Error (MSE) and detect cheating.**

   - The system will compare the captured image to a reference image to detect any irregularities indicating cheating.

4. **Cheating or non-cheating results will be displayed based on the MSE analysis.**

   - The system will provide feedback on whether cheating is detected or not.

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. **Fork the repository:** Click the "Fork" button in the upper-right corner of this repository to create your copy.

2. **Create a branch:** Make your changes in a separate branch on your fork.

3. **Commit your changes:** After making your changes, commit them to your branch.

4. **Create a Pull Request:** Open a Pull Request (PR) from your branch to the main repository. Provide a clear description of your changes.

5. **Open issues:** Feel free to open issues for bug reports or feature requests. We appreciate your feedback!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


